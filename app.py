from pathlib import Path

import pandas as pd
import streamlit as st


# =========================
# Configuração básica do app
# =========================
st.set_page_config(page_title="Vehicles US", layout="wide")
st.title("Sprint 5 — Vehicles US")


# ==========================================================
# Caminho do dataset (robusto para GitHub/Render)
# ----------------------------------------------------------
# Em vez de depender do "diretório atual" (que pode mudar no Render),
# montamos o caminho a partir da pasta onde o app.py está.
# Assim, se o arquivo vehicles_us.csv estiver AO LADO do app.py,
# a leitura funciona localmente e no deploy.
# ==========================================================
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = "vehicles_us.csv"
DATA_PATH = BASE_DIR / DATA_FILE


# ==========================================================
# Função de carga com cache
# ----------------------------------------------------------
# cache_data evita recarregar o CSV a cada interação no app
# (ex.: mexer em filtros), deixando o app mais rápido.
# ==========================================================
@st.cache_data(show_spinner="Carregando dados...")
def load_data(csv_path: Path) -> pd.DataFrame:
    # Lê o CSV. Se der erro (arquivo ausente/caminho errado), a exceção
    # será tratada fora para exibirmos uma mensagem clara no Streamlit.
    return pd.read_csv(csv_path)


# ======================
# Carregamento do dataset
# ======================
try:
    if not DATA_PATH.exists():
        # Mensagem objetiva: no Render, isso geralmente significa que o CSV
        # não foi commitado para o GitHub ou está com nome diferente.
        st.error(
            f"Não encontrei o arquivo `{DATA_FILE}` na mesma pasta do `app.py`.\n\n"
            f"Caminho procurado: {DATA_PATH}"
        )
        st.stop()

    df = load_data(DATA_PATH)

except Exception as e:
    # Se houver qualquer erro de leitura (CSV corrompido, encoding, etc.)
    st.error("Falha ao carregar o dataset. Detalhes do erro abaixo:")
    st.exception(e)
    st.stop()


# ==========================
# Sidebar (controles simples)
# ==========================
st.sidebar.header("Controles")

n_rows = st.sidebar.slider(
    "Quantas linhas mostrar na amostra?",
    min_value=5,
    max_value=50,
    value=20,
    step=5,
)

show_missing = st.sidebar.checkbox("Mostrar valores ausentes por coluna", value=True)


# ==========================
# Seção 1: visão geral
# ==========================
st.subheader("Informações básicas")
st.write({"linhas": df.shape[0], "colunas": df.shape[1]})

st.subheader("Amostra dos dados")
st.dataframe(df.head(n_rows))


# ==========================
# Seção 2: valores ausentes
# ==========================
if show_missing:
    st.subheader("Valores ausentes (por coluna)")
    missing = df.isna().sum().sort_values(ascending=False)
    missing = missing[missing > 0]

    if missing.empty:
        st.write("Não há valores ausentes no dataset.")
    else:
        # Mostramos como DataFrame para ficar legível no Streamlit
        st.dataframe(missing.rename("qtd_ausentes").to_frame())


# ==========================
# Seção 3: estatísticas simples
# ==========================
st.subheader("Resumo estatístico (colunas numéricas)")
numeric_cols = df.select_dtypes(include="number").columns.tolist()

if not numeric_cols:
    st.write("Não encontrei colunas numéricas para resumir.")
else:
    # describe() dá uma visão rápida (count, mean, std, min, quartis, max)
    st.dataframe(df[numeric_cols].describe().T)