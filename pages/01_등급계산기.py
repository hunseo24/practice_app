import streamlit as st
import math as mt
import pandas as pd

st.title("내신용 5등급 계산기")
student = st.number_input("총인원수",step=1)

col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    rank = st.number_input("등수",step=1)
    if (rank != 0 and student != 0):
        mypercent = rank / student
        if mypercent <= 0.1:
            grade = 1
        elif mypercent <= 0.34:
            grade = 2
        elif mypercent <= 0.66: grade = 3
        elif mypercent <= 0.90: grade = 4
        elif mypercent <= 1: grade = 5
        else: grade = "error"

        st.write(f"{grade}등급")

with col2:
    st.dataframe(pd.DataFrame({
"등급": ["1", "2", "3", "4", "5"],
"인원수": [mt.floor(student*0.1),mt.floor(student*0.34)-mt.floor(student*0.1),mt.floor(student*0.66)-mt.floor(student*0.34),mt.floor(student*0.9)-mt.floor(student*0.66),student-mt.floor(student*0.9)],
"비율": ["10%", "24%","32%","24%","10%"],
"누적 비율": ["10%","34%","66%","90%","100%"]

}))