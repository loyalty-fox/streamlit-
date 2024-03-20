# streamlit-
streamlit前端框架学习

### (1)参考链接：

30天：[https://30days.streamlit.app/](https://30days.streamlit.app/)<br />官方文档：[https://docs.streamlit.io/library/api-reference](https://docs.streamlit.io/library/api-reference)<br />caggle文档：[无需前端技能 用Streamlit部署你的模型！](https://mp.weixin.qq.com/s/gWsg7pwfIYl9f7EVme888g)<br />一图流：[Cheat sheet - Streamlit Docs](https://docs.streamlit.io/library/cheatsheet)<br />打包发布：[https://share.streamlit.io/](https://share.streamlit.io/)
<a name="P9BI5"></a>

### (2)magic机制——write()函数：

即使用 _**streamlit run **_执行的脚本代码在遇到单行变量时，会自动调用st.write()函数，来展示该数据，而write()函数会根据数据类型自动选择合适的函数进行数据打印展示，具体支持的参数类型如下。比如遇到DateFrame格式的数据就会将其显示为表格。<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/32656219/1709088744197-d10a71c2-c930-472c-9ab6-09442c1bbfa6.png#averageHue=%23fefdfd&clientId=u3bd9cd77-fa7b-4&from=paste&height=719&id=uda545bd1&originHeight=1078&originWidth=969&originalType=binary&ratio=1.5&rotation=0&showTitle=false&size=124082&status=done&style=none&taskId=u998a78b9-3147-41f0-b502-625221ab9c6&title=&width=646)
<a name="eWSrd"></a>

### (3)theme——主题

保存在app.py同一路径下的.streamlit/config.toml文件中，格式为：

```
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#00008B"
textColor="#FFFFFF"
font="monospace"
```

其中backgroundColor为主要背景色，secondaryBackgroundColor为副背景色，textColor为字体色<br />相关工具链接：[颜色码选择器](https://htmlcolorcodes.com/)

<a name="U0Taq"></a>

### (4)secrets管理

用于在streamlit.io上发布app.py时管理不方便展示的数据（如大模型key）

1. 向准备发布的app添加secrets：[https://blog.streamlit.io/secrets-in-sharing-apps/](https://blog.streamlit.io/secrets-in-sharing-apps/)
2. 使用添加的密钥：[Secrets management - Streamlit Docs](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)
   <a name="qNhlC"></a>

### (5)form——表单数据提交

相关链接：[Batch Input Widgets | Introducing Submit Button & Forms](https://blog.streamlit.io/introducing-submit-button-and-forms/)

1. **st.form** 创建一个将内容组合起来的表单，并且带有一个 "Submit" 提交按钮。
2. **通常情况下，当用户与组件交互的时候，Streamlit 应用就会重新运行一遍。**
3. 表单是是一个视觉上将元素和组件编组的容器，并且应当包含一个提交按钮。在此之中，用户可以与一个或多个组件进行任意次交互都不会触发重新运行。直到最后提交按钮被按下时，所有表单内组件的数值会一次性更新并传给 Streamlit。
4. 你可以使用 with 语句来向表单对象添加内容（推荐），或者也可以将其作为一个对象直接调用其对象方法（即首先将表单组件存入一个变量，随后调用该变量的 Streamlit 方法）
   <a name="Zb0Tt"></a>

#### 关键：

- 所有form都应当包含一个 st.form_submit_button 对象
- st.button 和 st.download_button 将无法在表单中使用
- 表单能够出现在你应用的任何地方（包括侧边栏、列等等），唯独不能嵌入另一个表单之中
  <a name="h2Bac"></a>

#### 用法示例：

```python
import streamlit as st

st.title('st.form')

# Full example of using the with notation
st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. Example of object notation')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
```

<a name="RBndP"></a>

### (6)cache——缓存机制

st.cache 使得你可以**优化 Streamlit 应用的性能**。<br />Streamlit 提供了一个缓存机制，使你的应用即便是在从互联网加载数据、操作大数据集或者进行大开销的计算时仍可以保持高性能。这主要通过 @st.cache 装饰器来实现。<br />当你用 @st.cache 装饰器标记一个函数时，它将告诉 Streamlit 在该函数执行前需要做如下一些检查：

- **函数的输入参数是否发生了变化**
- **函数中使用的外部变量是否发生了变化**
- **函数的主体是否发生了变化**
- **函数中用到的所有函数的主体是否发生了变化**

如果以上任意一项不满足，即 Streamlit 第一次见到这四者的这种顺序组合时，它将会执行这个函数，并且**将结果存储于本地缓存中**。然后当下一次该带缓存的函数被调用时，如果以上四项均未发生改变，则 Streamlit **会直接跳过函数执行，而直接从缓存中调用先前的结果并返回**。<br />Streamlit 通过哈希散列来追踪这些条件的变化。你可以把缓存当成一种存储在内存之中的键值对结构，其中上述四项总和的哈希值为键，以函数实际返回的引用为值。
<a name="ocNt4"></a>

#### 示例代码

```python
import streamlit as st

@st.cache
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data

d1 = fetch_and_clean_data(DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

d2 = fetch_and_clean_data(DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the data in d1 is the same as in d2.

d3 = fetch_and_clean_data(DATA_URL_2)
# This is a different URL, so the function executes.
```

<a name="G4X5N"></a>

#### 相关链接：

[https://30days.streamlit.app/?challenge=Day24](https://30days.streamlit.app/?challenge=Day24)<br />[st.cache - Streamlit Docs](https://docs.streamlit.io/library/api-reference/performance/st.cache)<br />[Caching - Streamlit Docs](https://docs.streamlit.io/library/advanced-features/caching)
<a name="ZEXxQ"></a>

#### 安全性

st.cache隐式使用该**pickle模块**，已知该模块是不安全的。缓存函数返回的任何内容都会被腌制并存储，然后在检索时取消腌制。确保缓存的函数返回可信值，因为有可能构建恶意的 pickle 数据，这些数据将在 unpickling 期间执行任意代码。切勿在不安全模式下加载可能来自不受信任来源或可能已被篡改的数据。仅加载您信任的数据。
<a name="Ye5xe"></a>

### (7)session_state——会话管理（常用，关键）

用于在每一次会话（session）后保留中间变量，而不是全部清除，可以保证不同页面之间的衔接，让app具备状态。<br />我们将通过一个浏览器标签页访问 Streamlit 应用定义为一个会话（Session）。每个连接至 Streamlit 服务器的标签页都将创建一个会话。每当你与应用中组件交互时，Streamlit 将从上到下地重新运行整个应用。每次重新运行都将会清空历史：没有变量将被保留下来。<br />而会话状态（Session State）是一个在同一会话的不同次重新运行间共享变量的方法。除了能够存储和保留状态，Streamlit 还提供了使用回调函数更改状态的支持。
<a name="VrxV3"></a>

#### 示例代码：

```python
import streamlit as st

st.title('st.session_state')

def lbs_to_kg():
  st.session_state.kg = st.session_state.lbs/2.2046
def kg_to_lbs():
  st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
  pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
  kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)
```

<a name="d5G3K"></a>

#### 相关链接：

[Add statefulness to apps - Streamlit Docs](https://docs.streamlit.io/library/advanced-features/session-state)<br />[Session State - Streamlit Docs](https://docs.streamlit.io/library/api-reference/session-state)
<a name="nvEVK"></a>

### (8)相关练手项目

<a name="ynX4C"></a>

#### 1.**使用 Hugging Face 和 Streamlit 搭建一个零样本学习文本分类器**

[https://30days.streamlit.app/?challenge=Day29](https://30days.streamlit.app/?challenge=Day29)<br />[How to create a zero-shot learning text classifier using Hugging Face & Streamlit!](https://www.charlywargnier.com/post/how-to-create-a-zero-shot-learning-text-classifier-using-hugging-face-and-streamlit)
<a name="pAPZo"></a>

#### 2.访问到 YouTube 视频的缩略图

[https://30days.streamlit.app/?challenge=Day30](https://30days.streamlit.app/?challenge=Day30)
