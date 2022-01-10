import streamlit as st
from multiapp import MultiApp
from apps.car_classifier import car_classifier, car_classifier_about
from apps.ocr import ocr_v2, ocr_about
from apps.main_page import main_page
from apps.scratch_segmentation import scratch_about, scratch
from apps.dent_detection import dent_about
from apps.used_car import used_car_prediction, used_car_prediction_about
from apps.team import about_us


app = MultiApp()

st.markdown("""
# SS501
""")

# Add all your application here
app.add_app("Home", main_page.app)
app.add_app("🚗  Car Classifier", car_classifier.app)
app.add_app("______About Car Classification", car_classifier_about.app)
app.add_app("🚓 Number Plate Detection", ocr_v2.app)
app.add_app("______About Number Plate Detection", ocr_about.app)
app.add_app("🚐  Scratch Detection", scratch.app)
app.add_app("______About Scratch Detection", scratch_about.app)
app.add_app("🚙 Used Car Price Prediction", used_car_prediction.app)
app.add_app("______About Used Car Price Prediction",
            used_car_prediction_about.app)
app.add_app("🚐  About Dent Detection", dent_about.app)
app.add_app("👩🏻‍💻🧑🏻‍💻 About Us", about_us.app)
# The main app
app.run()
