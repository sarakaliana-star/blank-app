import streamlit as st

# ==============================
# Cabeçalho
# ==============================
st.title("📊 Comparação de Indicadores Educacionais – MEPES x Escolas do Campo no ES")
st.write("Desenvolvido por **Sara Kaliana de Almeida Ferreira**")

# ==============================
# Layout com Tabs
# ==============================
tab1, tab2, tab3 = st.tabs(["Filtros", "Análises", "Bases de Dados"])

# ==============================
# Aba Filtros
# ==============================
with tab1:
    st.header("🎯 Filtros de Visualização")
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            tipo_escola = st.selectbox(
                "Selecione o tipo de escola:",
                ["MEPES (EFAs)", "Escolas do Campo da Rede"]
            )
        with col2:
            etapa_ensino = st.selectbox(
                "Selecione a etapa de ensino:",
                ["Ensino Fundamental - Anos Finais", 
                 "Ensino Médio"]
            )

    indicador = st.radio(
        "Selecione o indicador:",
        ["Taxa de Abandono", "Distorção Idade-Série"]
    )

    st.write(f"📌 Você selecionou: **{tipo_escola}** | **{etapa_ensino}** | **{indicador}**")


# ==============================
# Aba Análises
# ==============================
with tab2:
    st.header("📈 Análises e Insights")
    st.write("""
    Nesta seção serão apresentados os principais achados a partir das comparações,
    destacando o papel das EFAs e da pedagogia da alternância na permanência escolar.
    """)

    # Exemplo de containers lado a lado
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Gráfico (placeholder)")
        st.write("Aqui entrará um gráfico futuramente.")
    with col2:
        st.subheader("📝 Observações")
        st.write("Espaço para observações sobre os resultados.")


# ==============================
# Aba Bases de Dados
# ==============================
with tab3:
    st.header("📂 Bases de Dados")
    st.write("""
    Os dados utilizados serão provenientes dos **Microdados do Censo Escolar (INEP)**,
    filtrando as escolas do campo e as escolas do MEPES no Espírito Santo.
    Os indicadores a serem analisados são:
    - Taxa de Abandono
    - Distorção Idade-Série
    """)
