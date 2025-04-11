import streamlit as st
import pandas as pd
from PIL import Image

# Impostazioni della pagina
st.set_page_config(page_title="Ricerca Dati", layout="wide")

# Tema scuro (da impostazioni Streamlit, oppure manualmente da menu settings UI)
st.markdown(
    """
    <style>
    body {
        background-color: #0e1117;
        color: white;
    }
    .stButton>button {
        color: white;
        background-color: #1f77b4;
    }
    .stTextInput>div>div>input {
        background-color: #262730;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Carica logo
logo_path = "/Users/arnel/Documents/APPS/NUVA_WEBAPP/assets/GMR.png"
try:
    logo = Image.open(logo_path)
    logo = logo.resize((80, 80))  # ridimensiona se necessario
    col_logo, col_title = st.columns([1, 8])
    with col_logo:
        st.image(logo)
    with col_title:
        st.title("GMR Inventario - Visualizazatore & Ricerca Dati")
except Exception as e:
    st.title("GMR Inventario - Visualizazatore & Ricerca Dati")
    st.warning(f"Logo non caricato: {e}")

# File uploader
uploaded_file = st.file_uploader("Carica un file CSV o XLSX", type=["csv", "xlsx"])

# Variabili di stato per ricerca
if "filtered_df" not in st.session_state:
    st.session_state.filtered_df = None

if "original_df" not in st.session_state:
    st.session_state.original_df = None

if uploaded_file:
    # Leggi il file
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.session_state.original_df = df
        st.write("Anteprima dei dati:")
        st.dataframe(df, use_container_width=True)

        # Casella di ricerca
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            search_query = st.text_input("Cerca nella tabella", placeholder="Inserisci testo...")

        with col2:
            if st.button("Cerca"):
                if search_query.strip() != "":
                    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)]
                    st.session_state.filtered_df = filtered_df
                else:
                    st.warning("Inserisci un termine di ricerca.")

        with col3:
            if st.button("Nuova ricerca"):
                st.session_state.filtered_df = None

        # Bottone Annulla
        if st.button("Annulla"):
            st.session_state.filtered_df = None
            st.session_state.original_df = None

        # Mostra tabella filtrata o completa
        if st.session_state.filtered_df is not None:
            st.write("Risultati della ricerca:")
            st.dataframe(st.session_state.filtered_df, use_container_width=True)

    except Exception as e:
        st.error(f"Errore nel caricamento del file: {e}")
