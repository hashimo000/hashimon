import streamlit as st
import pandas as pd
import numpy as np
st.title("sorcetree")
st.write("こんにちは！")
"""
#ありがとう
##こんにちは
###こんばんは
"""
df = pd.DataFrame({
"1st":[1,2,3,4],
"2nd":[10,11,12,13]
})
st.dataframe(df,width=300,height=300)

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
)
st.line_chart(chart_data)

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [34.6,135.5],
    columns=["lat","lon"]
)
st.map(df)
import streamlit as st
from PIL import Image
import numpy as np
uploaded_file = st.file_uploader("ファイルアップロード", type='jpg')
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    img_array = np.array(image)
else:
    st.write("ファイルがアップロードされていません")
button1 = st.button("押してください")
if button1 == True :
    st.image(img_array,caption = 'サムネイル画像',use_column_width = True)
else:
    st.write("")

st.write('Interactive Widget')

text = st.sidebar.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text
condition = st.sidebar.slider('あなたの今の調子は？',0,10,5)
'コンディション:',condition

left_colum, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右コラム')

expander1=st.beta_expander('問い合わせ１')
expander1.write('問い合わせ１の回答')
expander2=st.beta_expander('問い合わせ２')
expander2.write('問い合わせ２の回答')
expander3=st.beta_expander('問い合わせ３')
expander3.write('問い合わせ３の回答')