
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="IA Café Commodity", layout="centered")

st.title("☕ IA Café Commodity")
st.write("Análise de mercado e estratégia personalizada com base no seu estoque.")

# Inputs do usuário
volume = st.number_input("📦 Volume do seu estoque (em sacas)", value=1000)
custo_medio = st.number_input("💰 Custo médio por saca (R$)", value=750.0)
meta_venda = st.number_input("🎯 Meta de preço de venda (R$)", value=950.0)

# Cotação atual
st.markdown("---")
st.subheader("📊 Cotação atual do Café Contrato C")
dados = yf.download("KC=F", period="7d", interval="1d")
preco_dolar = dados['Close'].iloc[-1]
preco_atual = preco_dolar * 5.5  # conversão estimada

st.metric("💲 Preço atual estimado (R$/saca)", f"R${preco_atual:.2f}")

# Cálculo de margem
margem = preco_atual - custo_medio
st.metric("📈 Margem atual", f"R${margem:.2f}")

# Estratégia sugerida
st.markdown("---")
st.subheader("📌 Recomendação Estratégica")

if preco_atual >= meta_venda:
    st.success("✅ Meta de preço atingida! Avalie venda parcial ou total do estoque.")
elif margem > 0:
    st.warning("🔄 Está no lucro, mas abaixo da meta. Considere hedge ou venda parcial.")
else:
    st.info("⏳ Preço abaixo do custo médio. Melhor segurar por enquanto.")

st.markdown("---")
st.caption("Desenvolvido para produtores e negociadores de café. Dados via Yahoo Finance.")
