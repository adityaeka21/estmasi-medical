import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

model = pickle.load(open('estimasi_medical.sav', 'rb'))

st.title('Estimasi Asuransi Kesehatan')

age = st.number_input('Umur Pasien')
sex2 = st.selectbox('Jenis Kelamin', ['Laki-Laki', 'Perempuan'])
children = st.number_input('Jumlah Tanggungan Anak')
smoker2 = st.selectbox('Apakah Pasien Merokok', ['Yes', 'No'])
region2 = st.selectbox('Wilayah Domisili', ['southeast','southwest', 'northwest','northeast'])

label_encoder_sex = LabelEncoder()
label_encoder_smoker = LabelEncoder()
label_encoder_region = LabelEncoder()

sex_encoded = label_encoder_sex.transform([sex])[0]
smoker_encoded = label_encoder_smoker.transform([smoker])[0]
region_encoded = label_encoder_region.transform([region])[0]

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[age,sex2,bmi,children,smoker2,region2]]
    )
    st.write ('Estimasi Biaya Medis dalam US Dolar : ', predict)
    st.write ('Estimasi Biaya Medis dalam IDR (Juta) :', predict*15000)
