import json
import streamlit as st
import requests

SERVER_URL = 'https://linear-model-service-carlosart17.cloud.okteto.net/v1/models/linear-model:predict'

def make_prediction(inputs):
    predict_request = {'instances': inputs}
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    prediction = response.json()
    return prediction

def main():
    st.title('Estimador de Tiempo de Desarrollo')

    code_size = st.number_input('Ingrese el numero de lineas de codigo:', min_value=0.0, step=1.0)

    if st.button('Predecir'):
        # Ajustar la entrada para que coincida con la nueva ecuación
        # En este caso, la entrada debe ser [2 * code_size + 1]
        inputs = [2 * code_size + 1]

        prediction = make_prediction(inputs)
        st.write(f'Tiempo estimado de desarrollo para un tamaño de código en horas de {code_size}: {prediction["predictions"][0][0]}')

if __name__ == '__main__':
    main()
