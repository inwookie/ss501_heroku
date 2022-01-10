import streamlit as st


def app():
    st.write('🔺 네비게이션을 사용하여 페이지를 이동하세요. 🔺')
    st.title('What We Achieved')

#     used_car_prediction = '[🚗  차종 분류](https://share.streamlit.io/inwookie/ss501_ai_bootcamp_hackathon/main/app.py)'
#     st.markdown(used_car_prediction, unsafe_allow_html=True)
    st.markdown("""
    ### 🚗  차종 분류
    ### 🚓  번호판 인식
    - Streamlit Server에 Tesseract Upload 문제로 인하여 여기에 구현 되어 있는 버전은 Tesseract를 사용하지 않는 버전입니다. Tesseract를 사용하는 버전은 About Number Plate Detection 페이지에서 확인하실수 있습니다.    
    ### 🚐  파손 인식
    - Streamlit Server Memory 문제로 인하여 여기에 구현되어 있는 Scratch Detection은 기존 EfficientNet 모델 대신 MobileNet 모델을 사용하고 있습니다. EfficientNet 모델을 사용하는 버전은 About Scratch Detection 페이지에서 확인하실수 있습니다.
    ### 🚙  중고차 가격 예측   
    """)
