# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Text formats
st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

'''
# Display image, video or audio file
st.image("kid.jpg")
st.audio("Audio.mp3")
st.video("video.mp4")
'''
'''
# Input widgets
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a color',['Red', 'Blue', 'Green'])
st.select_slider('Pick a mark',['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)

# Input widgets
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('Event start time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
'''

# Display progress and status
st.subheader("Progress bar")
st.progress(10)

st.subheader("Pending execution")
with st.spinner('Wait for it...'):
    time.sleep(3)

# Messages
st.success("Well done !")
st.error("Error found")
st.warning("Warning !!!")
st.info("This is for information only")
st.exception(RuntimeError("RuntimeError exception"))


# Sidebar
st.sidebar.title("Text on the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Select one",["Yes","No"])

# Container
container = st.container()
container.write("This is inside the container")
st.write("This is outside the container")


# Data Visualization Histogram
rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)

# Data Visualization Line Chart
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)

# Data Visualization Bar Chart
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)

# Data Visualization Area Chart
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)


# Display maps
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/