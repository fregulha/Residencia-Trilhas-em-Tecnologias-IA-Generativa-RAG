# Residência — Trilhas em Tecnologias: IA Generativa & RAG

Repositório destinado ao registro das atividades desenvolvidas durante o programa de **Residência — Trilhas em Tecnologias: IA Generativa & RAG**, do Instituto ECOA — PUC-Rio.

**Aluna:** Fernanda Fregulha

---

## 📚 Aulas

- [Aula 01 — Introdução à IA](./AULA_01/README.md) — Configuração do ambiente e primeira interação com um modelo de linguagem por meio de API.

- [Aula 02 — Extração de Metadados com Structured Outputs](./AULA_02/README.md) — Conversão de artigos científicos de PDF para Markdown e extração estruturada de metadados, como título, autores e ano.

- [Aula 03 — Embeddings e Busca Semântica Manual](./AULA_03/README.md) — Implementação de métricas de distância entre embeddings, comparação semântica de termos e frases e busca por linha, parágrafo e capítulo.

- [Aula 04 — Extração de PDF e Estratégias de Chunking](./AULA_04/README.md) — Conversão de artigos científicos para Markdown, avaliação da preservação de títulos, tabelas, fórmulas e imagens e comparação de dez estratégias de divisão de texto com LangChain.

---

## 🧩 Conceitos trabalhados

- Consumo de modelos de linguagem por API
- Prompting e geração de texto
- Structured Outputs
- Extração de metadados
- Conversão de PDF para Markdown
- Embeddings
- Distância euclidiana
- Similaridade e distância de cosseno
- Busca semântica manual
- Chunking de documentos
- Chunk size e chunk overlap
- Divisão por parágrafo, sentença e seção
- Separação recursiva de texto
- Preparação de documentos para RAG

---

## 🛠️ Tecnologias gerais

- Python
- Jupyter Notebook
- GroqCloud API
- OpenRouter Embeddings API
- OpenAI Python SDK
- Docling
- LangChain Text Splitters
- NumPy
- Pandas
- Requests
- Matplotlib
- Scikit-learn
- python-dotenv
- Virtual Environment (`venv`)
- Visual Studio Code

### APIs e modelos

A **GroqCloud API** foi utilizada nas atividades de geração de texto e Structured Outputs das Aulas 01 e 02.

Na Aula 03, o **OpenRouter** foi utilizado para acessar um modelo específico de embeddings. Essa escolha foi necessária porque a Groq não disponibilizava um endpoint próprio para geração de embeddings utilizado na atividade.

Na Aula 04, a conversão dos PDFs foi realizada localmente com o **Docling**, enquanto as estratégias de chunking foram implementadas com o pacote **LangChain Text Splitters**. A divisão dos documentos é uma operação local e não consome tokens de APIs de modelos de linguagem.

---

## 📁 Estrutura do repositório

```text
.
├── AULA_01/
│   └── README.md
├── AULA_02/
│   ├── README.md
│   ├── converter.py
│   ├── extrair_metadados.py
│   └── arquivos da atividade
├── AULA_03/
│   ├── README.md
│   └── atividade_embeddings.ipynb
├── AULA_04/
│   ├── README.md
│   ├── atividade_chunking.ipynb
│   ├── converter.py
│   ├── artigos em PDF
│   └── documentos em Markdown
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

Cada pasta possui seu próprio README com a descrição da atividade, conceitos estudados, instruções de configuração, decisões técnicas e resultados obtidos.

---

## ⚙️ Configuração geral

Clone o repositório e acesse sua pasta:

```bash
git clone https://github.com/fregulha/Residencia-Trilhas-em-Tecnologias-IA-Generativa-RAG.git
cd Residencia-Trilhas-em-Tecnologias-IA-Generativa-RAG
```

Crie um ambiente virtual Python.

No Windows:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

No Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

As configurações específicas de APIs, modelos e execução estão documentadas dentro da pasta de cada aula.

---

## 🔐 Segurança

As chaves de API são armazenadas localmente em arquivos `.env`, que não são versionados.

O `.gitignore` está configurado para ignorar arquivos de ambiente em qualquer pasta do repositório:

```gitignore
.env
.env.*
!.env.example
```

Os arquivos `.env.example` podem demonstrar quais variáveis são necessárias, mas nunca devem conter credenciais reais.

Nenhuma chave de API deve ser escrita diretamente no código, nos notebooks ou na documentação pública.

---

## 📖 Referências

- [LangChain — Text splitters](https://docs.langchain.com/oss/python/integrations/splitters)
- [Docling — documentação oficial](https://docling-project.github.io/docling/)
- [GroqCloud](https://console.groq.com/docs/overview)
- [OpenRouter](https://openrouter.ai/docs)
