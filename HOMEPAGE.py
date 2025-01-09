import streamlit as st

def main():
    st.set_page_config(
        page_title="Multi-Page Stock Price Prediction"
    )

    st.markdown("""
       <style>
        .main {
            background-color: black;
        }
       h1 {
           color: #1E90FF;  /* Dodger Blue for headings */
       }
       h3 {
           color: #32CD32;  /* Lime Green for subheadings */
       }
       .stMarkdown p {
           color: #000080;  /* Navy blue for regular text */
           font-size: 16px;
       }
       .stSidebar {
           background-color: reds;
       }
       .sidebar-content {
           color: #4B0082;  /* Indigo text in the sidebar */
       }
       </style>
       """, unsafe_allow_html=True)

    st.markdown(
    """
    # Welcome to the Stock Price Prediction App!

    This app is designed to help you predict future prices of various US stocks using advanced machine learning techniques. Powered by a **Decision Tree Algorithm** and built with **Streamlit**, this tool provides insights into stock market trends based on historical data and machine learning predictions.

    ### Key Features:
    - **Stock Dataset Viewer**: Explore historical data used for predictions, with an easy-to-read dataset display.
    - **Interactive Graphs**: Visualize price trends with dynamic graphs that help you analyze past performance and potential future movements.
    - **Real-time Predictions**: Input relevant parameters and generate real-time price predictions for popular US stocks.
    - **Machine Learning Model**: The app uses a Decision Tree algorithm, a robust tool for uncovering complex patterns in stock price trends.

    ### How It Works:
    1. **View Historical Data**: Access the underlying stock dataset to understand the inputs driving predictions.
    2. **Interactive Graphs**: Visualize past trends and predicted outcomes through interactive graphs.
    3. **Input Data for Predictions**: Provide key market indicators, and the app will predict future prices using machine learning.
    4. **Comprehensive Results**: Compare predicted prices against historical data to better understand potential market directions.

    Whether you're an experienced trader or new to stocks, this app offers powerful tools to help you make more informed decisions in the ever-changing US stock market.
    """,
    unsafe_allow_html=False
    )

if __name__ == "__main__":
    main()