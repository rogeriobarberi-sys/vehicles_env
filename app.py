import pandas as pd
import streamlit as st

# Configurações básicas da página do Streamlit (título do navegador e layout mais largo)
st.set_page_config(page_title='Vehicles US', layout='wide')

# Título principal da aplicação
st.title('Sprint 5 — Vehicles US')

@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    # Lê o dataset a partir de um arquivo CSV.
    # Usamos cache para não recarregar o arquivo a cada interação do usuário na página,
    # melhorando a performance e evitando leituras repetidas do disco.
    return pd.read_csv(path)

# Carrega os dados do arquivo CSV que está na raiz do repositório
df = load_data('vehicles_us.csv')

# Mostra uma amostra inicial para validar rapidamente se o carregamento funcionou
st.subheader('Amostra dos dados')
st.dataframe(df.head(20))

# Mostra um resumo mínimo (quantidade de linhas e colunas) para “visão geral” do dataset
st.subheader('Informações básicas')
st.write({'linhas': df.shape[0], 'colunas': df.shape[1]})