import streamlit as st
import requests

# URL del servidor donde está desplegado el modelo
SERVER_URL = 'https://linear-model-service-carlosart17.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(x_value):
    try:
        predict_request = {'instances': [[x_value]]}
        response = requests.post(SERVER_URL, json=predict_request)
        response.raise_for_status()
        prediction = response.json()
        return prediction["predictions"][0][0]
    except Exception as e:
        st.error(f'Error al hacer la predicción: {str(e)}')
        return None

def main():
    # Agrega el archivo de estilo CSS
    st.markdown(
        '<style>' + open('styles.css').read() + '</style>', 
        unsafe_allow_html=True
    )

    st.title('Formula 2x + 1 = 11')

    # Ingresar el valor de x
    x_value = st.number_input('Ingrese el valor de x:')

    if st.button('Predecir'):
        # Hacer la predicción
        prediction = make_prediction(x_value)

        if prediction is not None:
            # Mostrar la predicción
            st.write(f'Para x = {x_value}, la predicción es: {prediction}')

if __name__ == '__main__':
    main()
