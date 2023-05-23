import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('kanker_payudara.sav', 'rb'))

st.title('Klasifikasi Kanker Payudara')
kol1, kol2 = st.columns(2)
with kol1:
    pid = st.number_input('ID Pasien')
    meno = st.number_input('Status Menopause (0= premenopausal, 1= postmenopausal)')
    grade = st.number_input('Tingkat Tumor')
    pgr = st.number_input('Reseptor Progesteron')
    hormon = st.number_input('Terapi Hormon (0= Tidak, 1= Ya)')
    
with kol2:
    age = st.number_input('Usia Pasien')
    size = st.number_input('Ukuran Tumor (mm)')
    nodes = st.number_input('Jumlah Kelenjar Getah Bening')
    er = st.number_input('Reseptor Estrogen')
    rfstime = st.number_input('Jumlah Hari Dari Sehat ke Pertama Kambuh')

prediksi = ''
if st.button('Hasil'):
    prediksi = model.predict([[pid, age, meno, size, grade, nodes, pgr, er, hormon, rfstime]])
    
    if (prediksi [0] == 0):
        prediksi = 'Sembuh Total Tanpa Kambuh'
    else:
        prediksi = 'Kambuh Atau Meninggal'
st.success(prediksi)