# Residência - Trilhas em Tecnologias: IA Generativa & RAG

Repositório destinado ao registro das atividades desenvolvidas durante o programa de **Residência - Trilhas em Tecnologias: IA Generativa & RAG**, do Instituto ECOA - PUC-Rio.

**Aluna:** Fernanda Fregulha

---

## 📚 Aulas

* [Aula 01 - Introdução à IA](./AULA_01/README.md)
  Configuração do ambiente e primeira interação com um LLM por meio de API.

* [Aula 02 - Extração de Metadados com Structured Outputs](./AULA_02/README.md)
  Extração de metadados — título, autores e ano — de artigos científicos em Markdown, utilizando Structured Outputs.

* [Aula 03 - Embeddings e Busca Semântica Manual](./AULA_03/README.md)
  Implementação de distâncias entre embeddings, comparação semântica de termos e frases e busca por linha, parágrafo e capítulo.

---

## Tecnologias gerais

* Python
* Jupyter Notebook
* GroqCloud API
* OpenRouter Embeddings API
* OpenAI Python SDK
* NumPy
* Pandas
* Requests
* Matplotlib
* Scikit-learn
* python-dotenv
* Virtual Environment (`venv`)
* Visual Studio Code

A GroqCloud API foi utilizada nas atividades de geração de texto e Structured Outputs das Aulas 01 e 02.

Na Aula 03, o OpenRouter foi utilizado para acessar um modelo específico de embeddings e realizar comparações vetoriais e busca semântica.

---

## Estrutura do repositório

```text
.
├── AULA_01/
├── AULA_02/
├── AULA_03/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

Cada pasta de aula possui seu próprio README com a descrição da atividade, instruções de configuração, decisões técnicas e conceitos trabalhados.

---

## Configuração geral

Crie e ative um ambiente virtual Python.

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
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

As configurações específicas de API e execução estão documentadas dentro da pasta de cada aula.

---

## Segurança

As chaves de API são armazenadas localmente em arquivos `.env`, que não são versionados.

O `.gitignore` está configurado para ignorar arquivos de ambiente em qualquer pasta do repositório:

```gitignore
.env
.env.*
!.env.example
```

Os arquivos `.env.example` podem demonstrar quais variáveis são necessárias, mas nunca devem conter credenciais reais.

Nenhuma chave de API deve ser escrita diretamente no código, notebook ou documentação pública.
