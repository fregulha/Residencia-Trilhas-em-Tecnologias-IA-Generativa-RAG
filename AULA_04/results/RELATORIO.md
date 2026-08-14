# Relatório — avaliação de estratégias de chunking

## Metodologia e economia de tokens

Os 10 testes foram executados em `bioetica_e_ia.md`, `escrita_academica_ia.md` e `twitter_algoritmo.md`. O teste vencedor foi aplicado aos outros nove documentos, totalizando 12 Markdown processados. A autora confirmou que os nove PDFs locais correspondem aos arquivos do Google Drive.

Essa abordagem foi adotada porque uma tentativa anterior de repetir os dez testes em todos os documentos excedeu o limite de tokens antes da conclusão. Para economizar tokens e viabilizar a atividade, todas as estratégias foram comparadas sobre a mesma amostra e com o mesmo modelo `sentence-transformers/all-MiniLM-L6-v2`. Os embeddings finais foram produzidos localmente, sem chamadas ao OpenRouter.

## Configurações e estatísticas

| Teste | Estratégia | Configuração | Chunks | Média | Mínimo | Máximo | Cosseno adjacente |
|---:|---|---|---:|---:|---:|---:|---:|
| 1 | fixed_200 | 200, overlap 0 | 742 | 198.4 | 13 | 200 | 0.466 |
| 2 | fixed_500 | 500, overlap 0 | 298 | 494.6 | 63 | 500 | 0.569 |
| 3 | fixed_1000 | 1000, overlap 0 | 150 | 984.6 | 213 | 1000 | 0.682 |
| 4 | fixed_2000 | 2000, overlap 0 | 76 | 1951.3 | 440 | 2000 | 0.786 |
| 5 | fixed_500_overlap_50 | 500, overlap 50 | 330 | 496.3 | 156 | 500 | 0.620 |
| 6 | fixed_500_overlap_200 | 500, overlap 200 | 494 | 497.0 | 156 | 500 | 0.730 |
| 7 | paragraph | paragraph | 447 | 329.9 | 1 | 4291 | 0.404 |
| 8 | three_sentences | three_sentences | 378 | 389.6 | 5 | 1668 | 0.473 |
| 9 | recursive_1000_overlap_100 | 1000, overlap 100 | 211 | 708.8 | 65 | 996 | 0.604 |
| 10 | markdown_headers | markdown_headers | 67 | 2217.2 | 10 | 9877 | 0.570 |

Foram identificadas 144 tabelas Markdown, 0 referências de imagem e 171 marcadores `<!-- image -->`. A similaridade cosseno adjacente é apenas uma verificação complementar: overlap tende a aumentar essa medida e, por isso, ela não foi usada isoladamente.

## Exemplos de chunks

- **Teste 1 — fixed_200:** “273 <!-- image --> ## Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial Juracy Barbosa dos Santos 1 , Guilhermina Rego 1 , Rui Nunes 1 1. Faculdade de Medic…”
- **Teste 2 — fixed_500:** “273 <!-- image --> ## Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial Juracy Barbosa dos Santos 1 , Guilhermina Rego 1 , Rui Nunes 1 1. Faculdade de Medicina da Universidade do Porto, Porto, Portugal. ## Resumo O avanço da inteligência artificial tem transfo…”
- **Teste 3 — fixed_1000:** “273 <!-- image --> ## Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial Juracy Barbosa dos Santos 1 , Guilhermina Rego 1 , Rui Nunes 1 1. Faculdade de Medicina da Universidade do Porto, Porto, Portugal. ## Resumo O avanço da inteligência artificial tem transfo…”
- **Teste 4 — fixed_2000:** “273 <!-- image --> ## Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial Juracy Barbosa dos Santos 1 , Guilhermina Rego 1 , Rui Nunes 1 1. Faculdade de Medicina da Universidade do Porto, Porto, Portugal. ## Resumo O avanço da inteligência artificial tem transfo…”
- **Teste 5 — fixed_500_overlap_50:** “273 <!-- image --> ## Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial Juracy Barbosa dos Santos 1 , Guilhermina Rego 1 , Rui Nunes 1 1. Faculdade de Medicina da Universidade do Porto, Porto, Portugal. ## Resumo O avanço da inteligência artificial tem transfo…”
- **Teste 6 — fixed_500_overlap_200:** “273 <!-- image --> ## Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial Juracy Barbosa dos Santos 1 , Guilhermina Rego 1 , Rui Nunes 1 1. Faculdade de Medicina da Universidade do Porto, Porto, Portugal. ## Resumo O avanço da inteligência artificial tem transfo…”
- **Teste 7 — paragraph:** “273…”
- **Teste 8 — three_sentences:** “273 <!-- image --> ## Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial Juracy Barbosa dos Santos 1 , Guilhermina Rego 1 , Rui Nunes 1 1. Faculdade de Medicina da Universidade do Porto, Porto, Portugal. ## Resumo O avanço da inteligência artificial tem transfo…”
- **Teste 9 — recursive_1000_overlap_100:** “273 <!-- image --> ## Entre o algoritmo e o Juramento de Hipócrates: bioética na era da inteligência artificial Juracy Barbosa dos Santos 1 , Guilhermina Rego 1 , Rui Nunes 1 1. Faculdade de Medicina da Universidade do Porto, Porto, Portugal. ## Resumo…”
- **Teste 10 — markdown_headers:** “273 <!-- image -->…”

## Análise obrigatória

### 1. Qual estratégia gerou mais chunks?

O teste 1, `fixed_200`, gerou 742 chunks. O tamanho reduzido aumenta fragmentação, armazenamento e quantidade de vetores.

### 2. Qual gerou menos chunks?

O teste 10, `markdown_headers`, gerou 67 chunks. A baixa quantidade não significa maior qualidade, pois seções extensas podem concentrar assuntos diferentes.

### 3. Como o tamanho dos chunks variou?

Os testes fixos ficaram próximos de 200, 500, 1.000 e 2.000 caracteres. Parágrafos e sentenças variaram naturalmente. Recursive teve média de 708.8 e máximo de 996; Markdown chegou a 9877 caracteres.

### 4. Qual estratégia preservou melhor a estrutura?

Markdown preservou melhor headings e seções nos metadados. Recursive apresentou o melhor equilíbrio prático entre estrutura natural e tamanho controlado.

### 5. Como tabelas foram tratadas?

As tabelas simples foram mantidas como sintaxe Markdown. Cortes fixos podem dividir linhas e conceitos; Markdown e Recursive tendem a respeitar melhor os blocos, embora uma tabela maior que o limite ainda possa ser dividida. A conversão não garante preservação de células mescladas e layouts complexos.

### 6. Como imagens foram tratadas?

Foram contabilizadas referências Markdown e marcadores `<!-- image -->`. Quando existe apenas o marcador, a posição aproximada é preservada, mas os pixels e o significado visual não entram no embedding. Imagens não foram armazenadas separadamente por este pipeline.

### 7. Quais informações foram perdidas em PDF → Markdown?

Podem ter sido perdidos layout, colunas, posição exata, cores, células mescladas, fórmulas complexas, gráficos e relações entre figura e legenda. Não foi preservado um mapeamento confiável de página por chunk.

### 8. O corte por caracteres fragmentou conceitos?

Sim, especialmente com 200 caracteres. Ele pode interromper frases, referências e tabelas. Tamanhos maiores reduzem, mas não eliminam o problema; overlap recupera contexto ao custo de duplicação.

### 9. Parágrafos produziram chunks grandes?

Sim. O maior chunk do teste 7 teve 4291 caracteres. A estratégia respeita a unidade natural, mas produz tamanhos irregulares.

### 10. Três sentenças preservaram melhor o contexto?

Preservaram melhor fronteiras linguísticas do que cortes fixos pequenos, mas três sentenças podem separar uma explicação longa ou juntar assuntos diferentes.

### 11. Recursive apresentou vantagens?

Sim. Ele tenta parágrafos, linhas, sentenças, espaços e caracteres, mantendo o máximo abaixo de 1.000 e overlap moderado de 10%.

### 12. Markdown preservou a estrutura semântica?

Sim. Os headings aparecem nos metadados, mas algumas seções ficaram extensas. Uma abordagem híbrida Markdown + Recursive seria mais segura.

### 13. Qual estratégia é mais adequada para RAG?

O teste 9, `recursive_1000_overlap_100`, foi o mais adequado por equilibrar tamanho, contexto, hierarquia natural, overlap e consistência vetorial. A escolha não se baseou apenas no número de chunks.

### 14. Quais estratégias devem ser descartadas?

Como padrão, devem ser evitados 200 caracteres, 2.000 caracteres e overlap de 40%. Parágrafo puro e Markdown puro também exigem subdivisão quando geram unidades excessivas.

### 15. Quais estratégias usar nos próximos experimentos?

Recursive 1.000/100 e uma abordagem híbrida Markdown + Recursive. Uma avaliação futura deve usar perguntas reais e métricas como Recall@k ou MRR.

## Conclusão

O Recursive 1.000/100 produziu a melhor representação operacional para RAG nesta base. Todos os chunks receberam embeddings normalizados de 384 dimensões. Chunks maiores que o contexto do modelo foram processados em janelas e agregados, evitando descartar o final do texto. A conclusão ainda é exploratória porque não existe um conjunto rotulado de perguntas e respostas.
