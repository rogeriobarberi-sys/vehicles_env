import pandas as pd
import streamlit as st
import plotly.express as px

# 1. CONFIGURAÇÃO E CARREGAMENTO
st.set_page_config(page_title="Data Auto Insights", layout="wide")

@st.cache_data
def get_data():
    try:
        data = pd.read_csv('vehicles_us.csv')
    except FileNotFoundError:
        data = pd.read_csv('vehicles.csv')
    
    # Tratamento de dados para evitar erros nos gráficos
    data['is_4wd'] = data['is_4wd'].fillna(0).astype(int)
    data['paint_color'] = data['paint_color'].fillna('Não especificada')
    data['model_year'] = data['model_year'].fillna(df['model_year'].median()) if 'df' in locals() else data['model_year']
    return data

df = get_data()

# 2. CABEÇALHO
st.title("🚗 Análise Avançada de Mercado Automotivo")
st.markdown("---")

# 3. FILTROS NA BARRA LATERAL (Interatividade Avançada)
st.sidebar.header("Painel de Controle")
selected_make = st.sidebar.multiselect("Selecione Marcas Específicas", 
                                      options=sorted(df['model'].str.split().str[0].unique()),
                                      default=[])

price_limit = st.sidebar.slider("Filtrar por Preço Máximo ($)", 500, 100, 50000)

# Filtragem lógica
if selected_make:
    mask = (df['model'].str.startswith(tuple(selected_make))) & (df['price'] <= price_limit)
else:
    mask = df['price'] <= price_limit

filtered_df = df[mask]

# 4. GRÁFICOS LADO A LADO (LAYOUT PROFISSIONAL)
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Distribuição de Preço")
    fig1 = px.histogram(filtered_df, x="price", color="condition", nbins=50,
                       title="Preço vs Condição",
                       labels={'price': 'Preço ($)', 'count': 'Frequência'})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("📈 Preço vs Odômetro")
    # Este é o gráfico de "bolinhas" que você perguntou!
    fig2 = px.scatter(filtered_df, x="odometer", y="price", color="condition",
                     hover_data=['model_year', 'model'],
                     title="Impacto da Quilometragem no Valor",
                     labels={'odometer': 'Milhas Rodadas', 'price': 'Preço ($)'})
    st.plotly_chart(fig2, use_container_width=True)

# 5. ANÁLISE DE ATRIBUTOS (4x4 e Cor)
st.markdown("---")
st.header("🔍 O que valoriza o veículo?")

tab1, tab2 = st.tabs(["Tração 4x4", "Cores & Estética"])

with tab1:
    # Gráfico para medir se 4x4 ajuda a vender mais caro
    avg_4wd = filtered_df.groupby('is_4wd')['price'].median().reset_index()
    avg_4wd['is_4wd'] = avg_4wd['is_4wd'].map({1: 'Com 4x4', 0: 'Sem 4x4'})
    fig_4wd = px.bar(avg_4wd, x='is_4wd', y='price', color='is_4wd',
                    title="Mediana de Preço por Tipo de Tração")
    st.plotly_chart(fig_4wd)
    st.write("**Interpretação:** A mediana ajuda a ignorar valores muito discrepantes e focar no 'preço real' do mercado.")

with tab2:
    # Análise de cores
    fig_color = px.box(filtered_df, x="paint_color", y="price", 
                      title="Distribuição de Preços por Cor",
                      labels={'paint_color': 'Cor', 'price': 'Preço ($)'})
    st.plotly_chart(fig_color, use_container_width=True)

# 6. ANÁLISE DE TEMPO (O QUE VOCÊ PEDIU)
st.header("⏳ Análise de Tempo e Depreciação")
# Gráfico de linha para ver Ano vs Preço Médio
trend_df = filtered_df.groupby('model_year')['price'].mean().reset_index()
fig_line = px.line(trend_df, x='model_year', y='price',
                  title="Evolução do Valor Médio por Ano do Modelo",
                  labels={'model_year': 'Ano do Carro', 'price': 'Preço Médio'})
st.plotly_chart(fig_line, use_container_width=True)

# 7. VALIDAÇÃO E MÉTRICAS
st.markdown("---")
m1, m2, m3 = st.columns(3)
m1.metric("Veículos Exibidos", len(filtered_df))
m2.metric("Preço Médio", f"${filtered_df['price'].mean():,.2f}")
m3.metric("Tempo Médio de Venda", f"{filtered_df['days_listed'].mean():.1f} dias")

