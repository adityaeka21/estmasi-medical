import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

model = pickle.load(open('estimasi_medical.sav', 'rb'))

st.title('Estimasi Asuransi Kesehatan')

age = st.number_input('Umur Pasien')
sex2 = st.selectbox('Jenis Kelamin', ['Laki-Laki', 'Perempuan'])
bmi = st.number_input('Input BMI')
children = st.number_input('Jumlah Tanggungan Anak')
smoker2 = st.selectbox('Apakah Pasien Merokok', ['Yes', 'No'])
region2 = st.selectbox('Wilayah Domisili', ['southeast', 'southwest', 'northwest', 'northeast'])

# Define LabelEncoders for categorical variables
label_encoder_sex = LabelEncoder()
label_encoder_smoker = LabelEncoder()
label_encoder_region = LabelEncoder()

# Anda perlu melakukan fit pada objek LabelEncoder sebelum melakukan transform
label_encoder_sex.fit(['Laki-Laki', 'Perempuan'])
label_encoder_smoker.fit(['Yes', 'No'])
label_encoder_region.fit(['southeast', 'southwest', 'northwest', 'northeast'])

sex_encoded = label_encoder_sex.transform([sex2])[0]
smoker_encoded = label_encoder_smoker.transform([smoker2])[0]
region_encoded = label_encoder_region.transform([region2])[0]

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[age, sex_encoded,bmi, children, smoker_encoded, region_encoded]]
    )
    st.write('Estimasi Biaya Medis dalam US Dolar:', predict)
    st.write('Estimasi Biaya Medis dalam IDR (Juta):', predict * 15000)
