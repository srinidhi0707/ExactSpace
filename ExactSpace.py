import streamlit as st
import pandas as pd
import requests
import json
import time
from datetime import datetime
import plotly.graph_objects as go

st.set_page_config(page_title ="ExactSpace",page_icon="☁️",initial_sidebar_state="expanded",layout="wide")

URL = "http://www.balajiravi.duckdns.org/api/data/new"
getData= requests.get(url=URL)
data = getData.json()
df = pd.DataFrame(columns=["Id","User","Data","Updated_Data","Time"])
for i in range(0 ,len(data)):
        currentItem = data[i]
        df.loc[i] = [data[i]["id"],data[i]["name"],data[i]["data"],data[i]["change_data"],data[i]["time"]]

df['Date'] = df['Time'].apply(lambda x : x[:10])
df['Date'] = df['Date'].astype(str)
df['Time'] = df['Time'].apply(lambda x : x[12:16])
df = df[['Id','User','Data','Updated_Data','Date','Time']] 
metaData = df 
html_temp = """
<center><img src="https://s3.ap-south-1.amazonaws.com/prod-gti/companies_logos/7039653.png" width="205" height="137" class="">
<div style="background-color:olivedrab;padding:10px">
<h1 style="color:white;text-align:center;"> Dashboard</h1>
</div>
"""
 
import base64

main_bg = "backgroud.jpg"
main_bg_ext = "jpg"

side_bg = "backgroud.jpg"
side_bg_ext = "jpg"

st.markdown(
f"""
<style>
.reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
st.markdown(html_temp,unsafe_allow_html=True)
# st.sidebar.title("ExactSpace")
# ip = st.sidebar.text_input("USER","")
# calendar_ip = st.sidebar.date_input('DATE')
# calendar_ip = str(calendar_ip.strftime("%Y-%m-%d"))
# time_hr_ip = st.sidebar.selectbox("HOUR",['1', '2', '3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24'])
# time_min_ip = st.sidebar.slider("MINUTES", 1, 59)
# filterData = metaData[(df['Date'] == calendar_ip) & (df['User'] == ip) & (df['Time'].apply(lambda x : x[:1]) == time_hr_ip)]
dat=df.iloc[::-1]
fig = go.Figure(data=[go.Table(
    columnwidth = [5,17,100,90,20,10],
    header=dict(values=list(dat.columns),
                fill_color='olivedrab',
                align='left'),
    cells=dict(values=[dat.Id, dat.User, dat.Data, dat.Updated_Data,dat.Date,dat.Time],
               fill_color='lavender',
               align='left'))
])
fig.update_layout(width=1330, height=800)

st.write(fig)
# st.dataframe(df)