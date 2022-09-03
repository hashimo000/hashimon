import streamlit as st
import pandas as pd
import numpy as np
st.title("hashimotomizuki")
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