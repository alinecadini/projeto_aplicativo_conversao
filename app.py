import io
import pandas as pd
import streamlit as st
import openpyxl

def main():
    st.title("Conversor de Arquivo Excel para CSV")

    # Escolha da conversão
    opcao = st.selectbox("Conversão", ["Excel para CSV"])
    
    arquivo_carregado = st.file_uploader(f"Carregue seu arquivo {opcao.split()[0]}", type=["xlsx", "xls"])

    if arquivo_carregado is not None:
        try:
            # Ler o arquivo Excel em um DataFrame do pandas
            df = pd.read_excel(io.BytesIO(arquivo_carregado.read()))

            # Exibir uma pré-visualização básica
            st.write("Pré-visualização do DataFrame")
            st.dataframe(df.head())  # Exibir as primeiras linhas

            # Converter para CSV usando ";" como delimitador
            csv = df.to_csv(index=False, sep=';').encode("utf-8")
            st.download_button(
                label="Baixar CSV",
                data=csv,
                file_name="convertido.csv",
                mime="text/csv"
            )

        except Exception as e:
            st.error(f"Erro ao processar o arquivo: {e}")
    else:
        st.warning(f"Por favor, carregue um arquivo {opcao.split()[0]}.")

if __name__ == "__main__":
    main()