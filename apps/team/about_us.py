import streamlit as st

def app():
    st.title('Who We Are')

    # col1, col2, col3 = st.columns([1,6,1])

    # with col1:
    #     st.write("")

    # with col2:
    #     st.image('logo/ss501_logo.png')

    # with col3:
    #     st.write("")
    st.balloons()
    
    
    st.markdown("""
    ## Socar & Student 5 0 Likelions
    > 쏘카 해커톤 학생 다섯명이 멋쟁이 사자처럼!
    """)
    st.image('logo/ss501_logo.png')
    
    
    st.markdown("""
    #### 🧑🏻‍💻 철없는 팀장: **박웅규** [__차종 분류, 파손 인식__]
    #### 🧑🏻‍💻 열정 폭발: **백인욱** [__차종 분류, 웹/앱 개발__]
    #### 👩🏻‍💻 뛰어난 참여율: **김가영** [__번호판 인식, 웹 개발__]
    #### 👩🏻‍💻 아직도 학기중: **김수정** [__중고차 가격 예측, 웹 개발__]
    #### 🧑🏻‍💻 어디계세요?: **박준언** [__파손 인식 자료 조사__]
                """)
