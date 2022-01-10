import streamlit as st

def app():
    st.markdown("""
    # [Scratch Semantic Segmentation]

    ### 1. Summarize 
    - 데이터셋 : 쏘카 파손 이미지 데이터셋  
    - 사용 모델 : Efficient-b7  
    - 학습 방법 : Imagenet Pre-trained 된 데이터를 fine-tuning 한다
    - 손실 함수 : Focal Loss - Data imbalance 문제 해결을 위해 사용하고 Edge에 더 집중하도록 Loss를 수정 한다
    - 최적화 방법 : Adam  
    - 스케쥴러 : StepLR 사용 - 10epoch 이후 1/10 으로 LR 조정 한다. 
    - 후처리 1 : mIoU를 높이기 위해 CRF와 Threshold 방법 실험 - Threshold 방법이 더 효과적  
    - 후처리 2 : 사용자에게 파손 위치를 쉽게 알려주기 위한 Bounding Box     
        - output 결과에 Labeling을 통해 Bounding box 위치를 찾고 이미지에 Draw  


    ### 2. 실행 과정

    1. Dataset 준비 
        - Scratch 이미지와 그에 해당하는 Mask 이미지를 Load 한다. 
        - Mask 이미지들에 대해서는 3차원으로 구성되어 있고 Mask 이미지들을 Label로 사용하기 위해 변환한다. 
    """)

    st.markdown("""
    ### Scratch Image 
    """) 
    st.image('apps/scratch_segmentation/img/scratch_detection_img_0.jpg')
    st.markdown("""
    ### Mask Image
    """) 
    st.image('apps/scratch_segmentation/img/scratch_detection_img_1.jpg')
    
    st.markdown("""
    2. Image Augmentation 과정 
        - Image Augmentation 기법을 사용하여 Random Horizontal Flip, Vertial Flip, Color Jitter, Resize등을 해준다. 
        - OpenCV의 adaptiveThreshold 사용한다.

    3. 모델 학습 
        - Pytorch의 Segmentation 모델들 중 Unet을 불러온다. 
        - Encoder_name은 Efficientnet-b7으로 Encoder_weights은 imagenet으로 in_channels은 3으로 classes은 2로 설정한다.
        - Trainer Class 정의후 Fine-tuning을 해준다. 
    """)
    st.markdown("""
    ### 첫번째 Epoch 
    """) 
    st.image('apps/scratch_segmentation/img/scratch_detection_img_2.png')
    st.markdown("""
    ### 14번째 (마지막) Epoch 
    """) 
    st.image('apps/scratch_segmentation/img/scratch_detection_img_3.png')
    st.markdown("""
    ### 14번째 (마지막) Epoch Graph  
    """) 
    st.image('apps/scratch_segmentation/img/scratch_detection_img_4.png')
    
    st.markdown("""
    4. Scratch Detection 
        - Model을 Load후 테스트 해본다. 
    ### Original Image  
    """) 
    st.image('apps/scratch_segmentation/img/scratch_detection_img_5.jpg')
    st.markdown("""
    ### Scratch Detected Image  
    """) 
    st.image('apps/scratch_segmentation/img/scratch_detection_img_6.png')
    
    st.markdown("""
    ### 3. Page 설명

    Image Upload -> Original Image -> Scratch Semantic Segmentation 진행 -> Scratch 찾은후 Bordering 진행 -> Scratch Detected Image 

    """)