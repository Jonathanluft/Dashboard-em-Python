import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(page_title="Monitoramento de Irrigação", layout="wide")
st.title("Dashboard de Monitoramento do Sistema de Irrigação 🌱")

# Função para gerar dados iniciais
def generate_data():
    date_range = pd.date_range(end=datetime.now(), periods=24*6, freq='10T')
    moisture = np.random.uniform(20, 80, size=len(date_range))
    relay_state = np.random.choice([0, 1], size=len(date_range))
    ph = np.random.uniform(5, 8, size=len(date_range))
    p = np.random.uniform(0, 50, size=len(date_range))
    k = np.random.uniform(0, 50, size=len(date_range))
    
    return pd.DataFrame({
        "timestamp": date_range,
        "umidade": moisture,
        "rele": relay_state,
        "pH": ph,
        "fosforo": p,
        "potassio": k
    }).set_index("timestamp")

# Inicializar dados na sessão do Streamlit
if 'df' not in st.session_state:
    st.session_state.df = generate_data()

# Sidebar para filtros
st.sidebar.header("Filtros")
date_range = st.sidebar.date_input(
    "Selecione o período:",
    value=(st.session_state.df.index.min().date(), st.session_state.df.index.max().date())
)

# Tabs para organizar as visualizações
tab1, tab2, tab3 = st.tabs(["Dashboard", "Tabela de Dados", "Simulação"])

with tab1:
    st.subheader("Métricas em Tempo Real 📊")
    
    # Gráfico de Umidade e Estado do Relé
    col1, col2 = st.columns(2)
    with col1:
        st.line_chart(st.session_state.df[["umidade"]], color="#1f77b4")
        st.caption("Umidade do Solo (%)")
    
    with col2:
        fig, ax = plt.subplots()
        ax.step(st.session_state.df.index, st.session_state.df["rele"], where='post', color="#ff7f0e")
        ax.set_ylim(-0.1, 1.1)
        ax.set_yticks([0, 1])
        ax.set_yticklabels(["Desligado", "Ligado"])
        st.pyplot(fig)
        st.caption("Estado da Bomba de Irrigação")
    
    # Gráficos de pH e Nutrientes
    st.subheader("Qualidade do Solo")
    col3, col4 = st.columns(2)
    with col3:
        st.line_chart(st.session_state.df[["pH"]], color="#2ca02c")
        st.caption("Nível de pH")
    
    with col4:
        st.line_chart(st.session_state.df[["fosforo", "potassio"]], color=["#d62728", "#9467bd"])
        st.caption("Nutrientes (Fósforo e Potássio)")

with tab2:
    st.subheader("Dados Brutos 📋")
    st.dataframe(st.session_state.df, use_container_width=True)

with tab3:
    st.subheader("Simular Nova Leitura 🔄")
    
    # Inputs para simulação
    moisture_input = st.slider("Umidade (%)", 0, 100, 50)
    ph_input = st.slider("pH", 3.0, 10.0, 6.5)
    p_input = st.slider("Fósforo (mg/kg)", 0, 100, 30)
    k_input = st.slider("Potássio (mg/kg)", 0, 100, 30)
    
    if st.button("Simular"):
        new_data = pd.DataFrame({
            "timestamp": [datetime.now()],
            "umidade": [moisture_input],
            "rele": [1 if moisture_input < 30 else 0],
            "pH": [ph_input],
            "fosforo": [p_input],
            "potassio": [k_input]
        }).set_index("timestamp")
        
        # Atualizar os dados na sessão
        st.session_state.df = pd.concat([st.session_state.df, new_data])
        st.success("Dados simulados adicionados!")