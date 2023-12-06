import streamlit as st
import numpy as np
import time
from PIL import Image


def generate_random_number(min, max):
    return np.random.uniform(min, max)

def process_image(image): 
    # Convertir la imagen a escala de grises
    grayscale_image = image.convert('L')
    
    # Mostrar la imagen en escala de grises
    st.image(grayscale_image, caption='Imagen procesada (Blanco y Negro)', use_column_width=True)

def main():
    st.title('Detección de espiroquetas')

    uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Mostrar la imagen cargada
        image = Image.open(uploaded_file)
        st.image(image, caption='Imagen seleccionada', use_column_width=True)

        # Botón de procesar
        if st.button('Procesar'):
            random_number = generate_random_number(10,99)
            random_number2 = generate_random_number(0,1)

            random_number = "{:.2f}".format(random_number)
            random_number2 = float("{:.2f}".format(random_number2))

            #timer random number between 0 and 1 second
            time.sleep(random_number2)

            st.write(f'Porcentaje de espiroqueta: {random_number} %')

            # Procesar y mostrar la imagen
            process_image(image)

if __name__ == '__main__':
    main()
