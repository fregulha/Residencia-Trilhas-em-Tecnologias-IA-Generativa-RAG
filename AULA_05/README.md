# Aula 05 — Documents, metadados e preparação para busca vetorial

## Objetivo

Esta atividade apresenta o formato padrão `Document` do LangChain e migra a representação manual de chunks da Aula 04 para objetos com:

```python
Document(
    page_content="Texto do chunk",
    metadata={"fonte": "arquivo.md", "chunk_index": 1}
)
```

O embedding não é armazenado no `Document`. Ele será calculado e administrado pela vector store na etapa de indexação.

## Exercícios implementados

### Exercício 1 — Documents criados manualmente

- seis objetos `Document` sobre embeddings, chunking, RAG e tokenização;
- impressão de `page_content` e `metadata`;
- resultado de `len(documentos)`;
- teste com lista, dicionário aninhado, números, booleano e `None` nos metadados;
- teste de um documento sem `metadata` explícito;
- respostas conceituais no próprio notebook.

### Exercício 2 — Schema de metadados

O schema possui os sete campos obrigatórios e sete campos próprios:

| Categoria | Campos |
|---|---|
| Obrigatórios | `fonte`, `documento_id`, `chunk_index`, `estrategia`, `chunk_size`, `chunk_overlap`, `n_caracteres` |
| Próprios | `chunk_id`, `secao`, `pagina`, `n_tokens_estimados`, `caminho_origem`, `idioma`, `tem_tabela` |

O notebook documenta o tipo e a finalidade de cada campo, justifica os campos próprios e converte um chunk real da Aula 04 em `Document`.

### Exercício 3 — Busca vetorial com filtros

- `InMemoryVectorStore` do LangChain;
- amostra estratificada de até 15 chunks por documento;
- 12 fontes representadas;
- busca sem filtro;
- filtro por idioma;
- filtro por `documento_id`;
- `k=3` para limitar o contexto recuperado;
- exibição de score, fonte, `chunk_id`, caminho e trecho;
- resultados exportados em `results/buscas_exemplo.json`.

A amostragem e a store em memória reduzem processamento e armazenamento. Todos os embeddings são locais e o cache existente é reutilizado.

## Estrutura

```text
AULA_05/
├── README.md
├── atividade_documents_metadados.ipynb
└── results/
    └── buscas_exemplo.json
```

Os dados da Aula 04 são lidos diretamente de:

```text
AULA_04/results/bioetica_e_ia/test_10/chunks_embeddings.json
```

Nenhuma cópia adicional dos embeddings é criada. O exemplo utiliza `page_content` e metadados, respeitando a responsabilidade da vector store.

## Modelo local

O modelo configurado é:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Ele é carregado com `HuggingFaceEmbeddings`, produz vetores normalizados de 384 dimensões e reutiliza o cache local da Aula 04.

## Como executar

Na raiz do repositório:

```powershell
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Abra `AULA_05/atividade_documents_metadados.ipynb`, selecione o ambiente virtual como kernel e execute **Run All**.

## Dependências principais

- `langchain-core`
- `langchain-text-splitters`
- `langchain-huggingface`
- `sentence-transformers`
- `torch`
- `transformers`

## Referências

- [LangChain — Hugging Face embeddings](https://docs.langchain.com/oss/python/integrations/embeddings/huggingfacehub)
- [Hugging Face — Getting Started With Embeddings](https://huggingface.co/blog/getting-started-with-embeddings)
