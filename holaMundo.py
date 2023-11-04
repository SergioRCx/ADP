import streamlit as st
def main():
   st.title('¡Hola Mundo!')
    st.markdown(
        """
        <style>
        body {
            color: blue;
            background-color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.write('¡Bienvenido a mi aplicación!')
    st.write('Sergio RC')
if __name__ == '__main__':
    main()
