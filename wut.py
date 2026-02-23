import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="TSLA Stock Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 TSLA Stock Market Dashboard (2012–2026)")
st.markdown("Interactive Dashboard สำหรับวิเคราะห์ข้อมูลราคาหุ้น TSLA")

# =============================
# Upload CSV
# =============================
uploaded_file = st.file_uploader("📂 Upload TSLA CSV File", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    # แปลง Date เป็น datetime
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"])

    df = df.sort_values("Date")

    # =============================
    # Sidebar Filter
    # =============================
    st.sidebar.header("🔎 Filters")

    min_date = df["Date"].min()
    max_date = df["Date"].max()

    date_range = st.sidebar.date_input(
        "Select Date Range",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date
    )

    df = df[
        (df["Date"] >= pd.to_datetime(date_range[0])) &
        (df["Date"] <= pd.to_datetime(date_range[1]))
    ]

    # =============================
    # Moving Average
    # =============================
    df["MA7"] = df["Close"].rolling(7).mean()
    df["MA30"] = df["Close"].rolling(30).mean()

    # =============================
    # KPI Section
    # =============================
    st.subheader("📌 Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Highest Price", f"${df['High'].max():.2f}")
    col2.metric("Lowest Price", f"${df['Low'].min():.2f}")
    col3.metric("Average Close", f"${df['Close'].mean():.2f}")
    col4.metric("Total Volume", f"{int(df['Volume'].sum()):,}")

    # =============================
    # Price Trend Chart
    # =============================
    st.subheader("📈 Price Trend with Moving Average")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Date"],
        y=df["Close"],
        mode="lines",
        name="Close Price"
    ))

    fig.add_trace(go.Scatter(
        x=df["Date"],
        y=df["MA7"],
        mode="lines",
        name="MA7"
    ))

    fig.add_trace(go.Scatter(
        x=df["Date"],
        y=df["MA30"],
        mode="lines",
        name="MA30"
    ))

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Price ($)",
        hovermode="x unified"
    )

    st.plotly_chart(fig, use_container_width=True)

    # =============================
    # Volume Chart
    # =============================
    st.subheader("📊 Volume Analysis")

    fig2 = px.bar(
        df,
        x="Date",
        y="Volume",
        title="Trading Volume"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # =============================
    # Candlestick Chart
    # =============================
    st.subheader("🕯 Candlestick Chart")

    fig3 = go.Figure(data=[go.Candlestick(
        x=df["Date"],
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"]
    )])

    fig3.update_layout(
        xaxis_title="Date",
        yaxis_title="Price ($)"
    )

    st.plotly_chart(fig3, use_container_width=True)

    # =============================
    # Raw Data
    # =============================
    st.subheader("📄 Raw Data")
    st.dataframe(df)

    # Download button
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇ Download Filtered Data",
        csv,
        "filtered_tsla_data.csv",
        "text/csv"
    )

else:
    st.info("📂 กรุณาอัปโหลดไฟล์ TSLA CSV เพื่อเริ่มใช้งาน")
