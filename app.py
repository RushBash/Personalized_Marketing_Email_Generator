import streamlit as st

st.title("This is my first application")
st.header("this is header")
st.subheader("this is Subheader")

text1=""""Streamlit is a promising open-source Python library, which enables developers to build attractive user interfaces in no time. Streamlit is the easiest way especially for people with no front-end knowledge to put their code into a web application: No front-end (html, js, css) experience or knowledge is required."""

st.write(text1)

st.toggle("Toggle")

st.radio("Radio",{"Button1", "Button2", "Button3"})

st.slider("slider", 0,1000, 20)

st.selectbox("select Box",{"India", "Pakistan", "England"})

st.text_input("text input")
st.text_area("this is text area")
st.checkbox("this is checkbox")

st.sidebar.title("this is sidebar")
st.sidebar.checkbox("this is sidebars checkbox")
st.sidebar.slider("this is sidebars slider")

st.button("Click button")

marks={"mayur":78,
       "anand":80,
       "adarsh":65,
       "shubham":100}
st.bar_chart(marks)
st.line_chart(marks)
 
st.file_uploader("upload a file")
