import streamlit as st

st.title("Especialización Python for Analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Elena Loayza")

modulos = st.sidebar.selectbox("Selecione el módulo",["Listas","Arreglos","Funciones","POO"])

if modulos == "Listas":
  st.write("Te encuentras en el módulo de listas")

  valor_inicial = int(st.number_input("Ingrese tu valor inicial del rango", value=0))
  valor_final = int(st.number_input("]Ingrese tu valor inicial del rango",value=10))

  Lista = list(range(valor_inicial, valor_final)) 
  
elif modulos == "Arreglos":
  st.write("Te encuentras en el módulo de arreglos")

elif modulos == "Funciones":
   st.write("Te encuentras en el módulo de Funciones")

else:
   st.write("Te encuentras en el módulo de POO")
