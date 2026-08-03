# Residência - Trilhas em Tecnologias: IA Generativa & RAG

Repositório destinado às atividades desenvolvidas durante o programa de **Residência - Trilhas em Tecnologias: IA Generativa & RAG**.

**Aluna:** Fernanda Fregulha  
**Aula:** 01 - Introdução à IA

---

## Sobre a atividade

Nesta primeira aula, o objetivo foi configurar o ambiente de desenvolvimento em Python e realizar uma primeira interação com um **Large Language Model (LLM)** através de uma API.

O material original da aula utiliza a **API da OpenAI**. Durante a execução da atividade, optei por utilizar a **GroqCloud API**, que disponibiliza acesso gratuito a modelos de linguagem e possui compatibilidade com o SDK da OpenAI.

Dessa forma, foi possível manter a estrutura proposta na aula, realizando apenas pequenas alterações na configuração do cliente, modelo e variáveis de ambiente.

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
pip install -r requirements.txt
```

Entre as principais dependências utilizadas estão:

```text
openai
python-dotenv
```

---

## Configuração da API

O projeto original utiliza a API da OpenAI.

Para a execução desta atividade, utilizei a **GroqCloud API**, mantendo o SDK da OpenAI e alterando apenas a configuração necessária para direcionar as requisições ao endpoint da Groq.

Crie uma chave de API no GroqCloud e configure um arquivo `.env` dentro da pasta `AULA_01`.

Exemplo:

```env
GROQ_API_KEY=sua_chave_aqui
OPENAI_MODEL=openai/gpt-oss-20b
```

A chave da API não deve ser adicionada diretamente ao código ou publicada no repositório.

---

## Alteração para utilização do GroqCloud

No material original, o cliente é configurado utilizando:

```python
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

Para utilizar o GroqCloud, a configuração foi adaptada para:

```python
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
```

O modelo também foi alterado.

Em vez de:

```text
gpt-4o-mini
```

foi utilizado:

```text
openai/gpt-oss-20b
```

Além disso, o parâmetro:

```python
store=True
```

presente no exemplo original foi removido para manter compatibilidade com a API utilizada.

---

## Executando a atividade

Entre na pasta da Aula 01:

```bash
cd AULA_01
```

Execute o script:

```bash
python hello_llm.py
```

O programa envia uma mensagem para o modelo de linguagem e exibe a resposta diretamente no terminal.

Exemplo de prompt:

```text
Qual a capital do Brasil?
```

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
cd AULA_01
python hello_llm.py
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

.ipynb_checkpoints/
```

O arquivo `.env.example` pode ser mantido no repositório como referência:

```env
GROQ_API_KEY=sua_chave_aqui
OPENAI_MODEL=openai/gpt-oss-20b
```

A chave real deve existir apenas no arquivo `.env` local.

---

## Conceitos trabalhados

Nesta atividade foram explorados conceitos iniciais relacionados a:

- Inteligência Artificial;
- Large Language Models (LLMs);
- Prompts;
- APIs de modelos de linguagem;
- Variáveis de ambiente;
- Gerenciamento seguro de API Keys;
- Ambientes virtuais Python;
- Integração entre Python e LLMs;
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
