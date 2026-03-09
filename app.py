import pandas as pd
import streamlit as st
import plotly.express as px

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Análise de Mercado Automotivo", layout="wide")

@st.cache_data
def get_data():
    try:
        data = pd.read_csv('vehicles_us.csv')
    except FileNotFoundError:
        data = pd.read_csv('vehicles.csv')
    
    # Tratamento e Imputação de Dados
    data['is_4wd'] = data['is_4wd'].fillna(0).astype(int)
    data['paint_color'] = data['paint_color'].fillna('Não especificada')
    data['type'] = data['type'].fillna('other')
    data['model_year'] = data['model_year'].fillna(data['model_year'].median())
    return data

df = get_data()

# 2. INTRODUÇÃO E OBJETIVOS
st.title("🚗 Dashboard Estratégico: Mercado de Veículos Usados")
st.markdown("""
Este painel apresenta uma análise exploratória avançada sobre o mercado automotivo, focando em fatores de precificação, 
depreciação e liquidez. O objetivo é fornecer insights baseados em dados para otimização de inventário e estratégias de venda.
""")
st.divider()

# 3. FILTROS E CONTROLES
st.sidebar.header("Parâmetros de Pesquisa")
price_limit = st.sidebar.slider("Filtrar por Preço Máximo ($)", min_value=500, max_value=150000, value=50000)
filtered_df = df[df['price'] <= price_limit]

# 4. ANÁLISE DE LIQUIDEZ (Giro de Estoque)
st.header("1. 📈 Liquidez de Mercado: Giro de Estoque por Categoria")
st.markdown("""
A análise de liquidez identifica quais categorias de veículos saem do estoque mais rápido. 
Menos tempo listado (**Days Listed**) indica maior demanda relativa no mercado.
""")

liquidity_df = filtered_df.groupby('type')['days_listed'].mean().sort_values(ascending=False).reset_index()
fig_liq = px.bar(liquidity_df, x='days_listed', y='type', orientation='h',
                 title="Média de Dias no Anúncio por Tipo de Veículo",
                 labels={'days_listed': 'Média de Dias para Venda', 'type': 'Categoria'},
                 color='days_listed',
                 color_continuous_scale='Bluered_r')
st.plotly_chart(fig_liq, use_container_width=True)

# 5. DISTRIBUIÇÃO E PRECIFICAÇÃO
st.header("2. 📊 Estrutura de Preços e Valor Agregado")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição por Condição")
    fig_hist = px.histogram(filtered_df, x="price", color="condition", nbins=50,
                           title="Histograma de Preços vs. Estado do Veículo",
                           labels={'price': 'Preço ($)', 'count': 'Frequência'})
    st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    st.subheader("Impacto da Tração 4x4")
    fig_box = px.box(filtered_df, x="is_4wd", y="price", color="is_4wd",
                    title="Distribuição de Valor: Com vs. Sem 4x4",
                    labels={'is_4wd': 'Tração 4x4', 'price': 'Preço ($)'})
    st.plotly_chart(fig_box, use_container_width=True)

# 6. DEPRECIAÇÃO E TENDÊNCIAS
st.header("3. 📉 Ciclo de Vida e Depreciação")

tab1, tab2 = st.tabs(["Uso vs. Valor", "Evolução Temporal"])

with tab1:
    st.markdown("Análise da correlação entre quilometragem (odômetro) e o preço de revenda.")
    # CORREÇÃO AQUI: alpha mudou para opacity
    fig_scatter = px.scatter(filtered_df, x="odometer", y="price", color="condition",
                             opacity=0.4, hover_data=['model_year', 'model'],
                             title="Dispersão: Preço x Quilometragem",
                             labels={'odometer': 'Milhas Rodadas', 'price': 'Preço ($)'})
    st.plotly_chart(fig_scatter, use_container_width=True)

with tab2:
    st.markdown("Visualização da tendência de preço médio baseada no ano de fabricação do modelo.")
    trend_df = filtered_df.groupby('model_year')['price'].mean().reset_index()
    fig_line = px.line(trend_df, x='model_year', y='price',
                      title="Valor Médio de Mercado por Ano do Modelo",
                      labels={'model_year': 'Ano de Fabricação', 'price': 'Preço Médio ($)'})
    st.plotly_chart(fig_line, use_container_width=True)

# 7. MÉTRICAS DE RESUMO
st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("Volume da Amostra", f"{len(filtered_df)} veículos")
m2.metric("Preço Médio", f"${filtered_df['price'].mean():,.0f}")
m3.metric("Média de Dias Ativos", f"{filtered_df['days_listed'].mean():.1f} dias")