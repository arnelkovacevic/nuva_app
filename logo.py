import streamlit as st

def show_logo():
    st.markdown(
        """
        <div style='display: flex; align-items: center; justify-content: flex-start; margin-bottom: 20px;'>
            <img src='https://i.ibb.co/nqFLS5Kh/GMR.png' width='100'/>
            <h2 style='margin-left: 20px;'>GMR Inventario</h2>
        </div>
        """,
        unsafe_allow_html=True
    )