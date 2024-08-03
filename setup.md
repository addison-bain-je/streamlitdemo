# Setting up Streamlit

## Install Streamlit
1. Type this command in the terminal to install Streamlit:  
(I'm using PyCharm IDE)
```
pip install streamlit
```
![streamlit_1](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_1.png)

2. Test if installation works
```
streamlit hello
```
![streamlit_3](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_3.png)

3. How to run the Streamlit code
```
streamlit run file_name.py
```

## Display texts with Streamlit
![streamlit_4](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_4.png)

![streamlit_5](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_5.png)

```
# Text formats
st.title("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')
```

![streamlit_6](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_6.png)
![streamlit_7](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_7.png)

## Display an image, video or audio file with Streamlit
```
# Display image, video or audio file
st.image("kid.jpg")
st.audio("Audio.mp3")
st.video("video.mp4")
'''
```

## Display input widgets and controls
```
# Input widgets
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a color',['Red', 'Blue', 'Green'])
st.select_slider('Pick a mark',['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
```
![streamlit_9](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_9.png)

```
# Input widgets
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('Event start time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')
```
![streamlit_11](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_11.png)



## Display progress bar and status
```
# Display progress and status
st.subheader("Progress bar")
st.progress(10)

st.subheader("Pending execution")
with st.spinner('Wait for it...'):
    time.sleep(3)
```
![streamlit_12](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_12.png)


## Display status messages
```
st.success("Well done !")
st.error("Error found")
st.warning("Warning !!!")
st.info("This is for information only")
st.exception(RuntimeError("RuntimeError exception"))
```
![streamlit_13](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_13.png)


## Display Sidebar
```
st.sidebar.title("Text on the sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Select one",["Yes","No"])
```
![streamlit_14](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_14.png)


## Data Visualizations  

Histogram
```
# Data Visualization Histogram
rand = np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
```
![streamlit_15](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_15.png)


Line Chart
```
# Data Visualization Line Chart
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.line_chart(df)
```
![streamlit_16](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_16.png)


Bar Chart
```
# Data Visualization Bar Chart
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.bar_chart(df)
```
![streamlit_17](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_17.png)


Area Chart
```
# Data Visualization Area Chart
df = pd.DataFrame(np.random.randn(10, 2), columns=['x', 'y'])
st.area_chart(df)
```
![streamlit_18](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_18.png)


## Map Display
```
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)
```
![streamlit_19](https://github.com/addison-bain-je/streamlitdemo/blob/master/controls/streamlit_19.png)



--------------------------------------------------------------------   END  --------------------------------------------------------------------  

