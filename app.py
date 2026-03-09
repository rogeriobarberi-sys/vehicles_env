import pandas as pd
import streamlit as st
import plotly.express as px

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Market Insights - Veículos EUA", layout="wide")

@st.cache_data
def get_data():
    try:
        data = pd.read_csv('vehicles_us.csv')
    except FileNotFoundError:
        data = pd.read_csv('vehicles.csv')
    
    # Engenharia de Dados: Criando coluna 'make' (Marca)
    data['make'] = data['model'].apply(lambda x: str(x).split()[0])
    
    # Limpeza e Imputação
    data['is_4wd'] = data['is_4wd'].fillna(0).astype(int)
    data['paint_color'] = data['paint_color'].fillna('Não especificada')
    data['type'] = data['type'].fillna('other')
    data['model_year'] = data['model_year'].fillna(data['model_year'].median())
    return data

df = get_data()

# 2. CABEÇALHO
st.title("🚗 Dashboard Estratégico: Mercado de Veículos Usados")
st.markdown("---")

# 3. SIDEBAR (FILTROS E CONTROLES)
st.sidebar.header("Filtros Globais")

# Slider de Preço
price_limit = st.sidebar.slider("Preço Máximo ($)", min_value=500, max_value=150000, value=50000)

# Filtro de Marcas (Multiselect)
all_makes = sorted(df['make'].unique())
selected_makes = st.sidebar.multiselect("Selecionar Marcas", options=all_makes, default=[])

# Aplicação dos Filtros
filtered_df = df[df['price'] <= price_limit]
if selected_makes:
    filtered_df = filtered_df[filtered_df['make'].isin(selected_makes)]

# 4. TOGGLE PARA VISÃO ANALÍTICA
st.header("1. 📉 Tendências e Comportamento de Mercado")
show_comparison = st.toggle("Ativar Comparação Detalhada por Marca", value=False)

if show_comparison:
    st.subheader("Análise Comparativa de Preços por Marca")
    # Gráfico de barras com a média de preço por marca
    make_price = filtered_df.groupby('make')['price'].mean().sort_values(ascending=False).reset_index()
    fig_make = px.bar(make_price, x='make', y='price', color='price',
                     title="Preço Médio por Marca no Inventário",
                     labels={'make': 'Marca', 'price': 'Preço Médio ($)'})
    st.plotly_chart(fig_make, use_container_width=True)
else:
    st.subheader("Distribuição Geral de Preços")
    fig_hist = px.histogram(filtered_df, x="price", color="condition", nbins=50,
                           title="Histograma de Preços vs. Estado do Veículo",
                           labels={'price': 'Preço ($)', 'count': 'Frequência'})
    st.plotly_chart(fig_hist, use_container_width=True)

# 5. LIQUIDEZ E GIRO (O gráfico de barras horizontais)
st.header("2. 📈 Liquidez: Média de Dias em Anúncio")
liquidity_df = filtered_df.groupby('type')['days_listed'].mean().sort_values(ascending=False).reset_index()
fig_liq = px.bar(liquidity_df, x='days_listed', y='type', orientation='h',
                 title="Giro de Estoque por Categoria",
                 labels={'days_listed': 'Dias Médios', 'type': 'Categoria'},
                 color='days_listed', color_continuous_scale='Bluered_r')
st.plotly_chart(fig_liq, use_container_width=True)

# 6. DISPERSÃO (PREÇO X QUILOMETRAGEM) - CORREÇÃO OPACITY
st.header("3. 🔍 Ciclo de Vida: Depreciação por Uso")
fig_scatter = px.scatter(filtered_df, x="odometer", y="price", color="condition",
                         opacity=0.4, hover_data=['model_year', 'model'],
                         title="Relação Preço x Quilometragem",
                         labels={'odometer': 'Milhas Rodadas', 'price': 'Preço ($)'})
st.plotly_chart(fig_scatter, use_container_width=True)

# 7. MÉTRICAS FINAIS
st.divider()
c1, c2, c3 = st.columns(3)
c1.metric("Veículos em Análise", f"{len(filtered_df)} un.")
c2.metric("Preço Médio", f"${filtered_df['price'].mean():,.0f}")
c3.metric("Tempo Médio de Venda", f"{filtered_df['days_listed'].mean():.1f} dias")