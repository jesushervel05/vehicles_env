import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.title('Análisis de datos de vehículos')

st.write("Selecciona si quieres usar **botones** o **casillas de verificación** para mostrar los gráficos.")

# --- OPCIÓN 1: CON BOTONES ---
st.subheader('Opción 1: Usando botones')

# Crear botones
hist_button = st.button('Construir histograma')
scatter_button = st.button('Construir gráfico de dispersión')

# Histograma con botón
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión con botón
if scatter_button:
    st.write('Creación de un gráfico de dispersión entre odometer y price')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


# --- SEPARADOR VISUAL ---
st.markdown("---")

# --- OPCIÓN 2: CON CASILLAS DE VERIFICACIÓN ---
st.subheader('Opción 2: Usando casillas de verificación')

# Casillas
show_hist = st.checkbox('Mostrar histograma de odometer')
show_scatter = st.checkbox('Mostrar gráfico de dispersión (odometer vs price)')

# Histograma con checkbox
if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión con checkbox
if show_scatter:
    st.write('Creación de un gráfico de dispersión entre odometer y price')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)