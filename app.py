import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA (PAGE CONFIG)
# ==============================================================================
st.set_page_config(page_title="US Vehicles Market Analysis — Pro Portfolio", layout="wide")

# ==============================================================================
# 2. CARREGAMENTO E LIMPEZA (DATA ENGINEERING)
# ==============================================================================
BASE_DIR = Path(__file__).resolve().parent

CANDIDATE_FILES = [BASE_DIR / "vehicles_us.csv", BASE_DIR / "vehicles.csv"]
DATA_PATH = next((p for p in CANDIDATE_FILES if p.exists()), None)

if DATA_PATH is None:
    st.error("Data source not found. Check if 'vehicles.csv' is in the root directory.")
    st.stop()

@st.cache_data(show_spinner="Cleaning and Processing Data...")
def load_and_clean_data(path):
    """
    Função para carregar e limpar dados. 
    Nota para Recrutadores: Implementamos Imputação Estatística para 
    evitar perda de dados e manter a integridade da amostra.
    """
    data = pd.read_csv(path)
    
    # Conversão de tipos para garantir operações numéricas
    cols_to_numeric = ["price", "odometer", "model_year", "cylinders", "is_4wd", "days_listed"]
    for col in cols_to_numeric:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    
    if "date_posted" in data.columns:
        data["date_posted"] = pd.to_datetime(data["date_posted"], errors="coerce")

    # IMPUTAÇÃO POR GRUPO (Data Imputation)

    data['model_year'] = data['model_year'].fillna(data.groupby('model')['model_year'].transform('median'))
    data['cylinders'] = data['cylinders'].fillna(data.groupby('model')['cylinders'].transform('median'))
    data['odometer'] = data['odometer'].fillna(data.groupby('model_year')['odometer'].transform('median'))
    
    # Padronização de variáveis binárias e categóricas
    data['is_4wd'] = data['is_4wd'].fillna(0)
    data['paint_color'] = data['paint_color'].fillna('unknown')
    
    # Feature Engineering: Extraindo a marca (Brand)
    data['brand'] = data['model'].apply(lambda x: str(x).split()[0])
    
    return data.dropna(subset=['price', 'model_year', 'odometer', 'days_listed'])

df = load_and_clean_data(DATA_PATH)

# ==============================================================================
# 3. CABEÇALHO 
# ==============================================================================
st.title("🚗 Sprint 5 — Vehicles US: Strategic Market Analysis")
st.markdown(f"""
### Overview
Este dashboard fornece uma análise profunda do mercado de veículos usados nos EUA. 
Além da exploração básica, focamos em **Liquidez de Mercado** e **Depreciação**.

**Link do Projeto:** [https://vehicles-env-1niq.onrender.com](https://vehicles-env-1niq.onrender.com)
""")

# ==============================================================================
# 4. SIDEBAR - FILTROS DINÂMICOS
# ==============================================================================
st.sidebar.header("Explore the Market")
filtered = df.copy()

# Filtro de Preço
pmin, pmax = float(df['price'].min()), float(df['price'].max())
price_range = st.sidebar.slider("Price Range (USD)", pmin, pmax, (pmin, pmax))
filtered = filtered[(filtered['price'] >= price_range[0]) & (filtered['price'] <= price_range[1])]

# Filtro de Marcas
all_brands = sorted(df['brand'].unique())
selected_brands = st.sidebar.multiselect("Select Brands", options=all_brands, default=all_brands[:10])
if selected_brands:
    filtered = filtered[filtered['brand'].isin(selected_brands)]

# ==============================================================================
# 5. DASHBOARD - VISUALIZAÇÕES
# ==============================================================================

# Métricas Rápidas
c1, c2, c3 = st.columns(3)
c1.metric("Listings Found", f"{len(filtered):,}")
c2.metric("Avg. Price", f"${filtered['price'].mean():,.0f}")
c3.metric("Avg. Days to Sell", f"{filtered['days_listed'].mean():.1f}")

st.divider()

# --- REQUISITO: HISTOGRAMA ---
st.subheader("1. Market Price Distribution")
show_hist = st.checkbox("Show Price Histogram", value=True)
if show_hist:
    fig_hist = px.histogram(filtered, x="price", nbins=50, 
                             title="Distribution of Vehicle Prices",
                             labels={'price': 'Price (USD)'},
                             color_discrete_sequence=['#00CC96'])
    st.plotly_chart(fig_hist, use_container_width=True)

# --- REQUISITO: GRÁFICO DE DISPERSÃO ---
st.subheader("2. Depreciation Analysis (Price vs. Odometer)")
show_scatter = st.checkbox("Show Scatter Plot", value=True)
if show_scatter:
    fig_scatter = px.scatter(filtered, x="odometer", y="price", 
                              color="condition", 
                              title="Impact of Mileage on Resale Value",
                              labels={'odometer': 'Odometer (Miles)', 'price': 'Price (USD)'},
                              hover_data=['model_year', 'brand'],
                              opacity=0.5)
    st.plotly_chart(fig_scatter, use_container_width=True)

# --- BÔNUS PORTFÓLIO: ANÁLISE DE LIQUIDEZ ---
st.divider()
st.subheader("3. 📈 Business Intelligence: Market Liquidity")
st.markdown("""
**Insight para Recrutadores:** Esta análise identifica quais categorias de veículos saem do estoque mais rápido. 
Menos tempo listado (*Days Listed*) significa maior demanda.
""")

liquidity = filtered.groupby('type')['days_listed'].mean().reset_index().sort_values('days_listed')
fig_liq = px.bar(liquidity, x='days_listed', y='type', orientation='h',
                 title="Liquidity: Average Days Listed by Category",
                 labels={'days_listed': 'Mean Days to Sell', 'type': 'Vehicle Type'},
                 color='days_listed', color_continuous_scale='Bluered')
st.plotly_chart(fig_liq, use_container_width=True)

# --- EXPLORAÇÃO DE DADOS ---
with st.expander("Explore Processed Data Table"):
    st.dataframe(filtered.head(50), use_container_width=True)


