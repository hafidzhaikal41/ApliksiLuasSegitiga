import streamlit as st

st.write(""" 
# Aplikasi Luas Segitiga
Ini adalah aplikasi menghitung luas segitiga sederhana menggunakan Streamlit
 """)

alas = st.number_input("Masukkan Alas", 0)
tinggi = st.number_input("Masukkan Tinggi", 0)
hitung = st.button("Hitung Luas")

if hitung:
    luas= 0.5 * alas * tinggi
    st.success(f"Luas Segitiganya adalah {luas}")
    st.balloons()