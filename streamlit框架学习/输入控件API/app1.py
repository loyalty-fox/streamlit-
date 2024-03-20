import streamlit as st
import time

# download_button(label, date, file_name) 下载按钮
# label:按钮上的标签，date：点击按钮后下载的数据，file_name：默认下载的文件名称
with open("E:/学习文件/综合/其他/壁纸/2.jpg", "rb") as file:
    st.download_button(
            label="Download image",
            data=file,
            file_name="cat.jpg"
        )
    
# file_uploader 文件上传按钮
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')