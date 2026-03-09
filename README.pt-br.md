# Vehicles US — Análise Exploratória (EDA) + App Interativo

Este repositório contém um projeto de **Análise Exploratória de Dados (EDA)** com um **aplicativo interativo em Streamlit**, usando o dataset **Vehicles US**.  
O objetivo é explorar o conjunto de dados, documentar decisões de qualidade (tipos, ausências, possíveis outliers) e entregar visualizações interativas que sustentem conclusões claras.

## Links

- **Aplicativo (Render):** https://vehicles-env-1niq.onrender.com  
- **Repositório (GitHub):** https://github.com/rogeriobarberi-sys/vehicles_env  
- **README em inglês:** [README.md](README.md)

---

## Objetivos do projeto

- Construir um fluxo de EDA **reprodutível**
- Identificar e documentar **problemas de qualidade** (valores ausentes, tipos, valores extremos)
- Criar **visualizações interativas** para apoiar a análise
- Publicar um app web funcional como peça **de portfólio**

---

## Dataset

- Arquivo: `vehicles_us.csv`  
- Contexto: anúncios/listagens de veículos usados com campos como **preço**, **odômetro**, **ano do modelo**, **condição**, etc.

---

## Funcionalidades do app (EDA interativa)

O app em Streamlit permite:

- Visualizar uma **amostra dos dados** (tabela) após aplicar filtros
- Inspecionar **valores ausentes** por coluna
- Consultar **estatísticas descritivas** das colunas numéricas
- Interagir com controles de interface (ex.: **checkbox**, filtros)
- Explorar pelo menos duas visualizações:
  - **Histograma** (ex.: distribuição de `price`)
  - **Gráfico de dispersão** (ex.: `price` vs `odometer`)

---

## Limpeza e pré-processamento (decisões documentadas)
A proposta do projeto é evitar “mágica escondida” e aplicar decisões de forma transparente.


### 1) Tipos de dados
- Validar colunas numéricas (ex.: `price`, `odometer`, `model_year`) como numéricas
- Confirmar colunas categóricas (ex.: `condition`) como texto/categoria

### 2) Valores ausentes
- Medir a quantidade de valores ausentes por coluna
- Para gráficos que exigem valores completos (ex.: dispersão), linhas com `x` ou `y` ausentes são removidas **apenas naquele gráfico**, e não no dataset inteiro

### 3) Outliers (abordagem pragmática)
- Inspecionar valores extremos (preços muito altos / odômetro muito alto)
- Evitar apagar linhas “só para ficar bonito”; aplicar filtros apenas quando fizer sentido analítico e de forma explícita

> **Nota:** credibilidade de portfólio vem de decisões claras e justificadas, não de gráficos “perfeitos”.

---

## Principais conclusões (substitua pelos seus achados reais)

Inclua 3–6 bullets com o que você realmente observou. Estrutura exemplo:

- A distribuição de **preço** é assimétrica (concentração em faixas mais baixas)
- Em geral, **maior quilometragem** tende a associar-se a **menor preço**, com variações por condição
- A **condição** do veículo sugere faixas de preço distintas e impacta fortemente o valor

---

## Tecnologias

- **Python**
- **Pandas**
- **Streamlit**
- **Plotly**

---

## Como rodar localmente

1. Clone o repositório:
   - `git clone https://github.com/rogeriobarberi-sys/vehicles_env.git`
2. Entre na pasta do projeto:
   - `cd vehicles_env`
3. Instale as dependências:
   - `pip install -r requirements.txt`
4. Rode o app:
   - `streamlit run app.py`

---

## Estrutura do repositório

- `app.py` — app em Streamlit (EDA interativa + gráficos)
- `EDA.ipynb` — notebook com análise exploratória
- `vehicles_us.csv` — dataset usado pelo app
- `requirements.txt` — dependências Python
- `render.yaml` — configuração de deploy no Render
- `.streamlit/` — configuração do Streamlit (tema/ajustes)
