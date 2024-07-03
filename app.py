# import os
# import keras
# from keras.models import load_model
# import streamlit as st
# import tensorflow as tf

# st.header('Flower Classfication CNN Model')
# flower_name = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

# model= load_model('Flower_Recog_Model.h5')

# def classify_images(image_path):
#     input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
#     input_image_array = tf.keras.utils.img_to_array(input_image)
#     input_image_exp_dim = tf.expand_dims(input_image_array,0)

#     predictions = model.predict(input_image_exp_dim)
#     result = tf.nn.softmax(predictions[0])
#     outcome = 'The Image belongs to ' + flower_names[np.argmax(result)] + ' with a score of '+ str(np.max(result)*100)
#     return outcome

# uploaded_file = st.file_uploader('Upload an Image')
# if uploaded_file is not None:
#     with open(os.path.join('upload',uploaded_file.name), 'wb') as f:
#         f.write(uploaded_file.getbuffer())

# -----------------------------------------------------------------------
import os
import keras
from keras.models import load_model
import streamlit as st 
import tensorflow as tf
import numpy as np

st.header('Flower Classification CNN Model')
flower_names = ['Lotus', 'daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
# flower_names = ['Lotus', 'Orchid', 'daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

model = load_model('Flower_Recog_Model.keras')

def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array, 0)

    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    max_confidence = np.max(result) * 100

    if max_confidence >= 75:
        outcome = 'The image belongs to ' + flower_names[np.argmax(result)] + ' with a score of ' + str(max_confidence)
    else:
        outcome = 'Image NOT belong to Flower'

    return outcome

uploaded_file = st.file_uploader('Upload an Image')
if uploaded_file is not None:
    with open(os.path.join('upload', uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(uploaded_file, width = 200)

    st.markdown(classify_images(uploaded_file))

# ---------------------------------------------------------------------

# import os
# import keras
# from keras.models import load_model
# import streamlit as st 
# import tensorflow as tf
# import numpy as np

# # Function to perform user authentication
# def authenticate(username, password):
#     # Replace this with your actual authentication logic
#     if username == "admin" and password == "password":
#         return True
#     else:
#         return False

# # Function to display the login page
# def login_page():
#     st.title("Login")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     login_button = st.button("Login")
#     if login_button:
#         if authenticate(username, password):
#             st.success("Login successful!")
#             return True
#         else:
#             st.error("Invalid username or password")
#     return False

# #Main function
# def main():
#     if not login_page():
#         return

#     st.header('Flower Classification CNN Model')
#     flower_names = ['Lotus', 'daisy', 'dandelion', 'rose', 'sunflower', 'tulip']

#     model = load_model('Flower_Recog_Model.keras')

#     def classify_images(image_path):
#         input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
#         input_image_array = tf.keras.utils.img_to_array(input_image)
#         input_image_exp_dim = tf.expand_dims(input_image_array, 0)

#         predictions = model.predict(input_image_exp_dim)
#         result = tf.nn.softmax(predictions[0])
#         max_confidence = np.max(result) * 100

#         if max_confidence >= 75:
#             outcome = 'The image belongs to ' + flower_names[np.argmax(result)] + ' with a score of ' + str(max_confidence)
#         else:
#             outcome = 'Image not found'

#         return outcome

#     uploaded_file = st.file_uploader('Upload an Image')
#     if uploaded_file is not None:
#         with open(os.path.join('upload', uploaded_file.name), 'wb') as f:
#             f.write(uploaded_file.getbuffer())
        
#         st.image(uploaded_file, width = 200)

#         st.markdown(classify_images(uploaded_file))

# if __name__ == "__main__":
#     main()

