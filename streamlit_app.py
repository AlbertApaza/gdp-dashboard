import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title('Internet Consumption Dashboard - UPT')

# Subtitle
st.write("Monitoring internet consumption by laboratory at the Universidad Privada de Tacna")

# Generate example data for internet consumption
data = pd.DataFrame(
    np.random.randint(10, 100, size=(100, 3)),  # Generate random data between 10 and 100
    columns=['Laboratorio', 'Uso de Internet (MB)', 'Sesiones Activas']
)

# Add creative names for laboratories
laboratorios = ['Lab de Redes', 'Lab de Software', 'Lab de Electrónica', 'Lab de Inteligencia Artificial']
data['Laboratorio'] = np.random.choice(laboratorios, size=100)

# Display the complete data table
st.write("Generated Data:")
st.dataframe(data)

# Add a slider to filter data by internet usage
valor_seleccionado = st.slider('Select the minimum internet usage (MB) to filter:', 10, 100, 50)
st.write(f'Selected minimum internet usage: {valor_seleccionado} MB')

# Filter the data based on the selected value
data_filtrada = data[data['Uso de Internet (MB)'] >= valor_seleccionado]

# Display the filtered data table
st.write("Filtered Data by Internet Consumption:")
st.dataframe(data_filtrada)

# Create a line chart with filtered data
st.line_chart(data_filtrada.set_index('Laboratorio'))

# Create a bar chart with filtered data
st.bar_chart(data_filtrada.set_index('Laboratorio'))

# Add a button
if st.button('Update Dashboard'):
    st.write('Data updated!')
