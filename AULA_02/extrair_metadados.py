import json
import time
import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Carrega variáveis do .env (OPENAI_API_KEY, OPENAI_MODEL)
load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"  # endpoint da Groq, compatível com OpenAI
)

MODEL = os.environ.get("OPENAI_MODEL", "openai/gpt-oss-20b")


def extrair_texto_relevante(conteudo: str, chars_inicio: int = 2500, chars_fim: int = 1500) -> str:
    """
    Pega o início do documento (título, autores, resumo) e o final
    (datas de submissão/aprovação, afiliações, correspondência),
    que é onde normalmente aparecem os metadados em artigos científicos.
    """
    if len(conteudo) <= chars_inicio + chars_fim:
        return conteudo
    inicio = conteudo[:chars_inicio]
    fim = conteudo[-chars_fim:]
    return f"{inicio}\n\n[... trecho omitido ...]\n\n{fim}"


def extrair_metadados(caminho_md: str) -> dict:
    """
    Extrai metadados (titulo, autores, ano) de um arquivo .md
    usando Structured Outputs via Groq (API compatível com OpenAI).
    """
    conteudo = Path(caminho_md).read_text(encoding="utf-8")
    conteudo_relevante = extrair_texto_relevante(conteudo)

    schema = {
        "type": "object",
        "properties": {
            "titulo": {"type": "string"},
            "autores": {
                "type": "array",
                "items": {"type": "string"}
            },
            "ano": {"type": ["integer", "null"]}
        },
        "required": ["titulo", "autores", "ano"],
        "additionalProperties": False
    }

    resposta = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Você extrai metadados bibliográficos de textos acadêmicos. "
                    "Responda apenas com o JSON solicitado, sem texto adicional. "
                    "Use APENAS informações explicitamente presentes no texto. "
                    "Para o ANO de publicação: procure primeiro por uma data explícita "
                    "de publicação. Se não houver, mas houver datas de 'Recebido', "
                    "'Revisado' e 'Aprovado', use o ano da data de 'Aprovado' (é o ano "
                    "mais próximo da publicação real). NÃO confunda com anos citados no "
                    "corpo do texto sobre a metodologia da pesquisa (ex: 'artigos "
                    "publicados entre 2015 e 2024' refere-se à literatura revisada, não "
                    "à data de publicação deste artigo). "
                    "Se realmente não houver informação suficiente, retorne null."
                )
            },
            {
                "role": "user",
                "content": f"Extraia os metadados deste documento:\n\n{conteudo_relevante}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "metadados_paper",
                "schema": schema,
                "strict": True
            }
        },
        max_tokens=500,
        temperature=0
    )

    dados = json.loads(resposta.choices[0].message.content)
    return dados


def processar_arquivo(caminho_md: str, pasta_saida: str = ".") -> None:
    nome_base = Path(caminho_md).stem
    print(f"Processando {Path(caminho_md).name}...")

    try:
        metadados = extrair_metadados(caminho_md)
        caminho_saida = Path(pasta_saida) / f"output_{nome_base}.json"
        with open(caminho_saida, "w", encoding="utf-8") as f:
            json.dump(metadados, f, ensure_ascii=False, indent=2)
        print(f"  ✅ Salvo em {caminho_saida}")
        print(f"  {json.dumps(metadados, ensure_ascii=False)}")
    except Exception as e:
        print(f"  ❌ Erro ao processar {Path(caminho_md).name}: {e}")


if __name__ == "__main__":
    pasta_entrada = "."   # pasta onde estão os .md
    pasta_saida = "."     # pasta onde salvar os output_*.json

    arquivos_md = list(Path(pasta_entrada).glob("*.md"))

    if not arquivos_md:
        print("Nenhum arquivo .md encontrado na pasta.")

    for arquivo in arquivos_md:
        processar_arquivo(str(arquivo), pasta_saida)
        time.sleep(2)  # respeita o rate limit (TPM) entre requisições

    print("\nConcluído.")