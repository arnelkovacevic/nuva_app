import streamlit as st
import pandas as pd

# Impostazioni della pagina
st.set_page_config(page_title="Ricerca Dati", layout="wide")

# Tema scuro (manuale)
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

# Titolo
st.title("GMR Inventario - Visualizzatore & Ricerca Dati")

# File predefinito
default_file_url = "https://www.dropbox.com/scl/fi/emc2w2pai7kwv3v25w2pw/Copia-di-mm16.xlsx?rlkey=mwiiwcq2jla6irdli4916cajc&st=kcubfn1e&dl=1"

# Campo per link + pulsante Carica
url = st.text_input("Inserisci link al file XLSX (OneDrive, Dropbox, ecc.)", value=default_file_url)
carica_da_link = st.button("Carica da link")

# Uploader manuale
uploaded_file = st.file_uploader("Oppure carica un file CSV o XLSX", type=["csv", "xlsx"])

# Inizializzazione variabili
if "filtered_df" not in st.session_state:
    st.session_state.filtered_df = None
if "original_df" not in st.session_state:
    st.session_state.original_df = None
if "file_loaded" not in st.session_state:
    st.session_state.file_loaded = False

df = None

# 1. Caricamento da file uploadato
if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.session_state.file_loaded = True
        st.success("File caricato da upload!")
    except Exception as e:
        st.error(f"Errore nel caricamento del file: {e}")

# 2. Caricamento automatico da link predefinito (solo se non già caricato)
elif not st.session_state.file_loaded:
    try:
        df = pd.read_excel(default_file_url, engine="openpyxl")
        st.session_state.file_loaded = True
        st.success("File caricato automaticamente dal link di default!")
    except Exception as e:
        st.error(f"Errore nel caricamento del file dal link predefinito: {e}")

# 3. Caricamento manuale da link
elif carica_da_link and url:
    try:
        df = pd.read_excel(url, engine="openpyxl")
        st.session_state.file_loaded = True
        st.success("File caricato da link!")
    except Exception as e:
        st.error(f"Errore nel caricamento del file dal link: {e}")

# 4. Visualizzazione dati
if df is not None:
    st.session_state.original_df = df
    st.write("Anteprima dei dati:")
    st.dataframe(df, use_container_width=True)

    # Ricerca
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
        st.session_state.file_loaded = False
        st.experimental_rerun()

    # Mostra risultati
    if st.session_state.filtered_df is not None:
        st.write("Risultati della ricerca:")
        st.dataframe(st.session_state.filtered_df, use_container_width=True)