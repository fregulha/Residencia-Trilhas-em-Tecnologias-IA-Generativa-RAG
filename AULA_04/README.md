# Aula 04 — Avaliação de estratégias de chunking para RAG

## Objetivo

Esta atividade implementa um pipeline para converter documentos PDF em Markdown, comparar dez estratégias de *chunking*, gerar embeddings para cada chunk e exportar os resultados em JSON. A análise considera quantidade e tamanho dos chunks, preservação de contexto e estrutura, tabelas, imagens e consistência vetorial.

```text
PDF → Markdown → Chunking → Embeddings → JSON
```

## Base documental

A base contém 12 documentos Markdown:

- três documentos das aulas anteriores: `bioetica_e_ia.md`, `escrita_academica_ia.md` e `twitter_algoritmo.md`;
- nove artigos da Aula 04: *Attention Is All You Need*, BERT, GPT-3, GPT-4, InstructGPT, LLaMA, LoRA, RAG e Scaling Laws.

Os nove PDFs da Aula 04 foram convertidos automaticamente com Docling pelo script `converter.py`. A extração preservou boa parte dos textos, headings e tabelas, mas não produziu referências Markdown para imagens. Informações exclusivamente visuais podem ter sido perdidas.

## Metodologia e economia de tokens

Os dez testes foram executados nos três primeiros documentos:

- `bioetica_e_ia.md`;
- `escrita_academica_ia.md`;
- `twitter_algoritmo.md`.

Depois da comparação, a melhor estratégia foi aplicada aos outros nove documentos, completando o processamento dos 12 arquivos.

Essa abordagem foi adotada para economizar tokens, chamadas e tempo de processamento. Uma tentativa anterior de executar os dez testes em todos os documentos excedeu o limite de tokens antes de finalizar. Para manter a comparação válida, os dez testes usaram os mesmos três documentos e o mesmo modelo de embedding.

## Estratégias avaliadas

| Teste | Estratégia | Configuração |
|---:|---|---|
| 1 | Fixo | 200 caracteres, sem overlap |
| 2 | Fixo | 500 caracteres, sem overlap |
| 3 | Fixo | 1.000 caracteres, sem overlap |
| 4 | Fixo | 2.000 caracteres, sem overlap |
| 5 | Fixo com overlap | 500 caracteres, overlap 50 |
| 6 | Fixo com overlap | 500 caracteres, overlap 200 |
| 7 | Parágrafo | Um parágrafo por chunk |
| 8 | Sentenças | Três sentenças por chunk |
| 9 | Recursive | 1.000 caracteres, overlap 100 |
| 10 | Markdown | Separação por headings e seções |

Os testes utilizam `CharacterTextSplitter`, `RecursiveCharacterTextSplitter` e `MarkdownHeaderTextSplitter`, do pacote `langchain-text-splitters`.

## Resultados dos dez testes

As estatísticas abaixo correspondem aos três documentos usados na comparação.

| Teste | Estratégia | Chunks | Média | Mínimo | Máximo |
|---:|---|---:|---:|---:|---:|
| 1 | Fixo 200 | 742 | 198,4 | 13 | 200 |
| 2 | Fixo 500 | 298 | 494,6 | 63 | 500 |
| 3 | Fixo 1.000 | 150 | 984,6 | 213 | 1.000 |
| 4 | Fixo 2.000 | 76 | 1.951,3 | 440 | 2.000 |
| 5 | Fixo 500, overlap 50 | 330 | 496,3 | 156 | 500 |
| 6 | Fixo 500, overlap 200 | 494 | 497,0 | 156 | 500 |
| 7 | Parágrafo | 447 | 329,9 | 1 | 4.291 |
| 8 | Três sentenças | 378 | 389,6 | 5 | 1.668 |
| 9 | Recursive 1.000/100 | 211 | 708,8 | 65 | 996 |
| 10 | Markdown | 67 | 2.217,2 | 10 | 9.877 |

O teste fixo de 200 caracteres gerou mais chunks e apresentou maior fragmentação. O Markdown gerou menos chunks e preservou headings, mas criou seções muito extensas. O teste por parágrafo também apresentou unidades grandes e irregulares.

## Estratégia escolhida

O **Teste 9 — `recursive_1000_overlap_100`** apresentou o melhor equilíbrio para RAG porque:

- prioriza parágrafos, linhas, sentenças e palavras antes de cortar por caracteres;
- mantém o tamanho máximo abaixo de 1.000 caracteres;
- usa overlap moderado de 10%;
- reduz cortes abruptos sem a redundância do overlap de 40%;
- oferece chunks mais regulares do que parágrafo ou Markdown puros;
- apresentou consistência adequada entre embeddings adjacentes.

Uma evolução recomendada é uma estratégia híbrida: Markdown para preservar headings e Recursive para subdividir seções extensas.

## Embeddings

Todos os chunks receberam embeddings do modelo local:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Cada vetor possui 384 dimensões e é normalizado. O modelo é executado localmente com Transformers e PyTorch, evitando consumo de créditos do OpenRouter.

Resultados finais:

| Métrica | Resultado |
|---|---:|
| Documentos processados | 12 |
| Documentos com os 10 testes | 3 |
| Documentos com o método vencedor | 9 |
| Chunks com embeddings | 5.026 |
| Embeddings ausentes ou inválidos | 0 |
| Dimensão dos embeddings | 384 |

## Estrutura dos resultados

```text
results/
├── RELATORIO.md
├── summary.json
├── bioetica_e_ia/
│   ├── markdown/bioetica_e_ia.md
│   ├── test_01/chunks_embeddings.json
│   ├── ...
│   └── test_10/chunks_embeddings.json
├── escrita_academica_ia/
├── twitter_algoritmo/
└── demais_documentos/
    ├── markdown/documento.md
    └── test_09/chunks_embeddings.json
```

Os três documentos de avaliação possuem resultados dos testes 1–10. Os outros nove possuem o teste 9, escolhido na etapa comparativa.

- [Relatório completo](./results/RELATORIO.md)
- [Resumo estruturado](./results/summary.json)
- [Notebook executado](./atividade_chunking.ipynb)

## Como executar

Na raiz do repositório, crie e ative o ambiente virtual:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Converta os PDFs, caso seja necessário recriar os Markdown:

```powershell
python .\AULA_04\converter.py
```

Depois abra `AULA_04/atividade_chunking.ipynb`, selecione o ambiente virtual como kernel e execute **Run All**. Na primeira execução, o modelo de embeddings será baixado para `AULA_04/.hf_cache`; nas seguintes, será reutilizado localmente.

> Os arquivos de resultados já estão gerados. Não é necessário executar novamente para apenas revisar ou entregar a atividade.

## Entregáveis

- `converter.py`: conversão automática PDF → Markdown;
- `atividade_chunking.ipynb`: chunking, embeddings, estatísticas, exportação e análise;
- `results/*/markdown`: Markdown intermediário de cada documento;
- `results/*/test_*/chunks_embeddings.json`: chunks, embeddings e metadados;
- `results/summary.json`: configurações, ranking e validações vetoriais;
- `results/RELATORIO.md`: respostas às 15 perguntas e conclusão experimental.

## Tecnologias

- Python e Jupyter Notebook
- Docling
- LangChain Text Splitters
- Hugging Face Transformers
- PyTorch
- NumPy e Pandas

## Referências

- [LangChain — Text splitters](https://docs.langchain.com/oss/python/integrations/splitters)
- [Hugging Face — Getting Started With Embeddings](https://huggingface.co/blog/getting-started-with-embeddings)
- [Docling — documentação oficial](https://docling-project.github.io/docling/)
