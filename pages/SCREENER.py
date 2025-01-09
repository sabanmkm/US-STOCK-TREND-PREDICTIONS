import streamlit as st
import datetime
import yfinance as yf
import plotly_express as px

def main():
    st.markdown("<h1 style='text-align: center;"
                "font-family: Arial, sans-serif;"
                " font-size: 35px;"
                " ;color: white;'>US STOCKS DETAILS</h1>",
                unsafe_allow_html=True)

    s = st.selectbox("select pair", ["S&P 500", "Dow Jones Industrial Average", "Nasdaq Composite", "Russell 2000",
                                       "FTSE 100 (UK)", "DAX (Germany)"])
    std = st.date_input("ENTER DATE FROM", datetime.date(2002, 7, 6))
    etd = st.date_input("ENTER DATE UPTO", datetime.date(2024, 7, 6))
    if s == 'S&P 500':
        df = yf.download('^GSPC', start=std, end=etd)
        df
    if s == 'Dow Jones Industrial Average':
        df = yf.download('^DJI', start=std, end=etd)
        df
    if s == 'Nasdaq Composite':
        df = yf.download('^IXIC', start=std, end=etd)
        df
    if s == 'Russell 2000':
        df = yf.download('^RUT', start=std, end=etd)
        df
    if s == 'FTSE 100 (UK)':
        df = yf.download('^FTSE', start=std, end=etd)
        df
    if s == 'DAX (Germany)':
        df = yf.download('^GDAXI', start=std, end=etd)
        df
    fig = px.line(df, x=df.index, y=df['Adj Close'], title=s)
    st.plotly_chart(fig)


main()










