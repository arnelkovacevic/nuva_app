import streamlit as st

def show_logo():
    st.markdown(
        """
        <div style='margin-bottom: 0px; margin-left: 55px;'>
            <img src='https://i.ibb.co/cK1skNcK/IMG-6318.png' width='20'/>
        </div>
        <div style='display: flex; align-items: center; justify-content: flex-start; margin-top: -5px; gap: 10px;'>
            <a href='https://gmr-inventario.app/login' target='_blank' style='display: flex; align-items: center; gap: 10px;'>
                <img src='https://i.ibb.co/nqFLS5Kh/GMR.png' width='75'/>
                <img src='https://i.ibb.co/MkdYPmgJ/ba515e32-8e6a-4a78-8491-0567df6debb4.png' width='56'/>
            </a>
            <h2 style='margin-left: 40px;'>gXLS - Reader</h2>
        </div>
        """,
        unsafe_allow_html=True
    )