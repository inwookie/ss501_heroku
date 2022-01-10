import streamlit as st

def app():
    st.markdown("""
    # [Dent Detection]

    ### 1. Summarize 
    - 데이터셋 : DVM-CAR Dataset & 100,000 UK Used Car Dataset 
    - 사용 모델 : Linear Regression   

    ### 2. 결과 

    """)
    st.image('apps/used_car/img/used_car_img_0.png')
    
    st.markdown("""
    ### 잘된 예시 
                """)
    st.image('apps/used_car/img/used_car_img_2.png')
    
    st.markdown("""
    ### 잘못된 예시 
                """)
    st.image('apps/used_car/img/used_car_img_1.png')
    
    
    
    