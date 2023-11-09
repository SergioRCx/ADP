import streamlit as st

def main():
    st.markdown(
        """
        <style>
        body {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title('¡Hola Mundo!')
    st.write('<p style="font-size: 50px;color: aqua;">Sergio Alexis Romero Carreto</p>', unsafe_allow_html=True)
    st.write('<p style="font-size: 50px;color: aqua;">NC: 19091427</p>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()

