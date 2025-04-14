import streamlit as st
import pandas as pd
from logo import show_logo

# Impostazioni della pagina
st.set_page_config(page_title="Ricerca Dati", layout="wide")

# Tema scuro
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
    .hidden {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

show_logo()

# Titolo
st.title("GMR Inventario - Visualizzatore & Ricerca Dati")

# Link nascosto predefinito
default_file_url = "https://www.dropbox.com/scl/fi/emc2w2pai7kwv3v25w2pw/Copia-di-mm16.xlsx?rlkey=mwiiwcq2jla6irdli4916cajc&st=kcubfn1e&dl=1"

# Inizializzazione variabili
for key in ["filtered_df", "original_df", "file_loaded", "search_query"]:
    if key not in st.session_state:
        st.session_state[key] = None if "df" in key or "query" in key else False

# Uploader manuale
uploaded_file = st.file_uploader("Oppure carica un file CSV o XLSX", type=["csv", "xlsx"])

# Campo link opzionale (visivamente nascosto)
with st.expander("Carica da link personalizzato"):
    custom_url = st.text_input("Inserisci link al file XLSX")

if st.button("Carica da link") and custom_url.strip():
    try:
        df = pd.read_excel(custom_url.strip(), engine="openpyxl")
        st.session_state.original_df = df
        st.session_state.file_loaded = True
        st.success("File caricato dal link personalizzato!")
    except Exception as e:
        st.error(f"Errore nel caricamento del file: {e}")

# Caricamento da file uploadato
elif uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine="openpyxl")
        st.session_state.original_df = df
        st.session_state.file_loaded = True
        st.success("File caricato da upload!")
    except Exception as e:
        st.error(f"Errore nel caricamento del file: {e}")

# Caricamento automatico invisibile
elif not st.session_state.file_loaded:
    try:
        df = pd.read_excel(default_file_url, engine="openpyxl")
        st.session_state.original_df = df
        st.session_state.file_loaded = True
        st.success("File caricato automaticamente dal link di default.")
    except Exception as e:
        st.error(f"Errore nel caricamento del file di default: {e}")

# Se dati presenti, visualizza
if st.session_state.original_df is not None:
    st.write("Anteprima dei dati:")
    st.dataframe(st.session_state.original_df, use_container_width=True)

    # Ricerca
    col1, col2 = st.columns([4, 1])
    with col1:
        search_input = st.text_input("Cerca nella tabella", value=st.session_state.search_query or "")
    with col2:
        if st.button("Cerca"):
            if search_input.strip():
                st.session_state.search_query = search_input
                st.session_state.filtered_df = st.session_state.original_df[
                    st.session_state.original_df.apply(
                        lambda row: row.astype(str).str.contains(search_input, case=False).any(), axis=1
                    )
                ]
            else:
                st.warning("Inserisci un termine da cercare.")

    if st.session_state.filtered_df is not None and not st.session_state.filtered_df.empty:
        st.markdown("---")
        st.subheader("Risultati della ricerca:")
        st.dataframe(st.session_state.filtered_df, use_container_width=True)
    elif st.session_state.search_query:
        st.warning("Nessun risultato trovato.")

    # Pulsante Reset
        # Pulsante Reset
    if st.button("Annulla / Reset"):
        # Usiamo una chiave di stato temporanea per segnalare il reset
        st.session_state["do_reset"] = True
        st.rerun()

# Gestione reset dopo il rerun
if st.session_state.get("do_reset", False):
    for key in ["filtered_df", "original_df", "search_query", "file_loaded"]:
        st.session_state[key] = None if "df" in key or "query" in key else False
    st.session_state["do_reset"] = False