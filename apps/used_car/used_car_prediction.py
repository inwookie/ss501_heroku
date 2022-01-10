import streamlit as st
import torch
import pandas as pd


def app():
    @st.cache(allow_output_mutation=True, ttl=3600)
    def load_model():
        model = torch.load('linear.pt', map_location=torch.device('cpu'))
        return model

    with st.spinner('Model is being loaded..'):
        model = load_model()

    st.write("""
            # Predicting the price of used cars
            ### 중고차 가격 예측하기
            """
             )

    # csv 파일 불러오기
    data = pd.read_csv(r'Edited_Trim_table.csv')
    used_car = data.copy()

    used_car['Year'] = used_car['Year'].astype(str)
    used_car['Genmodel'] = used_car['Genmodel'].astype(str)
    used_car['Genmodel'] = used_car['Genmodel'].str.capitalize()

    def get_options(x):
        a = list(set(list(x)))
        a.sort()
        return tuple(a)

    Maker = st.selectbox('Please select a maker',
                         get_options(used_car['Maker']))

    Genmodel = st.selectbox('Please select a genmodel',
                            get_options(used_car[(used_car['Maker'] == Maker)]['Genmodel']))

    Year = st.selectbox('Please select a year',
                        get_options(used_car[(used_car['Genmodel'] == Genmodel)]['Year']))

    Entry_price = int(used_car[(used_car['Maker'] == Maker) & (
        used_car['Genmodel'] == Genmodel) & (used_car['Year'] == Year)]['Entry_price'].head(1))
    price = int(used_car[(used_car['Maker'] == Maker) & (
        used_car['Genmodel'] == Genmodel) & (used_car['Year'] == Year)]['Price'].head(1))

    def import_and_predict(Entry_price, model):
        y_pred = model.predict([[Entry_price]])[0]
        return round(y_pred)

    prediction = import_and_predict(Entry_price, model)
    pound_to_won = 1628.21
    prediction_to_won = prediction * pound_to_won
    price_to_won = price * pound_to_won

    st.write(f'Prediction in Pound: {prediction} £')
    st.write(f'Price in Pound: {price} £')

    st.write(f'Prediction in Won: {int(prediction_to_won / 10000)} 만원')
    st.write(f'Price in Won: {int(price_to_won / 10000)} 만원')
    st.write(
        f'Difference in Won: {int((prediction_to_won-price_to_won) / 10000)} 만원')
