import streamlit as st

def main():
    st.title('¡Hola Mundo!')
    st.markdown(
        """
        <style>
        body {
            text-align: center;
            color: aqua;
            font-size: 50px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.write('Sergio Alexis Romero Carreto')
    st.write('NC: 19091427')
#text-align: center;
#color: aqua;
#font-size: 50px;
if __name__ == '__main__':
    main()

