# Residência — Trilhas em Tecnologias: IA Generativa & RAG

Repositório das atividades desenvolvidas no programa de **Residência — Trilhas em Tecnologias: IA Generativa & RAG**, do Instituto ECOA — PUC-Rio.

**Aluna:** Fernanda Fregulha

## Aulas

- [Aula 01 — Introdução à IA](./AULA_01/README.md): configuração do ambiente e primeira interação com um modelo de linguagem por API.
- [Aula 02 — Extração de metadados](./AULA_02/README.md): conversão de PDF para Markdown e extração estruturada de título, autores e ano.
- [Aula 03 — Embeddings e busca semântica](./AULA_03/README.md): métricas de distância, comparação semântica e recuperação por linha, parágrafo e capítulo.
- [Aula 04 — Estratégias de chunking para RAG](./AULA_04/README.md): conversão de 12 documentos, comparação de dez estratégias, embeddings locais e seleção experimental do melhor método.
- [Aula 05 — Documents, metadados e busca vetorial](./AULA_05/README.md): criação de objetos `Document`, schema de metadados, vector store local e buscas semânticas com filtros.

## Destaque da Aula 04

A Aula 04 implementa o pipeline:

```text
PDF → Markdown → Chunking → Embeddings → JSON
```

Os dez testes de chunking foram comparados em três documentos. O método vencedor, `recursive_1000_overlap_100`, foi aplicado aos outros nove para economizar tokens e concluir o processamento sem exceder o limite encontrado na tentativa anterior.

Resultado final:

- 12 documentos processados;
- 5.026 chunks com embeddings;
- vetores locais de 384 dimensões;
- nenhuma chamada paga para gerar os embeddings finais;
- relatório com as 15 questões obrigatórias;
- resultados organizados por documento e teste.

Consulte a [documentação completa da Aula 04](./AULA_04/README.md) e o [relatório experimental](./AULA_04/results/RELATORIO.md).

## Conceitos trabalhados

- consumo de modelos de linguagem por API;
- prompting e Structured Outputs;
- extração de metadados;
- conversão de PDF para Markdown;
- embeddings e similaridade de cosseno;
- busca semântica;
- chunk size e chunk overlap;
- divisão por caracteres, parágrafos, sentenças e headings;
- separação recursiva;
- preparação de documentos para RAG;
- exportação de dados estruturados em JSON.

## Tecnologias

- Python
- Jupyter Notebook
- Visual Studio Code
- GroqCloud e OpenRouter
- OpenAI Python SDK
- Docling
- LangChain Text Splitters
- Hugging Face Transformers
- PyTorch
- NumPy, Pandas, Matplotlib e Scikit-learn
- python-dotenv

Na Aula 04, o chunking e os embeddings finais são executados localmente. O modelo `sentence-transformers/all-MiniLM-L6-v2` é armazenado em cache dentro da pasta da aula e não consome créditos do OpenRouter.

## Estrutura do repositório

```text
.
├── AULA_01/
│   └── README.md
├── AULA_02/
│   ├── README.md
│   ├── converter.py
│   └── extrair_metadados.py
├── AULA_03/
│   ├── README.md
│   └── atividade_embeddings.ipynb
├── AULA_04/
│   ├── README.md
│   ├── converter.py
│   ├── atividade_chunking.ipynb
│   ├── documentos PDF e Markdown
│   └── results/
│       ├── RELATORIO.md
│       ├── summary.json
│       └── resultados por documento e teste
├── AULA_05/
│   ├── README.md
│   ├── atividade_documents_metadados.ipynb
│   └── results/
│       └── buscas_exemplo.json
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Configuração

Clone o repositório:

```bash
git clone https://github.com/fregulha/Residencia-Trilhas-em-Tecnologias-IA-Generativa-RAG.git
cd Residencia-Trilhas-em-Tecnologias-IA-Generativa-RAG
```

Crie o ambiente virtual e instale as dependências.

Windows:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux ou macOS:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Para sair do ambiente virtual, em qualquer sistema operacional, execute:

```bash
deactivate
```

Cada pasta possui instruções específicas de execução em seu próprio README.

## Segurança

Chaves de API são armazenadas somente em arquivos `.env`, ignorados pelo Git. Nunca publique credenciais em notebooks, código ou documentação.

O cache local do modelo da Aula 04 (`AULA_04/.hf_cache`) também é ignorado, pois pode ser baixado novamente quando necessário.

## Referências

- [LangChain — Text splitters](https://docs.langchain.com/oss/python/integrations/splitters)
- [Hugging Face — embeddings](https://huggingface.co/blog/getting-started-with-embeddings)
- [Docling — documentação oficial](https://docling-project.github.io/docling/)
- [GroqCloud](https://console.groq.com/docs/overview)
- [OpenRouter](https://openrouter.ai/docs)
