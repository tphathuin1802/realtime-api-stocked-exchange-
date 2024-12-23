import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Import your df and df_balance from asset.main (ensure this import is correct)
from asset.main import df, df_balance

# Use Markdown with custom HTML and CSS to center the header
st.markdown(
    """
    <h1 style='text-align: center;'>BINANCE TRADING UPDATE TOOL</h1>
    """,
    unsafe_allow_html=True,
)

# Initialize the session state
if "selection" not in st.session_state:
    st.session_state["selection"] = 0

# Create a dropdown to change selection (if applicable to your use case)
st.session_state["selection"] = st.selectbox(
    "Select Option", options=["Option 1", "Option 2", "Option 3"]
)

# Check if df is not empty
if df is not None and not df.empty:
    # Create candlestick chart
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["timestamp"],
                open=df["open"],
                high=df["high"],
                low=df["low"],
                close=df["close"],
            )
        ]
    )

    fig.update_layout(
        title=dict(text="Binance Candlestick Chart"),
        yaxis=dict(title=dict(text="Binance Stock")),
        width=1900,
        height=700,
    )

    # Display candlestick chart and data
    st.plotly_chart(fig)
else:
    st.error("Data not available for candlestick chart")

# Optional: Display balance data (if needed)
if df_balance is not None and not df_balance.empty:
    st.write("Account Balance Data:", df_balance)
else:
    st.write("Balance data not available")
