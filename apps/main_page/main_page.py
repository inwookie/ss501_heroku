import streamlit as st


def app():
    st.write('๐บ ๋ค๋น๊ฒ์ด์์ ์ฌ์ฉํ์ฌ ํ์ด์ง๋ฅผ ์ด๋ํ์ธ์. ๐บ')
    st.title('What We Achieved')

#     used_car_prediction = '[๐  ์ฐจ์ข ๋ถ๋ฅ](https://share.streamlit.io/inwookie/ss501_ai_bootcamp_hackathon/main/app.py)'
#     st.markdown(used_car_prediction, unsafe_allow_html=True)
    st.markdown("""
    ### ๐  ์ฐจ์ข ๋ถ๋ฅ
    ### ๐  ๋ฒํธํ ์ธ์
    - Streamlit Server์ Tesseract Upload ๋ฌธ์ ๋ก ์ธํ์ฌ ์ฌ๊ธฐ์ ๊ตฌํ ๋์ด ์๋ ๋ฒ์ ์ Tesseract๋ฅผ ์ฌ์ฉํ์ง ์๋ ๋ฒ์ ์๋๋ค. Tesseract๋ฅผ ์ฌ์ฉํ๋ ๋ฒ์ ์ About Number Plate Detection ํ์ด์ง์์ ํ์ธํ์ค์ ์์ต๋๋ค.    
    ### ๐  ํ์ ์ธ์
    - Streamlit Server Memory ๋ฌธ์ ๋ก ์ธํ์ฌ ์ฌ๊ธฐ์ ๊ตฌํ๋์ด ์๋ Scratch Detection์ ๊ธฐ์กด EfficientNet ๋ชจ๋ธ ๋์  MobileNet ๋ชจ๋ธ์ ์ฌ์ฉํ๊ณ  ์์ต๋๋ค. EfficientNet ๋ชจ๋ธ์ ์ฌ์ฉํ๋ ๋ฒ์ ์ About Scratch Detection ํ์ด์ง์์ ํ์ธํ์ค์ ์์ต๋๋ค.
    ### ๐  ์ค๊ณ ์ฐจ ๊ฐ๊ฒฉ ์์ธก   
    """)
