import streamlit as st

def show_logo():
    st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: flex-start; margin-bottom: 20px;'>
            <img src='https://www.dropbox.com/scl/fi/ylush0jc19rum18nqb8rs/apple-touch-icon-180x180.png?rlkey=w8vsuhanee8udezq5aiziijgp&st=5j2wwgo1&dl=1' width='100'/>
            <h2 style='margin-left: 20px;'>GMR Inventario</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    