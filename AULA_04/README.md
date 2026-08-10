# Aula 04 — Extração de PDF, Markdown e estratégias de chunking

## Objetivo

Esta atividade tem como objetivo converter documentos em PDF para Markdown, analisar como elementos como textos, títulos, tabelas, fórmulas e imagens foram preservados e comparar diferentes estratégias de divisão de texto (*chunking*) utilizando o LangChain.

O processo realizado foi:

1. Conversão dos artigos em PDF para Markdown com o Docling.
2. Análise da qualidade dos arquivos Markdown gerados.
3. Inclusão dos três documentos Markdown utilizados anteriormente na Aula 02.
4. Aplicação de dez estratégias de *chunking* sobre a base completa.
5. Comparação da quantidade e do tamanho dos chunks.
6. Identificação da estratégia mais adequada para utilização em um sistema RAG.

## Estrutura da base

A base final utilizada nos testes contém 12 documentos Markdown:

### Documentos da Aula 02

- `bioetica_e_ia.md`
- `escrita_academica_ia.md`
- `twitter_algoritmo.md`

### Artigos convertidos na Aula 04

- `attention_is_all_you_need.md`
- `bert_pretraining.md`
- `gpt3_language_models.md`
- `gpt4_technical_report.md`
- `instruct_gpt.md`
- `llama_foundation_models.md`
- `lora_low_rank_adaptation.md`
- `retrieval_augmented_generation.md`
- `scaling_laws_llm.md`

No total, a base possui:

| Métrica | Resultado |
|---|---:|
| Arquivos Markdown | 12 |
| Caracteres | 1.487.836 |
| Palavras | 210.096 |
| Títulos identificados | 708 |
| Tabelas Markdown identificadas | 151 |
| Marcadores de imagem | 171 |
| Imagens referenciadas | 0 |

## Conversão dos PDFs

Os nove artigos da Aula 04 foram convertidos com a biblioteca Docling. O script `converter.py` procura todos os arquivos `.pdf` na pasta `AULA_04`, converte cada documento e salva um arquivo `.md` com o mesmo nome.

Para executar a conversão a partir da raiz do repositório:

```powershell
python ".\AULA_04\converter.py"
```

Para conferir os arquivos gerados:

```powershell
Get-ChildItem ".\AULA_04\*.md"
```

### Resultado da extração

A conversão preservou grande parte do conteúdo textual e da estrutura dos documentos:

- Os títulos foram representados como headings Markdown.
- Diversas tabelas foram convertidas para a sintaxe de tabelas Markdown.
- A ordem de leitura e a organização dos textos foram preservadas na maior parte dos documentos.
- Algumas quebras, espaçamentos e artefatos do PDF podem permanecer no texto convertido.
- As imagens não foram exportadas como arquivos ou referências visuais.
- As posições das figuras foram representadas por marcadores `<!-- image -->`.

Foram encontrados 171 marcadores de imagem e nenhuma imagem referenciada. Portanto, informações existentes exclusivamente em gráficos, diagramas ou figuras podem não estar presentes no texto final.

A contagem automática de fórmulas procurou blocos delimitados por `$$` e não encontrou ocorrências. Esse resultado não permite concluir, isoladamente, que todas as fórmulas foram perdidas, pois elas podem ter sido representadas com outra sintaxe. Por isso, a qualidade das equações também deve ser verificada visualmente nos arquivos Markdown.

## Estratégias de chunking

Os testes foram implementados no notebook `atividade_chunking.ipynb` com os splitters do pacote `langchain-text-splitters`.

| Teste | Estratégia | Variável analisada |
|---:|---|---|
| 1 | Fixo, 200 caracteres, sem overlap | Tamanho extremo baixo |
| 2 | Fixo, 500 caracteres, sem overlap | Tamanho |
| 3 | Fixo, 1.000 caracteres, sem overlap | Tamanho |
| 4 | Fixo, 2.000 caracteres, sem overlap | Tamanho extremo alto |
| 5 | Fixo, 500 caracteres, overlap 50 | Overlap leve de 10% |
| 6 | Fixo, 500 caracteres, overlap 200 | Overlap elevado de 40% |
| 7 | Por parágrafo | Estrutura natural |
| 8 | Por sentença, agrupando três | Estrutura natural |
| 9 | Recursivo com separadores hierárquicos | Estratégia composta |
| 10 | Por seção ou heading Markdown | Estrutura semântica |

Nos testes 1 a 6 foi utilizado `CharacterTextSplitter`. O teste 9 utilizou `RecursiveCharacterTextSplitter`, enquanto o teste 10 utilizou `MarkdownHeaderTextSplitter`. Os testes por parágrafo e por grupo de três sentenças foram implementados como classes específicas baseadas em `TextSplitter`.

## Resultados

| Teste | Estratégia | Chunks | Menor | Maior | Média de caracteres |
|---:|---|---:|---:|---:|---:|
| 1 | Fixo, 200, sem overlap | 7.279 | 1 | 200 | 191,83 |
| 2 | Fixo, 500, sem overlap | 2.969 | 1 | 500 | 479,74 |
| 3 | Fixo, 1.000, sem overlap | 1.493 | 9 | 1.000 | 971,52 |
| 4 | Fixo, 2.000, sem overlap | 749 | 9 | 2.000 | 1.960,98 |
| 5 | Fixo, 500, overlap 50 | 3.299 | 1 | 500 | 479,85 |
| 6 | Fixo, 500, overlap 200 | 4.943 | 1 | 500 | 479,84 |
| 7 | Por parágrafo | 4.025 | 1 | 40.445 | 367,65 |
| 8 | Três sentenças | 4.115 | 5 | 17.262 | 315,75 |
| 9 | Recursivo | 4.363 | 1 | 500 | 330,86 |
| 10 | Por heading Markdown | 707 | 9 | 52.364 | 2.107,12 |

Todos os testes geraram chunks. Nos testes que possuem limite configurado — 1, 2, 3, 4, 5, 6 e 9 — nenhum chunk ultrapassou o tamanho determinado.

## Análise das estratégias

### Tamanhos fixos

Os testes com tamanhos fixos são simples e previsíveis, mas podem cortar palavras, sentenças ou ideias no meio. O teste de 200 caracteres apresentou a maior fragmentação, enquanto o teste de 2.000 caracteres preservou mais contexto, mas pode misturar diferentes assuntos no mesmo trecho.

### Overlap

O overlap ajuda a preservar informações localizadas nas fronteiras dos chunks. O overlap de 50 caracteres aumentou moderadamente a quantidade de trechos. Já o overlap de 200 caracteres gerou maior redundância e, consequentemente, maior volume de dados para processamento e armazenamento.

### Parágrafos e sentenças

As estratégias por parágrafo e por sentenças preservam estruturas naturais do texto. Entretanto, os resultados apresentaram tamanhos muito variáveis. O maior chunk por parágrafo chegou a 40.445 caracteres e o maior grupo de sentenças chegou a 17.262 caracteres, o que pode ser inadequado para recuperação semântica e envio a modelos com limites menores de contexto.

### Headings Markdown

A divisão por headings apresentou a menor quantidade de chunks e preservou a estrutura semântica das seções. Contudo, algumas seções ficaram extensas demais, com um chunk máximo de 52.364 caracteres. Dessa forma, essa estratégia não é suficiente sozinha quando os documentos possuem seções longas.

### Separação recursiva

O splitter recursivo procura separar primeiro por estruturas maiores, como parágrafos e linhas. Quando necessário, utiliza sentenças, espaços e, por último, caracteres. Isso oferece um equilíbrio entre respeito à estrutura textual e controle de tamanho.

## Melhor estratégia

Entre os dez testes realizados, o **Teste 9 — `RecursiveCharacterTextSplitter`** apresentou o melhor equilíbrio geral para esta base.

Essa estratégia:

- respeitou o limite de 500 caracteres;
- gerou chunks com média de aproximadamente 331 caracteres;
- evitou os trechos excessivamente grandes encontrados nos testes por parágrafo, sentenças e headings;
- preservou melhor as separações naturais do texto do que os cortes fixos;
- apresentou características adequadas para uma etapa posterior de embeddings e recuperação semântica em RAG.

Em uma implementação real, uma alternativa ainda mais completa seria combinar as estratégias 10 e 9: primeiro separar os documentos por headings Markdown e, em seguida, aplicar o splitter recursivo dentro das seções que ultrapassarem o limite desejado.

## Como executar o notebook

1. Ative o ambiente virtual do projeto.
2. Abra `AULA_04/atividade_chunking.ipynb` no VS Code ou Jupyter.
3. Selecione o kernel correspondente ao ambiente virtual.
4. Reinicie o kernel para evitar variáveis de execuções anteriores.
5. Execute todas as células com **Run All**.
6. Confirme que foram carregados 12 documentos.
7. Confira as tabelas, exemplos de chunks, gráfico comparativo e validação final.

Resultado esperado ao final:

```text
Validação concluída: os 10 testes geraram chunks.
```

## Tecnologias utilizadas

- Python
- Jupyter Notebook
- Docling
- LangChain Text Splitters
- Pandas
- Matplotlib
- Expressões regulares

## Referências

- [LangChain — Text splitters](https://docs.langchain.com/oss/python/integrations/splitters)
- [Docling — documentação oficial](https://docling-project.github.io/docling/)
