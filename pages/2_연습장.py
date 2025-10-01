import streamlit as st
import math as mt

tab1, tab2, tab3, tab4 = st.tabs(["메인화면", "기타", "바로가기", "정보 입력"])

with tab1:
    st.header("🎈 나의 새로운 앱")
    st.warning("2025년 10월 6일은 추석입니다")
    st.success("즐거운 추석 되세요!")
    st.image("https://gongu.copyright.or.kr/gongu/wrt/cmmn/wrtFileImageView.do?wrtSn=13297230&filePath=L2Rpc2sxL25ld2RhdGEvMjAyMS8yMS9DTFMxMDAwNC8xMzI5NzIzMF9XUlRfMjFfQ0xTMTAwMDRfMjAyMTEyMTNfMQ==&thumbAt=Y&thumbSe=b_tbumb&wrtTy=10004")

    st.markdown("---")

with tab2:
    st.title("근의 공식")
    st.latex(r"x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}")
    st.markdown("---")

    with st.expander("영상 및 오디오"):
        st.video("https://www.youtube.com/watch?v=B1J6Ou4q8vE")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

    # 지도 출력
    import pandas as pd
    with st.expander("위치"):
        df = pd.DataFrame({"lat": [37.4678448], "lon": [126.8118164]})
        st.map(df, zoom=12)

    st.code("""
    import streamlit as st
    st.title('Hello World')
    """, language="python")

with tab3:
    col1, col2, col3 = st.columns(3)  # 2개의 열 생성
    with col1:
        st.link_button("클래스룸", 'https://www.classroom.google.com')
    with col2:
        st.link_button("드라이브", 'https://www.drive.google.com')
    with col3:
        st.link_button("하이러닝", 'https://www.hi.goe.go.kr')

with tab4:
    #age = st.number_input("나이를 입력해 주세요!",step=1)
    #st.write(f"태어난 연도 : {2025-age+1}년")
    date = st.date_input("생년월일을 선택하세요")
    gender = st.radio("성별을 선택하세요", ["남성", "여성"])
    # 드롭다운에서 하나 선택
    color = st.selectbox("반을 선택하세요", ["1-1", "2-1", "3-1"])
    st.write("반:", color)

    level = st.slider("등급을 선택하세요", 1, 9, 5)
    image_data = st.camera_input("사진을 찍어보세요")
    if image_data:
        st.image(image_data)