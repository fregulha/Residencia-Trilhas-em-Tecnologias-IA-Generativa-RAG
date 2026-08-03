# Residência - Trilhas em Tecnologias: IA Generativa & RAG

Repositório destinado às atividades desenvolvidas durante o programa de **Residência - Trilhas em Tecnologias: IA Generativa & RAG**.

**Aluna:** Fernanda Fregulha  
**Aula:** 01 - Introdução à IA

---

## Sobre a atividade

Nesta primeira aula, o objetivo foi configurar o ambiente Python e realizar uma integração simples com um modelo de linguagem utilizando uma API.

O projeto original utiliza a API da OpenAI. Para esta atividade, utilizei a **GroqCloud API**, mantendo a biblioteca `openai` e adaptando apenas a configuração do cliente.

---

## Tecnologias utilizadas

- Python
- GroqCloud API
- OpenAI Python SDK
- python-dotenv
- Virtual Environment (`venv`)
- Jupyter Notebook
- Visual Studio Code

Modelo utilizado:

```text
openai/gpt-oss-20b
```

---

## Estrutura do projeto

```text
IA/
├── AULA_01/
│   ├── hello_llm.py
│   └── hello_llm.ipynb
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

O arquivo `.env` é utilizado apenas localmente e não deve ser versionado.

---

## Configuração

### 1. Criar o ambiente virtual

Windows:

```bash
python -m venv venv
```

Linux/macOS:

```bash
python3 -m venv venv
```

### 2. Ativar o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## Configuração da API

Crie uma chave no GroqCloud e configure um arquivo `.env` dentro da pasta `AULA_01`.

Exemplo:

```env
GROQ_API_KEY=sua_chave_aqui
OPENAI_MODEL=openai/gpt-oss-20b
```

A chave da API não deve ser adicionada diretamente ao código nem enviada para o repositório.

---

## Integração com o GroqCloud

O cliente utiliza o SDK da OpenAI apontando para o endpoint da Groq:

```python
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
```

O modelo é carregado através da variável de ambiente:

```python
modelo = os.getenv(
    "OPENAI_MODEL",
    "openai/gpt-oss-20b"
)
```

---

## Executando a atividade

Entre na pasta:

```bash
cd AULA_01
```

Execute:

```bash
python hello_llm.py
```

O script envia uma mensagem ao modelo de linguagem e exibe a resposta no terminal.

Exemplo utilizado:

```text
Qual a capital do Brasil?
```

---

## Conceitos trabalhados

- Inteligência Artificial
- Large Language Models (LLMs)
- Prompts
- APIs de modelos de linguagem
- Variáveis de ambiente
- Gerenciamento de API Keys
- Ambientes virtuais Python
- Integração entre Python e LLMs

---

## Segurança

O `.gitignore` deve conter, no mínimo:

```gitignore
venv/
.env
**/.env
__pycache__/
*.pyc
.ipynb_checkpoints/
```

O arquivo `.env.example` pode ser versionado como referência:

```env
GROQ_API_KEY=sua_chave_aqui
OPENAI_MODEL=openai/gpt-oss-20b
```

---

## Autora

**Fernanda Fregulha**

Atividade desenvolvida no programa:

**Residência - Trilhas em Tecnologias: IA Generativa & RAG**