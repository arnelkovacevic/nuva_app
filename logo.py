import streamlit as st

def show_logo():
    st.markdown(
        """
        <div style='margin-top: -10px; margin-left: 55px;'>
            <img src='https://i.ibb.co/8n1Gy1xm/x-logo.png' width='20'/>
        </div>
        <div style='display: flex; align-items: center; justify-content: flex-start; margin-bottom: 10px;'>
            <a href='https://gmr-inventario.app/login' target='_blank'>
                <img src='https://i.ibb.co/nqFLS5Kh/GMR.png' width='75'/>
            </a>
            <h2 style='margin-left: 20px;'>gXLS - Reader</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
