import streamlit as st
from PIL import Image

def app():
    st.markdown("""
    # [ Car Classification]

    ### 1. Summarize 
    - 데이터셋 : Stanford Car Dataset  
    - 사용 모델 : Efficient-b3 (활성 함수 : Mish)  
    - 학습 방법 : Imagenet Pre-trained 된 데이터를 fine-tuning    
    - 손실 함수 : LabelSmoothingLoss() - 추론을 잘못했을때 Penalty를 줄여주고 일반화에 도움을 준다.
    - 최적화 방법 : RAdam - 실험적 결과 - 학습 안정성을 높인다.  
    - 스케쥴러 : ReduceLROnPlateau 사용 - Validation 성능이 향상하지 않을 시 학습률 낮춘다.    

    ### 2. 실행 과정

    1. Original Image Dataset에 대하여 torchvison의 transforms를 사용한다 
    """)
    
    st.image('apps/car_classifier/img/car_classifier_img_0.png')
    
    st.markdown("""
        - Train 이미지 데이터에 Random Horizontal Flip, Random Rotation, 그리고 Resize를 적용한다. 
        - Test 이미지 데이터에는 Resize만 적용한다. 
        - 확인후 Mix Up Augmentation 기법을 적용하여 데이터와 라벨을 섞어 데이터를 생성해낸다. 
 
    2. Model 훈련 
        - Train Model 과 Eval Model 함수를 만들어 적용한다. 
        - Efficientnet-b3 모델을 불러와 LabelSmoothingLoss() 적용후 모델을 훈련시킨다.
    """)
    st.image('apps/car_classifier/img/car_classifier_img_1.png')
    st.image('apps/car_classifier/img/car_classifier_img_2.png')
    st.image('apps/car_classifier/img/car_classifier_img_4.png')
    
    st.markdown("""
    3. Model load 후 테스트 
    """)
    st.image('apps/car_classifier/img/car_classifier_img_3.png')
    
    st.markdown("""
    ### 3. Page 설명

    Image Upload -> Classify from the 196 Classes -> Output Prediction and Percentage -> Plot Top 5 Prediction and Percentage 

    """)