import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from PIL import Image
st.set_page_config(layout="wide")
from streamlit_autorefresh import st_autorefresh

# update every 5 seconds limited to 100 refreshes. add (limit=100) if required,
st_autorefresh(interval=15000, key="dataframerefresh")

#logo section and header title part.
header= st.sidebar.container()
with header:
    padding = 0
    st.markdown(f""" <style>reportview-container .main .block-container{{padding-top: {padding}rem;padding-right: {padding}rem;padding-left: {padding}rem;padding-bottom: {padding}rem;}} </style> """, unsafe_allow_html=True)
    img = Image.open("MicrosoftTeams-image.png")
    st.image(img, width=300)
title = '<h1 style="font-family:sans-serif; color:Red; font-size: 40px;">Line output and Worker Efficiency Monitoring</h1>'
st.markdown(title,unsafe_allow_html=True)
#adding new pages..

# load csv
df = pd.read_csv("rfid_punches.csv")
#st.dataframe(get_data())

var1 = st.selectbox('Select Floor', df['floor'].unique())
vala = len(df[df["floor"] == var1])
avg = round(vala/len(var1) * 10)

#make room for showing floor values
col1, col2, col3 = st.columns(3)

with col1:
    st.info("Total Production of "+str(var1))
    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = vala,
    mode = "gauge+number+delta",
    # title = {'text': "Speed"},
    delta = {'reference': 200},  
    gauge = {'axis': {'range': [None, 200]},
                'steps' : [
                    {'range': [0, 100], 'color': "lightgray"},
                    {'range': [100, 150], 'color': "gray"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 190}}))
    fig.update_layout(
                            autosize=False,
                            width=250,
                            height=150,
                            margin=dict(
                                        l=00,
                                        r=00,
                                        b=0,
                                        t=20,
                                        pad=4))

    st.plotly_chart(fig)
with col2:
    st.info("Average Production (in %) of "+str(var1))
    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = avg,
    mode = "gauge+number+delta",
    # title = {'text': "Speed"},
    delta = {'reference': 100},  
    gauge = {'axis': {'range': [None, 100]},
                'steps' : [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "gray"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}}))
    fig.update_layout(
                            autosize=False,
                            width=250,
                            height=150,
                            margin=dict(
                                        l=00,
                                        r=00,
                                        b=0,
                                        t=20,
                                        pad=4))

    st.plotly_chart(fig)
with col3:
    st.info("Productive Production of "+str(var1))
    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = vala-20,
    mode = "gauge+number+delta",
    # title = {'text': "Speed"},
    delta = {'reference': 100},  
    gauge = {'axis': {'range': [None, 100]},
                'steps' : [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "gray"}],
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}}))
    fig.update_layout(
                            autosize=False,
                            width=250,
                            height=150,
                            margin=dict(
                                        l=00,
                                        r=00,
                                        b=0,
                                        t=20,
                                        pad=4))

    st.plotly_chart(fig)

st.header("Workstation Performance Index")
l0, l1, l2, l3, l4, l5, l6, l7, l8 = st.columns(9)
with l0:
    st.write("Attributes")
with l1:
    bt1 = st.button("Line 1")
with l2:
    bt2 = st.button("Line 2")
with l3:
    bt3 = st.button("Line 3")
with l4:
    bt4 = st.button("Line 4")
with l5:
    bt5 = st.button("Line 5")
with l6:
    bt6 = st.button("Line 6")
with l7:
    bt7 = st.button("Line 7")
with l8:
    bt8 = st.button("Line 8")

t0, t1, t2, t3, t4, t5, t6, t7, t8 = st.columns(9)
with t0:
    st.write("Total Production")
with t1:
    amp1 = len(df[df['line'] == "Line 1"])
    if amp1 > 20:
        st.info(amp1)
    elif amp1 >= 10:
        st.warning(amp1)
    else:
        st.error(amp1)
    #st.info(len(df[df['line'] == "Line 1"]))
with t2:
    amp2 = len(df[df['line'] == "Line 2"])
    if amp2 > 20:
        st.info(amp2)
    elif amp2 >= 10:
        st.warning(amp2)
    else:
        st.error(amp2)
    #st.info(len(df[df['line'] == "Line 2"]))
with t3:
    amp3 = len(df[df['line'] == "Line 3"])
    if amp3 > 20:
        st.info(amp3)
    elif amp3 >= 10:
        st.warning(amp3)
    else:
        st.error(amp3)
    #st.info(len(df[df['line'] == "Line 3"]))
with t4:
    amp4 = len(df[df['line'] == "Line 4"])
    if amp4 > 20:
        st.info(amp4)
    elif amp4 >= 10:
        st.warning(amp4)
    else:
        st.error(amp4)
    #st.info(len(df[df['line'] == "Line 4"]))
with t5:
    amp5 = len(df[df['line'] == "Line 5"])
    if amp5 > 20:
        st.info(amp5)
    elif amp5 >=10:
        st.warning(amp5)
    else:
        st.error(amp5)
    #st.error(len(df[df['line'] == "Line 5"]))
with t6:
    amp6 = len(df[df['line'] == "Line 6"])
    if amp6 > 20:
        st.info(amp6)
    elif amp6 >= 10:
        st.warning(amp6)
    else:
        st.error(amp6)
    #st.error(len(df[df['line'] == "Line 6"]))
with t7:
    amp7 = len(df[df['line'] == "Line 7"])
    if amp7 > 20:
        st.info(amp7)
    elif amp7 >= 10:
        st.warning(amp7)
    else:
        st.error(amp7)
    #st.error(len(df[df['line'] == "Line 7"]))
with t8:
    amp8 = len(df[df['line'] == "Line 8"])
    if amp8 > 20:
        st.info(amp8)
    elif amp8 >=10:
        st.warning(amp8)
    else:
        st.error(amp8)
    #st.error(len(df[df['line'] == "Line 8"]))

a0, a1, a2, a3, a4, a5, a6, a7, a8 = st.columns(9)
with a0:
    st.write("Average Productivity")
with a1:
    ap1 = round(len(df[df["line"] == "Line 1"])/len(df['line'])*100)
    if ap1 >= 20:
        st.info(ap1)
    elif ap1 >= 10:
        st.warning(ap1)
    else:
        st.error(ap1)
    #st.info(round(len(df[df["line"] == "Line 1"])/len(df['line'])*100))
with a2:
    ap2 = round(len(df[df["line"] == "Line 2"])/len(df['line'])*100)
    if ap2 >= 20:
        st.info(ap2)
    elif ap2 >= 10:
        st.warning(ap2)
    else:
        st.error(ap2)
    #st.info(round(len(df[df["line"] == "Line 2"])/len(df['line'])*100))
with a3:
    ap3 = round(len(df[df["line"] == "Line 3"])/len(df['line'])*100)
    if ap1 >= 20:
        st.info(ap3)
    elif ap3 >= 10:
        st.warning(ap3)
    else:
        st.error(ap3)
    #st.info(round(len(df[df["line"] == "Line 3"])/len(df['line'])*100))
with a4:
    ap4 = round(len(df[df["line"] == "Line 4"])/len(df['line'])*100)
    if ap4 >= 20:
        st.info(ap4)
    elif ap4 >= 10:
        st.warning(ap4)
    else:
        st.error(ap4)
    #st.warning(round(len(df[df["line"] == "Line 4"])/len(df['line'])*100))
with a5:
    ap5 = round(len(df[df["line"] == "Line 5"])/len(df['line'])*100)
    if ap5 >= 20:
        st.info(ap5)
    elif ap5 >= 10:
        st.warning(ap5)
    else:
        st.error(ap5)
    #st.error(round(len(df[df["line"] == "Line 5"])/len(df['line'])*100))
with a6:
    ap6 = round(len(df[df["line"] == "Line 6"])/len(df['line'])*100)
    if ap6 >= 20:
        st.info(ap6)
    elif ap6 >= 10:
        st.warning(ap6)
    else:
        st.error(ap6)
    #st.error(round(len(df[df["line"] == "Line 6"])/len(df['line'])*100))
with a7:
    ap7 = round(len(df[df["line"] == "Line 7"])/len(df['line'])*100)
    if ap7 >= 20:
        st.info(ap7)
    elif ap7 >= 10:
        st.warning(ap7)
    else:
        st.error(ap7)
    #st.error(round(len(df[df["line"] == "Line 7"])/len(df['line'])*100))
with a8:
    ap8 = round(len(df[df["line"] == "Line 8"])/len(df['line'])*100)
    if ap8 >= 20:
        st.info(ap8)
    elif ap8 >= 10:
        st.warning(ap8)
    else:
        st.error(ap8)
    #st.error(round(len(df[df["line"] == "Line 8"])/len(df['line'])*100))

st.subheader("Analysis of Whole Work-Station")
value = (df["line"]).value_counts()
g=pd.DataFrame(value)
st.bar_chart(g, width=300, height=200)

if bt1:
    st.subheader("Analysis of Work-Station 1")
    value = (df["line"] == "Line 1").value_counts()
    g=pd.DataFrame(value)
    st.bar_chart(g, width=300, height=200)
if bt2:
    st.subheader("Analysis of Work-Station 2")
    value = (df["line"] == "Line 2").value_counts()
    g=pd.DataFrame(value)
    st.bar_chart(g, width=300, height=200)
if bt3:
    st.subheader("Analysis of Work-Station 3")
    value = (df["line"] == "Line 3").value_counts()
    g=pd.DataFrame(value)
    st.bar_chart(g, width=300, height=200)
if bt4:
    st.subheader("Analysis of Work-Station 4")
    value = (df["line"] == "Line 4").value_counts()
    g=pd.DataFrame(value)
    st.bar_chart(g, width=300, height=200)
if bt5:
    st.subheader("Analysis of Work-Station 5")
    value = (df["line"] == "Line 5").value_counts()
    g=pd.DataFrame(value)
    st.bar_chart(g, width=300, height=200)
if bt6:
    st.subheader("Analysis of Work-Station 6")
    value = (df["line"] == "Line 6").value_counts()
    g=pd.DataFrame(value)
    st.bar_chart(g, width=300, height=200)
if bt7:
    st.subheader("Analysis of Work-Station 7")
    value = (df["line"] == "Line 7").value_counts()
    g=pd.DataFrame(value)
    st.bar_chart(g, width=300, height=200)
if bt8:
    st.subheader("Analysis of Work-Station 8")
    value = (df["line"] == "Line 8").value_counts()
    g=pd.DataFrame(value)
    st.bar_chart(g, width=300, height=200)
