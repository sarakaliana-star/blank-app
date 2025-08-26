import streamlit as st

st.title("🎈 Meu primeiro APP")


# Título do app
st.title("Comparação de Indicadores Educacionais – MEPES x Escolas do Campo no ES")

# Nome da autora
st.write("Desenvolvido por **Sara Kaliana de Almeida Ferreira**")

st.header("Filtros de Visualização")

tipo_escola = st.selectbox(
    "Selecione o tipo de escola:",
    ["MEPES (EFAs)", "Escolas do Campo da Rede"]
)

etapa_ensino = st.selectbox(
    "Selecione a etapa de ensino:",
    ["Ensino Fundamental - Anos Iniciais", 
     "Ensino Fundamental - Anos Finais", 
     "Ensino Médio"]
)

indicador = st.radio(
    "Selecione o indicador:",
    ["Taxa de Abandono", "Distorção Idade-Série"]
)

st.write(f"📌 Você selecionou: **{tipo_escola}** | **{etapa_ensino}** | **{indicador}**")


# Análises

st.header("Análises e Insights")
st.write("""
Nesta seção serão apresentados os principais achados a partir das comparações,
destacando o papel das EFAs e da pedagogia da alternância na permanência escolar.
""")

# Bases de Dados
# ==============================
st.header("Bases de Dados")
st.write("""
Os dados utilizados serão provenientes dos **Microdados do Censo Escolar (INEP)**,
filtrando as escolas do campo e as escolas do MEPES no Espírito Santo.
Os indicadores a serem analisados são:
- Taxa de Abandono
- Distorção Idade-Série
""")
