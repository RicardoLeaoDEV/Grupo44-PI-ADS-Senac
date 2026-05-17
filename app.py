import streamlit as st
import pandas as pd
import os

# Configuração da página do Streamlit
st.set_page_config(
    page_title="PI - Impacto Global nos Combustíveis",
    page_icon="📊",
    layout="wide"
)

# Estilização para o topo
st.title("📊 Impacto Global: Preço dos Combustíveis e Mercado de Petróleo")
st.markdown("### Análise macroeconômica da volatilidade de preços e efeitos de conflitos geopolíticos")
st.write("---")

# Criando a linha executiva de KPIs no topo (Simulando o topo do Power BI)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Preço Médio Global", value="$1.11")
with col2:
    st.metric(label="Maior Preço", value="$370.00")
with col3:
    st.metric(label="Taxa Média de Aumento", value="4.96%")
with col4:
    st.metric(label="Petróleo Brent (Barril)", value="$83.33")

st.write("---")

# Seção de apresentação do Dashboard
st.subheader("🖼️ Preview do Dashboard Executivo")
st.write("Abaixo está a interface finalizada do dashboard desenvolvido no Power BI:")

# Caminho para o print do dashboard que já está na vossa pasta images
caminho_imagem = os.path.join("images", "dashboard1.png")

if os.path.exists(caminho_imagem):
    st.image(caminho_imagem, caption="Dashboard Interativo - Análise de Combustíveis e Petróleo", use_column_width=True)
else:
    st.info("O Dashboard finalizado foi estruturado e guardado na pasta 'dashboard' do repositório como um arquivo .pbix.")

st.write("---")
st.markdown("**Projeto Integrador desenvolvido para o curso de Análise e Desenvolvimento de Sistemas (ADS).**")
