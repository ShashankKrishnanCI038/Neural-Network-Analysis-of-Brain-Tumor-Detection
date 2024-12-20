import streamlit as st
from PIL import Image

st.header("Get in Touch")

st.sidebar.header("Project Programmer")
profile = Image.open(r"programmer.jpg")
st.sidebar.image(profile, caption="Shashank Krishnan, AIML Engineer")

st.write("""
 **Neural Network Analysis of Brain Tumor** is a WebApp that is Developed by Shashank K, AIML Engineering graduate from Don Bosco Institute of Technology, Kumbalagodu.

 For Any Queries ragarding trained CNN Model and Datasets used for training:
    * Please do mail to shashank2002.shashu@gmail.com 
    * Ping me on +91 7829493269 via Whatsapp

""")