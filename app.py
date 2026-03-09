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
    
    # Engenharia de Dados: Extraindo a Marca
    data['make'] = data['model'].apply(lambda x: str(x).split()[0])
    
    # Limpeza e Imputação (Consistente com o README)
    data['is_4wd'] = data['is_4wd'].fillna(0).astype(int)
    data['paint_color'] = data['paint_color'].fillna('Não especificada')
    data['type'] = data['type'].fillna('other')
    data['model_year'] = data['model_year'].fillna(data['model_year'].median())
    return data

df = get_data()

# 2. CABEÇALHO E INTRODUÇÃO
st.title("🚗 Dashboard Estratégico: Mercado de Veículos Usados")
st.markdown("""
Este painel integra análises de **Business Intelligence** para explorar tendências de preço, 
fatores de valorização e liquidez de mercado. Utilize os filtros laterais para refinar os insights.
""")
st.divider()

# 3. SIDEBAR (FILTROS GLOBAIS)
st.sidebar.header("Filtros de Pesquisa")

# Slider de Preço
price_limit = st.sidebar.slider("Preço Máximo ($)", min_value=500, max_value=150000, value=50000)

# Multiselect de Marcas
all_makes = sorted(df['make'].unique())
selected_makes = st.sidebar.multiselect("Selecionar Marcas", options=all_makes, default=[])

# Aplicação dos Filtros
filtered_df = df[df['price'] <= price_limit]
if selected_makes:
    filtered_df = filtered_df[filtered_df['make'].isin(selected_makes)]

# 4. ANÁLISE DE LIQUIDEZ E GIRO 
st.header("1. 📈 Liquidez: Giro de Estoque por Categoria")
st.info("Veículos com menor 'Média de Dias' possuem maior demanda e saem do pátio mais rápido.")

liquidity_df = filtered_df.groupby('type')['days_listed'].mean().sort_values(ascending=False).reset_index()
fig_liq = px.bar(liquidity_df, x='days_listed', y='type', orientation='h',
                 title="Giro de Estoque (Days Listed)",
                 labels={'days_listed': 'Média de Dias', 'type': 'Categoria'},
                 color='days_listed', color_continuous_scale='Bluered_r')
st.plotly_chart(fig_liq, use_container_width=True)

#5 ANÁLISE DE CONSERVAÇÃO Vs TEMPO
st.header("2. ⚡ Agilidade de Venda por Estado de Conservação")
st.markdown("Será que carros em melhor estado vendem mais rápido? O gráfico abaixo mostra a distribuição do tempo de anúncio para cada condição.")

fig_cond_time = px.strip(filtered_df, x='condition', y='days_listed', color='condition',
                         title="Dispersão de Dias no Anúncio por Condição",
                         labels={'condition': 'Condição', 'days_listed': 'Dias até Venda'})
st.plotly_chart(fig_cond_time, use_container_width=True)

st.info("**Conclusão:** Observe se há uma concentração maior de pontos na parte inferior para condições específicas. Isso indica um giro de estoque mais acelerado para esse perfil de veículo.")

# 5.5 ESTRUTURA DE PREÇOS (COM TOGGLE)
st.header("3. 📊 Análise de Precificação")
show_by_make = st.toggle("Alternar Visão: Por Marca vs. Por Condição", value=False)

if show_by_make:
    make_price = filtered_df.groupby('make')['price'].mean().sort_values(ascending=False).reset_index()
    fig_price = px.bar(make_price, x='make', y='price', color='price',
                      title="Preço Médio por Fabricante",
                      labels={'make': 'Marca', 'price': 'Preço Médio ($)'})
else:
    fig_price = px.histogram(filtered_df, x="price", color="condition", nbins=50,
                            title="Distribuição de Preços por Condição",
                            labels={'price': 'Preço ($)', 'count': 'Frequência'})

st.plotly_chart(fig_price, use_container_width=True)

# 6. VALOR AGREGADO: 4X4 E CORES (ABAS)
st.header("4. 🔍 Fatores de Valorização")
tab_4wd, tab_color = st.tabs(["Impacto do 4x4", "Influência da Cor"])

with tab_4wd:
    fig_4wd = px.box(filtered_df, x="is_4wd", y="price", color="is_4wd",
                    title="Diferença de Valor: Com vs. Sem 4x4",
                    labels={'is_4wd': 'Possui 4x4', 'price': 'Preço ($)'})
    st.plotly_chart(fig_4wd, use_container_width=True)

with tab_color:
    fig_color = px.box(filtered_df, x="paint_color", y="price", 
                      title="Distribuição de Preço por Cor do Veículo",
                      labels={'paint_color': 'Cor', 'price': 'Preço ($)'})
    st.plotly_chart(fig_color, use_container_width=True)

# 7. CICLO DE VIDA E TEMPO (O GRÁFICO DE BOLINHAS E LINHAS)
st.header("5. 📉 Ciclo de Vida e Depreciação")
col_scat, col_line = st.columns(2)

with col_scat:
    fig_scatter = px.scatter(filtered_df, x="odometer", y="price", color="condition",
                             opacity=0.4, hover_data=['model_year', 'model'],
                             title="Dispersão: Preço x Quilometragem",
                             labels={'odometer': 'Milhas Rodadas', 'price': 'Preço ($)'})
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_line:
    trend_df = filtered_df.groupby('model_year')['price'].mean().reset_index()
    fig_line = px.line(trend_df, x='model_year', y='price',
                      title="Evolução do Preço Médio por Ano",
                      labels={'model_year': 'Ano do Modelo', 'price': 'Preço Médio ($)'})
    st.plotly_chart(fig_line, use_container_width=True)

# 8. MÉTRICAS FINAIS
st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("Amostra Filtrada", f"{len(filtered_df)} veículos")
m2.metric("Preço Médio", f"${filtered_df['price'].mean():,.0f}")
m3.metric("Média de Dias Ativos", f"{filtered_df['days_listed'].mean():.1f} dias")
