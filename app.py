import streamlit as st
from PIL import Image

st.title("Leopard App")

# Sidebar for image adjustments
st.sidebar.header("Image Settings")
image_width = st.sidebar.slider("Adjust Image Width", min_value=100, max_value=800, value=400, key='image_width')
image_height = st.sidebar.slider("Adjust Image Height", min_value=100, max_value=800, value=400, key='image_height')

# Load and resize the image
image = Image.open("leo.jpg")
resized_image = image.resize((image_width, image_height))
st.image(resized_image, caption='Leopard Image')

# Sidebar for video adjustments


st.subheader("Leopard Video")

# Video display
Video1 = open("leo.mp4", "rb")
st.video(Video1)
