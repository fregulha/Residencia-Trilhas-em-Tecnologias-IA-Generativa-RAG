# Aula 03 - Embeddings e Busca Semântica Manual

Atividade de **07/08** da Residência - Trilhas em Tecnologias: IA Generativa & RAG.

**Aluna:** Fernanda Fregulha

## Sobre a atividade

Nesta atividade, foram estudados embeddings, métricas de distância entre vetores e busca semântica.

A implementação calcula manualmente a Distância Euclidiana, a Similaridade de Cosseno e a Distância de Cosseno. Em seguida, essas métricas são utilizadas para comparar palavras, frases e trechos dos documentos Markdown produzidos na Aula 02.

A busca semântica foi realizada com três estratégias de divisão dos documentos:

* linha por linha;
* parágrafos;
* capítulos identificados pelos títulos Markdown.

Em cada estratégia, o embedding da pergunta é comparado com o embedding de cada trecho. Os resultados são ordenados pela Similaridade de Cosseno, retornando os três trechos com maior score.

## Tecnologias utilizadas

* Python
* Jupyter Notebook
* NumPy
* Pandas
* Requests
* Matplotlib
* Scikit-learn
* python-dotenv
* OpenRouter Embeddings API
* Visual Studio Code

Modelo de embedding utilizado:

```text
nvidia/nemotron-3-embed-1b:free
```

## Por que o OpenRouter foi utilizado em vez da Groq?

Nas Aulas 01 e 02, foi utilizada a GroqCloud API para tarefas de geração de texto e extração estruturada de informações com LLMs.

A Aula 03, entretanto, exige a geração de embeddings: vetores numéricos que representam o significado semântico de palavras, frases e documentos.

No momento da realização desta atividade, a API oficial da Groq não disponibilizava um endpoint específico para geração de embeddings. A chave `GROQ_API_KEY` utilizada nas aulas anteriores autentica somente requisições enviadas à infraestrutura da Groq e não pode ser utilizada diretamente no OpenRouter.

O OpenRouter foi escolhido porque disponibiliza o endpoint:

```text
POST https://openrouter.ai/api/v1/embeddings
```

Além disso, oferece acesso ao modelo gratuito:

```text
nvidia/nemotron-3-embed-1b:free
```

Esse modelo é próprio para geração de embeddings e pode ser utilizado em tarefas de busca semântica e RAG.

Dessa forma, cada aula mantém sua configuração independente:

* Aulas 01 e 02: `GROQ_API_KEY`, utilizada para geração de texto e Structured Outputs;
* Aula 03: `OPENROUTER_API_KEY`, utilizada para geração de embeddings.

Os arquivos `.env` das aulas anteriores foram preservados e continuam utilizando a Groq normalmente.

Documentações consultadas:

* [Groq API Reference](https://console.groq.com/docs/api-reference)
* [OpenRouter Embeddings API](https://openrouter.ai/docs/api_reference/embeddings)
* [OpenRouter Free Models](https://openrouter.ai/collections/free-models)

## Estrutura da Aula 03

```text
AULA_03/
├── atividade_embeddings.ipynb
└── README.md
```

O arquivo `.env` é utilizado apenas localmente para armazenar a chave da API e não deve ser enviado ao GitHub.

## Configuração

As dependências do projeto podem ser instaladas a partir da raiz do repositório:

```bash
pip install -r requirements.txt
```

Dentro da pasta `AULA_03`, crie um arquivo `.env`:

```env
OPENROUTER_API_KEY=sua_chave_do_openrouter
EMBEDDING_MODEL=nvidia/nemotron-3-embed-1b:free
```

Uma chave pode ser criada em:

[OpenRouter - API Keys](https://openrouter.ai/settings/keys)

## Executando a atividade

Abra o arquivo `atividade_embeddings.ipynb` no Visual Studio Code e selecione o ambiente virtual do projeto como kernel Python.

Execute as células em ordem, utilizando `Shift + Enter`, ou selecione `Run All` para executar todo o notebook.

## Distância Euclidiana

A Distância Euclidiana representa a distância em linha reta entre dois vetores.

A função implementada aceita vetores de qualquer dimensão, desde que possuam o mesmo tamanho:

```python
def distancia_euclidiana(embedding_a, embedding_b):
    vetor_a, vetor_b = validar_embeddings(
        embedding_a,
        embedding_b
    )

    diferencas = vetor_a - vetor_b
    soma_dos_quadrados = np.sum(diferencas ** 2)

    return float(np.sqrt(soma_dos_quadrados))
```

Quanto menor a distância, mais próximos estão os vetores.

## Similaridade e Distância de Cosseno

A Similaridade de Cosseno compara a direção de dois vetores.

Valores próximos de `1` indicam maior similaridade. A Distância de Cosseno é calculada como:

```text
Distância de Cosseno = 1 - Similaridade de Cosseno
```

Consequentemente, quanto menor a Distância de Cosseno, maior a similaridade entre os embeddings.

## Testes com vetores

As funções foram inicialmente testadas com os seguintes vetores:

```python
embedding_a = [1, 0, 0]
embedding_b = [0, 1, 0]
embedding_c = [1, 0, 0]
```

Foram realizadas as comparações:

* `embedding_a` com `embedding_b`;
* `embedding_a` com `embedding_c`;
* `embedding_b` com `embedding_c`.

Os vetores `embedding_a` e `embedding_c` são idênticos e, portanto, possuem distância zero. Já `embedding_a` e `embedding_b` são ortogonais, apresentando Similaridade de Cosseno igual a zero.

## Comparação de termos

Foram gerados embeddings para os termos:

```text
gato, felino, cachorro, carro, caminhão, moto, banana, maçã e goiaba
```

Todos os pares foram comparados utilizando:

* Distância Euclidiana;
* Similaridade de Cosseno;
* Distância de Cosseno.

Como etapa adicional, foi utilizada a técnica MDS — Multidimensional Scaling — para projetar os embeddings em duas dimensões e visualizar a proximidade entre os termos.

A posição exata dos pontos no gráfico não representa uma dimensão semântica específica. O objetivo é observar as distâncias relativas entre os termos.

## Comparação de frases

Uma frase sobre um cachorro brincando no parque foi utilizada como âncora e comparada com:

* uma paráfrase;
* uma frase relacionada ao contexto de animais;
* uma frase de outro domínio;
* uma frase com negação.

A paráfrase apresentou a maior similaridade, enquanto a frase relacionada à economia apresentou a menor.

A frase com negação permaneceu semanticamente próxima da âncora por compartilhar termos e contexto semelhantes. Isso demonstra que embeddings capturam bem o assunto geral, mas podem apresentar limitações na interpretação de oposição e negação.

## Busca semântica manual

Os documentos Markdown da Aula 02 foram carregados e divididos em diferentes tamanhos de trechos.

Para cada estratégia:

1. os trechos foram extraídos dos documentos;
2. um embedding foi gerado para cada trecho;
3. um embedding foi gerado para a pergunta;
4. a Similaridade de Cosseno foi calculada manualmente entre a pergunta e cada trecho;
5. os resultados foram ordenados pelo score;
6. os três trechos mais relevantes foram retornados.

Pergunta utilizada no teste:

```text
O que é autonomia e opacidade algorítmica?
```

Embora os embeddings tenham sido gerados em lotes para reduzir a quantidade de requisições à API, cada trecho recebeu seu próprio vetor e foi comparado individualmente com a pergunta. Não foram utilizados bancos vetoriais ou bibliotecas prontas de busca semântica.

## Estratégias de divisão

### Linhas

A divisão por linhas produz trechos pequenos e específicos. Ela pode localizar frases diretamente relacionadas à pergunta, mas oferece pouco contexto ao redor do resultado.

### Parágrafos

Os parágrafos preservam mais contexto e geralmente proporcionam um equilíbrio entre precisão e quantidade de informação recuperada.

### Capítulos

Os capítulos oferecem respostas mais completas, porém o conteúdo adicional pode diminuir a concentração semântica do assunto procurado.

A escolha do tamanho dos trechos é uma decisão importante em sistemas RAG e influencia diretamente a qualidade da recuperação.

## Segurança

A chave do OpenRouter permanece armazenada somente no arquivo `.env`.

O `.gitignore` impede que arquivos `.env` sejam enviados ao repositório:

```gitignore
.env
.env.*
```

Chaves de API nunca devem ser escritas diretamente no notebook ou publicadas no GitHub.

## Conceitos trabalhados

* embeddings;
* representação vetorial de textos;
* Distância Euclidiana;
* Similaridade de Cosseno;
* Distância de Cosseno;
* busca semântica;
* ranking por similaridade;
* divisão de documentos em chunks;
* processamento em lotes;
* visualização MDS;
* fundamentos de recuperação para sistemas RAG.
