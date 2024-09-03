import streamlit as st
# import pandas as pd
from PIL import Image


st.title("Test Audio Web App")

st.header("This is Sample Application")

st.subheader("Test")

st.markdown("Here we use to right just Text")

img = Image.open("myimage.jpeg")
st.image(img,
         caption="Aashiq shaw",
         width=400,
         channels="RGB"
         )
st.audio("gallan.mp3")

st.code(""" for x in range(1,5):
            print("Hello World")
            """)

# dataset = pd.read_csv("test.csv")
# st.dataframe(dataset)

name = st.text_input("Enter Your Name")
state = st.text_input("Enter Your State")
adr = st.text_area("Enter Your Address")
classNo = st.selectbox("Select your class from below lists ",(1,2,3,4,5))

button1 = st.button("Submit")
if button1 :
    st.markdown(f'''
            Name : {name}
            State : {state}
            Address : {adr}
            Class : {classNo}
            ''')