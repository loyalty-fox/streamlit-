import streamlit as st

# radio 多选按钮
genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

# selectbox 下拉选项
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

st.write('You selected:', option)

# multiselect 多选下拉选项
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
)

st.write('You selected:', options)

# slider 滑动数值条
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# select_slider 列表滑动条
color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

# text_input 单行文本输入
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

# text_area 多行文本输入
txt = st.text_area('Text to input')
st.write('Your input:', txt)

# number_input 数字输入
number = st.number_input('Insert a number')
st.write('The current number is ', number)

