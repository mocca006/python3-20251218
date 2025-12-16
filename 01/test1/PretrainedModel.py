import streamlit as st 
import numpy as np  
import pandas as pd  
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from skimage import io
from skimage.transform import resize
from PIL import Image

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('./style.css')


def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image

def predict(model, image1, target):
    # image2 = io.imread(image1)    
    image2 = Image.open(image1)
    image = prepare_image(image2, target)
    # print(image.shape)    
    
    preds = model.predict(image)
    results = imagenet_utils.decode_predictions(preds) #, top=1000)
    df = pd.DataFrame()
    for (imagenetID, label, prob) in results[0]:
        df = pd.concat((df, pd.DataFrame({"label": [label], "probability": [float(prob)]})), ignore_index=True)
    return df

def load_model():
    # load the pre-trained model
    return ResNet50(weights="imagenet")

model = load_model()

st.title("1000種物件辨識")

uploaded_file = st.file_uploader("上傳圖片('.png, .jpg)", type=['png', 'jpg'])
if uploaded_file is not None:
    st.write("predict...")
    predictions = predict(model, uploaded_file, (224, 224))
    col1, col2 = st.columns(2)
    col1.image(uploaded_file, use_column_width=True)
    col2.write('### 預測結果：')
    col2.write(predictions)
    
