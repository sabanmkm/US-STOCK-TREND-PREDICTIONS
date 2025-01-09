import streamlit as st
import pickle
import numpy as np


def main():
    st.markdown(
        "<h1 style='text-align: center; font-family: Arial, sans-serif; font-size: 35px; color: white;'>PREDICT TREND</h1>",
        unsafe_allow_html=True)

    crp = st.selectbox("Select Pair", ["S&P 500", "Dow Jones Industrial Average", "Nasdaq Composite",
                                       "Russell 2000", "FTSE 100 (UK)", "DAX (Germany)"])


    ope = float(st.text_input("Enter Open Price ", "0"))
    hig = float(st.text_input("Enter Highest Price ", "0"))
    low = float(st.text_input("Enter Lowest Price ", "0"))
    cl = float(st.text_input("Enter Closing Price ", "0"))
    vlm = float(st.text_input("Enter Volume ", "0"))

    features = np.array([[ope, hig, low, cl, vlm]])

    if crp == 'S&P 500':
        model = pickle.load(open('model_0(GSPC).sav', 'rb'))
        scaler = pickle.load(open('scaler_0snp.sav', 'rb'))
    elif crp == 'Dow Jones Industrial Average':
        model = pickle.load(open('model_1(DJI).sav', 'rb'))
        scaler = pickle.load(open('scaler_1dow.sav', 'rb'))
    elif crp == 'Nasdaq Composite':
        model = pickle.load(open('model_2(IXIC).sav', 'rb'))
        scaler = pickle.load(open('scaler_2nas.sav', 'rb'))
    elif crp == 'Russell 2000':
        model = pickle.load(open('model_3(RUT).sav', 'rb'))
        scaler = pickle.load(open('scaler_3rus.sav', 'rb'))
    elif crp == 'FTSE 100 (UK)':
        model = pickle.load(open('model_4(FTSE).sav', 'rb'))
        scaler = pickle.load(open('scaler_4fts.sav', 'rb'))
    elif crp == 'DAX (Germany)':
        model = pickle.load(open('model_5(GDAXI).sav', 'rb'))
        scaler = pickle.load(open('scaler_5dax.sav', 'rb'))

    if model and scaler:
        pred = st.button("PREDICT")
        if pred:
            features1 = scaler.transform(features)
            result = model.predict(features1)

            if result == 0:
                st.markdown("""
                        <div style='text-align: center; font-family: Arial, sans-serif; font-size: 20px; color: white; background-color: red; padding: 10px; border-radius: 5px; display: inline-block;'>
                            <strong>DOWN</strong>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown("""
                        <div style='text-align: center; font-family: Arial, sans-serif; font-size: 20px; color: white; background-color: green; padding: 10px; border-radius: 5px; display: inline-block;'>
                            <strong>UP</strong>
                        </div>
                    """, unsafe_allow_html=True)

            st.warning(
                "⚠️ Please note: The predictions provided by this app are based on historical data and machine learning. They do not guarantee future price movements.")


if __name__ == "__main__":
    main()
