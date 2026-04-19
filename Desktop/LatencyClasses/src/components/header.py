import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px; margin-top: 20px;">
            <img src='{logo_url}' height='100px'/>
            <h1 style='text-align: center; color: #E0E3FF; font-family: "Climate Crisis", sans-serif;'>Latency<br>Classes</h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: flex-start; gap: 10px; padding: 10px 0;">
            <img src='{logo_url}' height='85px'/>
            <h2 style='text-align: left; color: #5B6EE1; font-family: "Climate Crisis", sans-serif; margin: 0;'>Latency<br>Classes</h2>
        </div>
    """, unsafe_allow_html=True)