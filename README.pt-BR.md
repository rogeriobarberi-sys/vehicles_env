# 🚗 Mercado de Veículos EUA - Dashboard de Análise Estratégica

Uma aplicação web de **Business Intelligence** construída com **Streamlit** e **Plotly**. Este projeto transforma um dataset bruto de anúncios automotivos em uma ferramenta de decisão, utilizando técnicas avançadas de engenharia de dados e visualização interativa.

## 🚀 Demonstração ao Vivo
[https://vehicles-env-1niq.onrender.com](https://vehicles-env-1niq.onrender.com)

---

## 🛠 Tecnologias Utilizadas
* **Python 3.12** (Core do projeto)
* **Pandas** (Manipulação e Imputação Estatística)
* **Streamlit** (Interface Web e Deploy de Dashboards)
* **Plotly Express** (Visualizações Interativas Dinâmicas)
* **Render** (Hospedagem e CI/CD via GitHub)

---

## 📊 Engenharia e Limpeza de Dados (Abordagem Profissional)

A integridade dos insights depende da qualidade dos dados. Implementei um pipeline de limpeza que evita o descarte de informações valiosas:

### 1. Imputação de Dados Contextual (Group-based Imputation)
Para evitar o viés de simplesmente deletar linhas incompletas, utilizei a **imputação estatística**:
* **Ano do Modelo e Cilindros:** Valores ausentes foram preenchidos usando a **mediana por modelo** (`groupby('model')`), garantindo que um sedan não receba especificações de um caminhão.
* **Odômetro:** A quilometragem foi imputada com base na **mediana do ano do modelo**, respeitando a correlação natural entre idade e uso.
* **Tratamento de Booleanos:** A coluna `is_4wd` foi normalizada (nulos para `0`), permitindo análises binárias precisas de valorização.

### 2. Programação Defensiva e Otimização
* **Resolução de Caminhos (Pathlib):** O sistema detecta automaticamente o ambiente (Local vs Render) para localizar os arquivos `.csv`, eliminando erros de diretório.
* **Cache de Dados (`@st.cache_data`):** Implementação de cache para que o carregamento e processamento de 51.525 linhas ocorram apenas uma vez, tornando a experiência do usuário instantânea.



---

## 📈 Análises de Negócio Implementadas

O dashboard foi projetado para responder a perguntas estratégicas de mercado:

* **Análise de Valor Agregado (4x4):** Medimos o impacto financeiro da tração integral no preço de revenda usando **Boxplots**, permitindo identificar a mediana e a dispersão de preços (outliers).
* **Impacto da Quilometragem (Depreciação):** Gráficos de dispersão interativos que correlacionam o uso do veículo com o seu valor, segmentados por condição (Excellent, Good, Fair).
* **Análise de Liquidez (Tempo de Venda):** Estudo de `days_listed` para entender quais faixas de preço e tipos de veículos possuem o maior giro de estoque.
* **Curva de Tendência Temporal:** Gráficos de linha que demonstram a variação do preço médio conforme o ano de fabricação, essencial para entender a depreciação anual.

---

## 📁 Estrutura do Repositório
* `app.py`: Código principal da aplicação Streamlit.
* `notebooks/EDA.ipynb`: Análise exploratória detalhada e rascunhos de limpeza.
* `vehicles_us.csv`: Base de dados (referenciada na raiz).
* `requirements.txt`: Lista de dependências para o ambiente de produção.

---

### 💡 Como rodar este projeto localmente
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv env`.
3. Ative o ambiente e instale as dependências: `pip install -r requirements.txt`.
4. Execute o app: `streamlit run app.py`.