import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Neural Network Analysis of Kidney Stone",
    page_icon="🏥"
)
# Set the background image
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_url}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function with your image URL or local path
set_background("https://live.staticflickr.com/7808/46142041874_dc975994de_h.jpg")

st.header("Get in Touch")

st.sidebar.header("Project Programmer")
profile = Image.open(r"C:\Users\SHASHANK K\PycharmProjects\Project Files\Brain Tumor Detection\Shashank K.jpg")
st.sidebar.image(profile, caption="Shashank Krishnan, AIML Engineer")

st.write("""
 **Neural Network Analysis of Brain Tumor** is a WebApp that is Developed by Shashank K, AIML Engineering graduate from Don Bosco Institute of Technology, Kumbalagodu.

 For Any Queries ragarding trained CNN Model and Datasets used for training:
    * Please do mail to shashank2002.shashu@gmail.com 
    * Ping me on +91 7829493269 via Whatsapp

""")