import streamlit as st
import pandas as pd
import seaborn as sns
def main():
    st.title('¡Hola Mundooo!')
    st.write('Sergio RC')
    df=pd.read_csv('/content/drive/MyDrive/auto_mpg_data_tvs.txt',sep='\t',header=0)
    df
    corrSp=df [['mpg','weight','acceleration']].corr(method='spearman')
    
    st.pyplot(sns.heatmap(corrSp, annot=True,cmap='viridis'))

if __name__ == '__main__':
    main()
