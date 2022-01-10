import streamlit as st
from PIL import Image

def app():
    st.markdown("""
    # [ Detection of Numplate ]

    ### 1. Summarize 
    - 가장 유명한 Edge 탐색 알고리즘 중 하나인 Canny Edge를 이용하여 Edge를 찾는다.
    - Original Image의 Gray에서 모든 불필요한 Edge를 제거할 수 있는 유일한 방법으로, 윤곽을 가장 잘 찾아내는 알고리즘이다.


    ### 2. 실행 과정

    1. Original Image에 대하여 Gray Image를 얻은 후, 다양한 filter 적용
    """)
    
    st.image('apps/ocr/img/ocr_img_0.png')
    
    st.markdown("""
        - Morphology Translate를 사용하여 fixel값을 대체한다. 전체적인 윤곽을 파악하고 작은 object를 제거한다.
        - Edge가 남아있는 상태에서 나머지를 Blurring하여 Edge검출에 용이한 Gaussian Blurring 사용한다.
    """)
    
    st.image('apps/ocr/img/ocr_img_1.png')
    
    st.markdown("""
    2. Double Thresholding 진행 (첫번째는 지금, 두번째는 Contouring 후)
        - image의 pixel값을 이진화 하기 위함.
        - OpenCV의 adaptiveThreshold 사용한다.

    3. Edge Trackig 검출
        - fixel값이 동일한 영역을 경계선으로 나타내는 contours를 이용해 번호판 숫자 검출.
        - OpenCV의 findcontours를 사용한다. (1단계)
    """)
    st.image('apps/ocr/img/ocr_img_2.png')
    
    st.markdown("""
        - 검출한 contours들에 대하여 OpenCV의 boundinRect를 이용해 해당 edge를 둘러싸는 사각형을 그린다.
        - 사각형 중, 일정한 크기와 간격, 구조를 가지며 인접 개수가 일정 갯수 이상인 번호판 contours들을 찾는다. (2단계) 
    """)
    st.image('apps/ocr/img/ocr_img_3.png')
    
    st.markdown("""
        - 사각형 배열을 찾은 후 시작점과 사각형 배열의 너비, 높이 등 조건을 통해 번호판 영역을 확정하고, Pytesserct-ocr을 이용하여
        번호판의 Text를 검출한다.
    """)
    st.image('apps/ocr/img/ocr_img_4.png')
    st.image('apps/ocr/img/ocr_img_5.png')
    st.image('apps/ocr/img/ocr_img_6.png')
    
    st.markdown("""
    4. Covering Numplate
        - Rectangle을 이용해 번호판 영역의 thickness를 -1로 설정하여, 기존 이미지에서 번호판 영역을 가림으로써 중고차 매매시 Image Upload를 용이하게 한다.
    """)
    st.image('apps/ocr/img/ocr_img_7.png')
    
    st.markdown("""
    ### 3. Page 설명

    Image Upload -> Original Image -> Numplate Crop한 Image -> Pytesseract로 OCR을 진행한 Result -> Numplate Covering 한 Image

    """)