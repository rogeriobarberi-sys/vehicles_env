# Mercado de Veículos EUA - Dashboard de Análise Exploratória (EDA)

Uma aplicação web avançada de Análise Exploratória de Dados construída com **Streamlit** e **Plotly**. Este projeto vai além da visualização básica, implementando limpeza de dados robusta e imputação estatística para fornecer insights de mercado confiáveis.

## 🛠 Tecnologias Utilizadas
- **Python** (Pandas, Pathlib)
- **Streamlit** (Interface Web e Implementação)
- **Plotly Express** (Gráficos Interativos)
- **Render** (Hospedagem em Nuvem)

## 📊 Engenharia e Limpeza de Dados (Abordagem Profissional)

Para garantir uma análise de alta qualidade e manter padrões de um portfólio profissional, as seguintes etapas de integridade de dados foram implementadas:

### 1. Imputação de Dados Robusta (Baseada em Grupos)
Em vez de simplesmente descartar linhas com valores ausentes, apliquei uma estratégia de **imputação contextual**:
- **Ano do Modelo e Cilindros:** Valores ausentes foram preenchidos usando a **mediana** de cada `modelo` de veículo específico. Isso preserva a distribuição característica de cada tipo de carro.
- **Odômetro:** A quilometragem ausente foi imputada com base na **mediana** do `ano_do_modelo` correspondente, refletindo a correlação lógica entre a idade do carro e seu uso.
- **Atributos Booleanos:** A coluna `is_4wd` foi padronizada, tratando nulos como `0` (Falso) com base na estrutura do conjunto de dados.

### 2. Programação Defensiva e Tipagem
- Implementação de resolução de caminhos de arquivo robusta usando `pathlib` para garantir o funcionamento perfeito no **Render/GitHub**.
- Aplicação de tipagem numérica rigorosa para `preço`, `odômetro` e `ano_do_modelo` para evitar erros durante a filtragem interativa.

### 3. Lógica de Visualização Avançada
- **Análise de Depreciação:** Gráfico de dispersão com sobreposição de "Condição" para visualizar como o desgaste afeta o valor de revenda.
- **Segmentação de Mercado:** Boxplots para identificar outliers de preço e a distribuição entre diferentes tipos de veículos (SUV, Caminhão, Sedan, etc.).

---
*Nota: Este projeto foi desenvolvido como parte do Bootcamp de Análise de Dados da TripleTen, aprimorado com funcionalidades personalizadas para atingir padrões de portfólio profissional.*
