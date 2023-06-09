import pickle
import streamlit as st

# membaca model
gaji_model = pickle.load(open('gaji_model_regression.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Total Pendapatan Pertahun')

#membagi kolom
col1, col2 = st.columns(2)

with col1 :
    age = st.number_input ('Umur')
    workclass = st.number_input ('Kelas Kerja, Private=0 , Self-emp-not-inc=1, Local-gov=2, State-gov=3, Self-emp-inc=4, Federal-gov=5, Without-pay=6, Never-worked=7')
    education = st.number_input ('Pendidikan, HS-grad=0, Some-college=1, Bachelors=2, Masters=3, Assoc-voc=4, Assoc-acdm=5, Prof-school=6, Doctorate=7, Preschool=8')
    marital_status = st.number_input ('Status Perkawinan, Married-civ-spouse=0, Never-married=1, Divorced=2, Separated=3, Widowed=4')
    

with col2 :
    relationship = st.number_input ('Status Berkeluarga, Husband=0, Not-in-family=1, Own-child=2, Unmarried=3, Wife=4')
    sex = st.number_input ('Jenis Kelamin, Female=0, Male=1')
    capital_gain= st.number_input ('Total Capitan Gain')
    capital_loss= st.number_input ('Total Capital Loss')
    hours_per_week= st.number_input ('Jumlah Jam Kerja Per-Minggu')

# code untuk prediksi
gaji_diag = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi gaji'):
    gaji_predict = gaji_model.predict([[age, workclass, education, marital_status, relationship, 
                                            sex, capital_gain, capital_loss, hours_per_week]])

    if gaji_predict == 0:
        gaji_diag = 'Total pendapatan pertahun <=50K US Dollar'
    else:
        gaji_diag = 'Total pendapatan pertahun >50K US Dollar'
st.success(gaji_diag)
