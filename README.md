# Vehicle Data Explorer 

Esta aplicación web permite explorar datos de anuncios de autos usados en EE.UU. mediante visualizaciones interactivas.

## Funcionalidad

- Visualización de histogramas de kilometraje (`odometer`).
- Gráfico de dispersión entre variables seleccionadas.
- Interactividad a través de botones o casillas de verificación usando **Streamlit**.
- Análisis exploratorio básico de datos (`EDA`) con **Plotly Express** y **Pandas**.

## Tecnologías utilizadas
- Python
- Streamlit
- Plotly Express
- Pandas

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/<tu-usuario>/<tu-repositorio>.git
   ```bash
2.python -m venv .venv
.\.venv\Scripts\activate
   ```bash
pip install -r requirements.txt
   ```bash
streamlit run app.py