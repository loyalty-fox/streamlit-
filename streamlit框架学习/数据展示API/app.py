import streamlit as st
import pandas as pd
import numpy as np

# 注意：write函数可以直接根据传入参数智能选择合适的打印函数
# st.write()可以打印多种格式和类型的对象，但可以传入多个变量。一般情况下，可以打印：
# 字符串
# Pandas表格
# 函数或模块介绍
# 字典或列表
# Matplotlib/Altair图表

# magic机制，可以在不调用任何 Streamlit 方法的情况下写入应用程序
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# title函数
st.title('应用的标题')

# header
st.header('应用内容的标题')

# subheader函数
st.subheader('应用内容的子标题')

# caption函数，用于标题、旁白、脚注、旁注和其他解释性文本
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

# markdown
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

# code 展示代码
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

# image 展示图片
url = "https://img2024.cnblogs.com/blog/1809841/202403/1809841-20240313132347219-13618990.jpg"
st.title('Display Image from URL')
st.markdown(f'<img src="{url}" alt="Image from URL" style="width:100%;">', unsafe_allow_html=True)

# text函数，将文本内容展示为等宽格式
st.text('This is some text.')

# table 将Pandas表格进行静态展示，不支持拖动和内容修改
df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

# metric，以粗体显示指标，并可选指示指标如何变化
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# json 将内容进行折叠展示
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})

# line_chart 将使用altair展示折线图，支持交互式拖拽、放大和缩小
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# map 绘制地图
df = pd.DataFrame({
    "col1": np.random.randn(1000) / 50 + 37.76,
    "col2": np.random.randn(1000) / 50 + -122.4,
    "col3": np.random.randn(1000) * 100,
    "col4": np.random.rand(1000, 4).tolist(),
})

st.map(df,
    latitude='col1',
    longitude='col2',
    size='col3',
    color='col4')