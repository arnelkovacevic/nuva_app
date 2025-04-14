import streamlit as st
import pandas as pd

# Impostazioni della pagina
st.set_page_config(page_title="Ricerca Dati", layout="wide")

# Tema scuro (manuale)
st.markdown("""
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
    .hidden-input {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Titolo
st.title("GMR Inventario - Visualizzatore & Ricerca Dati")

# Link nascosto predefinito
default_file_url = "https://www.dropbox.com/scl/fi/emc2w2pai7kwv3v25w2pw/Copia-di-mm16.xlsx?rlkey=mwiiwcq2jla6irdli4916cajc&st=kcubfn1e&dl=1"

# Inizializzazione variabili session_state
for key in ["filtered_df", "original_df", "file_loaded"]:
    if key not in st.session_state:
        st.session_state[key] = None if "df" in key else False

# Upload manuale
uploaded_file = st.file_uploader("Oppure carica un file CSV o XLSX", type=["csv", "xlsx"])

# Pulsante "Carica da link"
url = st.text_input("Inserisci link al file XLSX", value="", key="custom_link_input")
carica_da_link = st.button("Carica da link")

df = None

# 1. Caricamento da file uploadato
if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.success("File caricato da upload!")
        st.session_state.file_loaded = True
    except Exception as e:
        st.error(f"Errore nel caricamento del file: {e}")

# 2. Caricamento manuale da link
elif carica_da_link and url.strip():
    try:
        df = pd.read_excel(url.strip(), engine="openpyxl")
        st.success("File caricato dal link personalizzato!")
        st.session_state.file_loaded = True
    except Exception as e:
        st.error(f"Errore nel caricamento del file dal link: {e}")

# 3. Caricamento automatico invisibile dal link predefinito
elif not st.session_state.file_loaded:
    try:
        df = pd.read_excel(default_file_url, engine="openpyxl")
        st.success("File caricato automaticamente dal link di default.")
        st.session_state.file_loaded = True
    except Exception as e:
        st.error(f"Errore nel caricamento del file dal link predefinito: {e}")

# Se è stato caricato un DataFrame valido
if df is not None:
    st.session_state.original_df = df

# Visualizza i dati (originali o filtrati)
if st.session_state.original_df is not None:
    st.write("Anteprima dei dati:")

    if st.session_state.filtered_df is not None:
        st.dataframe(st.session_state.filtered_df, use_container_width=True)
    else:
        st.dataframe(st.session_state.original_df, use_container_width=True)

    # Barra ricerca
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        search_query = st.text_input("Cerca nella tabella", placeholder="Inserisci testo...")

    with col2:
        if st.button("Cerca"):
            if search_query.strip():
                filtered_df = st.session_state.original_df[
                    st.session_state.original_df.apply(
                        lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1
                    )
                ]
                if not filtered_df.empty:
                    st.session_state.filtered_df = filtered_df
                else:
                    st.warning("Nessun risultato trovato.")
            else:
                st.warning("Inserisci un termine di ricerca.")

    with col3:
        if st.button("Nuova ricerca"):
            st.session_state.filtered_df = None

    # Pulsante Annulla
    if st.button("Annulla"):
        st.session_state.filtered_df = None
        st.session_state.original_df = None
        st.session_state.file_loaded = False
        st.experimental_rerun()