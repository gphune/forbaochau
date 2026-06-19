import streamlit as st

st.title("💖 Web dành cho em")

name = st.text_input("Tên em là gì?")

if st.button("Bấm vào đây"):
    st.balloons()
    st.write(f"Anh yêu {name} ❤️")