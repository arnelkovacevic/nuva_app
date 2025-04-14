import streamlit as st

def set_favicon():
    st.markdown(
        """
        <link rel="icon" href="https://i.ibb.co/nqFLS5Kh/GMR.png" type="image/png"/>
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black">
        <meta name="apple-mobile-web-app-title" content="GMR">
        <link rel="apple-touch-icon" href="https://i.ibb.co/gzhq2Vm/gmr-180.png">
        """,
        unsafe_allow_html=True
    )