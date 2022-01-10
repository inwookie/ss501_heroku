import streamlit as st

def app():
    st.markdown("""
    # [Dent Detection]

    ### 1. Summarize 
    - 데이터셋 : 쏘카 파손 이미지 데이터셋    
    - 사용 모델 : Yolov5-ultralytics  
    - 학습 방법 : COCO Pre-trained 된 데이터를 fine-tuning  
    - 손실 함수 : BCEWithLogitsLoss + loss for bounding box regression  
    - 최적화 방법 : SGD  
    - 스케쥴러 : OneCycleLR  

    - Label setting :  [class, center_x, center_y, width, height]  
        - class 제외 0~1값이 되도록 세팅
        
    - True Positive : 36개  
    - False Positive 17개  
    - True Negative : 51개  


    ### 2. 결과 

    """)
    st.image('apps/dent_detection/img/dent_img_06.png')
    
    st.markdown("""
    ### 잘된 예시 
                """)
    st.image('apps/dent_detection/img/dent_img_01.jpg')
    st.image('apps/dent_detection/img/dent_img_05.jpg')
    
    st.markdown("""
    ### 잘못된 예시 
                """)
    st.image('apps/dent_detection/img/dent_img_02.jpg')
    st.image('apps/dent_detection/img/dent_img_03.jpg')
    
    
    