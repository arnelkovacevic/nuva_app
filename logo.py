import streamlit as st
import webbrowser

def show_logo():
    # Riga con immagine piccola in alto a sinistra
    st.markdown(
        """
        <div style='margin-top: -10px; margin-left: 55px;'>
            <img src='https://i.ibb.co/cK1skNcK/IMG-6318.png' width='20'/>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Riga con logo cliccabile e testo accanto
    cols = st.columns([1, 6])
    with cols[0]:
        if st.button("", key="gmr_logo_btn"):
            webbrowser.open_new_tab("https://gmr-inventario.app/login")
        st.markdown(
            """
            <style>
            button[data-testid="gmr_logo_btn"] {
                background-image: url('https://i.ibb.co/nqFLS5Kh/GMR.png');
                background-size: contain;
                background-repeat: no-repeat;
                background-position: center;
                width: 75px;
                height: 75px;
                border: none;
                padding: 0;
                margin: 0;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    with cols[1]:
        st.markdown("## gXLS - Reader")
    
    