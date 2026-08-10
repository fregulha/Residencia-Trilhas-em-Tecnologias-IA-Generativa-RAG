import os
from pathlib import Path

os.environ["TORCH_COMPILE_DISABLE"] = "1"

from docling.document_converter import DocumentConverter


# Localiza automaticamente a pasta onde este arquivo está salvo
PASTA_AULA_04 = Path(__file__).resolve().parent

# Procura somente arquivos PDF dentro da AULA_04
pdfs = sorted(PASTA_AULA_04.glob("*.pdf"))

print("Iniciando conversão...")
print(f"Pasta utilizada: {PASTA_AULA_04}")
print(f"Foram encontrados {len(pdfs)} PDFs")

if not pdfs:
    raise FileNotFoundError(
        f"Nenhum PDF foi encontrado em: {PASTA_AULA_04}"
    )

converter = DocumentConverter()

arquivos_convertidos = []
arquivos_com_erro = []

for numero, pdf in enumerate(pdfs, start=1):
    print()
    print(f"[{numero}/{len(pdfs)}] Convertendo: {pdf.name}")

    try:
        resultado = converter.convert(str(pdf))

        markdown = resultado.document.export_to_markdown()

        caminho_markdown = pdf.with_suffix(".md")

        caminho_markdown.write_text(
            markdown,
            encoding="utf-8"
        )

        arquivos_convertidos.append(caminho_markdown.name)

        print(f"Markdown criado: {caminho_markdown.name}")

    except Exception as erro:
        arquivos_com_erro.append({
            "arquivo": pdf.name,
            "erro": str(erro)
        })

        print(f"Erro ao converter {pdf.name}: {erro}")


print()
print("=" * 60)
print("CONVERSÃO FINALIZADA")
print("=" * 60)
print(f"PDFs encontrados: {len(pdfs)}")
print(f"Arquivos convertidos: {len(arquivos_convertidos)}")
print(f"Arquivos com erro: {len(arquivos_com_erro)}")

if arquivos_convertidos:
    print()
    print("Markdown gerados:")

    for nome in arquivos_convertidos:
        print(f"- {nome}")

if arquivos_com_erro:
    print()
    print("Erros encontrados:")

    for item in arquivos_com_erro:
        print(f"- {item['arquivo']}: {item['erro']}")