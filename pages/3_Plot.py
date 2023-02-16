import time
import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.colored_header import colored_header

colored_header(
    label="My First App",
    description="Plot graph example",
    color_name="blue-green-70",
)

## 設定網頁標題
#st.title('My First App')

# 加入網頁文字內容
st.write("By Oscar")

# 加入 pandas 資料表格
# Magic commands
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# 繪製折線圖
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

#繪製地圖
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [22.4, 114.2],
    columns=['lat', 'lon'])
st.map(map_data)

# 加入小工具
if st.checkbox('顯示地圖圖表'):
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [22.4, 114.2],
        columns=['lat', 'lon'])
    st.map(map_data)

option = st.sidebar.selectbox(
    '你喜歡哪種動物？',
    ['狗', '貓', '鸚鵡', '天竺鼠'])
'你的答案：', option
    # streamlit run app.py