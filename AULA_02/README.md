# Residência - Trilhas em Tecnologias: IA Generativa & RAG

Repositório destinado às atividades desenvolvidas durante o programa de **Residência - Trilhas em Tecnologias: IA Generativa & RAG**.

**Aluna:** Fernanda Fregulha  
**Aula:** 02 - Extração de Metadados de Documentos com Structured Outputs

---

## Sobre a atividade

Nesta segunda aula, o objetivo foi processar arquivos **Markdown** (convertidos a partir de PDFs de artigos científicos) e extrair metadados relevantes — como título, autores e ano de publicação — utilizando **Structured Outputs**, recurso que garante que a resposta de um LLM siga um formato JSON pré-definido.

O material original da aula referencia **OpenRouter** e **Groq** como provedores compatíveis com Structured Outputs. Optei por utilizar a **GroqCloud API**, pelos mesmos motivos da Aula 01: acesso gratuito e compatibilidade com o SDK da OpenAI.

A atividade foi dividida em duas etapas: conversão de PDF para Markdown e, em seguida, extração estruturada dos metadados de cada arquivo `.md`.

---

## Tecnologias utilizadas

- Python
- GroqCloud API
- OpenAI Python SDK
- python-dotenv
- Structured Outputs (JSON Schema)
- Virtual Environment (`venv`)
- Visual Studio Code

Modelo utilizado:

```text
openai/gpt-oss-20b
```

---

## Estrutura do projeto

```text
AULA_02/
├── converter.py                    # Converte PDFs para Markdown
├── extrair_metadados.py            # Extrai metadados dos .md via LLM
├── bioetica_e_ia.pdf
├── bioetica_e_ia.md
├── output_bioetica_e_ia.json
├── escrita_academica_ia.pdf
├── escrita_academica_ia.md
├── output_escrita_academica_ia.json
├── twitter_algoritmo.pdf
├── twitter_algoritmo.md
├── output_twitter_algoritmo.json
└── packages.txt
```

O arquivo `.env` é utilizado apenas localmente para armazenar a chave da API e não deve ser versionado.

---

## Configuração do projeto

### 1. Criar o ambiente virtual

No Windows:

```bash
python -m venv venv
```

No Linux/macOS:

```bash
python3 -m venv venv
```

---

### 2. Ativar o ambiente virtual

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

Quando o ambiente virtual estiver ativo, o terminal deverá apresentar:

```text
(venv)
```

no início da linha.

---

### 3. Instalar as dependências

Com o ambiente virtual ativado:

```bash
pip install openai python-dotenv
```

Principais dependências utilizadas:

```text
openai
python-dotenv
```

---

## Configuração da API

Assim como na Aula 01, esta atividade utiliza a **GroqCloud API** por meio do SDK da OpenAI, apontando para o endpoint compatível da Groq.

Crie uma chave de API no GroqCloud e configure um arquivo `.env` dentro da pasta `AULA_02`.

Exemplo:

```env
OPENAI_API_KEY=sua_chave_aqui
OPENAI_MODEL=openai/gpt-oss-20b
```

A chave da API não deve ser adicionada diretamente ao código ou publicada no repositório.

---

## Alteração para utilização do GroqCloud

O cliente é configurado apontando para o endpoint da Groq, mantendo o SDK da OpenAI:

```python
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
```

O Structured Output é definido via `response_format`, com um JSON Schema `strict`, garantindo que a resposta do modelo siga exatamente os campos esperados:

```python
response_format={
    "type": "json_schema",
    "json_schema": {
        "name": "metadados_paper",
        "schema": schema,
        "strict": True
    }
}
```

---

## Executando a atividade

Entre na pasta da Aula 02:

```bash
cd AULA_02
```

Execute o script de extração de metadados:

```bash
python extrair_metadados.py
```

O script processa automaticamente todos os arquivos `.md` presentes na pasta e gera, para cada um, um arquivo `output_<nome_do_arquivo>.json` com o seguinte formato:

```json
{
  "titulo": "Título do trabalho",
  "autores": [
    "Autor 1",
    "Autor 2"
  ],
  "ano": 2024
}
```

---

## Decisões técnicas

Durante a implementação, alguns ajustes foram necessários para lidar com limitações reais da API gratuita e com a estrutura dos documentos:

- **Truncamento inteligente do conteúdo:** o plano gratuito da Groq possui limite de 8.000 tokens por minuto (TPM). Para evitar erros de `rate limit`, o script envia apenas o início do documento (título, autores, resumo) e o final (datas de submissão/aprovação, afiliações), em vez do texto completo — reduzindo o consumo de tokens sem perder as informações relevantes para a extração.
- **`temperature=0`:** garante respostas mais determinísticas, adequadas para uma tarefa de extração factual, não criativa.
- **Campo `ano` aceita `null`:** quando a data de publicação não está explícita no texto, o modelo retorna `null` em vez de estimar um valor, evitando metadados incorretos.
- **Orientação explícita no prompt:** o modelo foi instruído a não confundir anos citados no corpo do texto (ex: período de artigos revisados na metodologia) com o ano de publicação do próprio artigo, e a utilizar a data de "Aprovado" como referência quando não houver data de publicação explícita.

---

## Executando novamente o projeto

Após a primeira configuração, não é necessário criar o ambiente virtual nem instalar as dependências novamente.

Basta acessar a pasta do projeto e ativar o ambiente virtual.

No Windows:

```bash
venv\Scripts\activate
```

Depois:

```bash
cd AULA_02
python extrair_metadados.py
```

---

## Como sair do Ambiente Virtual

Quando terminar de trabalhar no projeto, o ambiente virtual pode ser desativado com:

```bash
deactivate
```

O `(venv)` desaparecerá do início da linha do terminal, indicando que o ambiente virtual foi desativado.

---

## Segurança

O `.gitignore` está configurado para evitar o versionamento de arquivos sensíveis e arquivos desnecessários:

```gitignore
.env
.env.*
!.env.example

venv/
.venv/

__pycache__/
*.pyc
```

A chave real deve existir apenas no arquivo `.env` local.

---

## Conceitos trabalhados

Nesta atividade foram explorados conceitos relacionados a:

- Structured Outputs (JSON Schema);
- Extração de metadados de documentos com LLMs;
- Conversão de PDF para Markdown;
- Engenharia de prompt para tarefas de extração factual;
- Gerenciamento de limites de taxa (rate limits / TPM) de APIs;
- Manipulação de arquivos JSON em Python;
- Variáveis de ambiente e gerenciamento seguro de API Keys;
- Utilização de provedores compatíveis com o SDK da OpenAI.

---

## Autora

**Fernanda Fregulha**

Atividade desenvolvida durante o programa:

**Residência - Trilhas em Tecnologias: IA Generativa & RAG**

---

## Repositório

**Residencia-Trilhas-em-Tecnologias-IA-Generativa-RAG**

Repositório público destinado ao registro das atividades, estudos e projetos desenvolvidos ao longo do programa de residência.