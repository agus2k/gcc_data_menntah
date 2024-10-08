import streamlit as st
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import time
import seaborn as sn


st.title('Prediksi Gaji pada saat lulus')
st.subheader('Memprediksi apakah kalian lulus lalu bekerja dengan gaji di atas atau sama dengan UMR tempat kalian bekerja')
url = 'https://raw.githubusercontent.com/agus2k/gcc_data_menntah/main/Data_Mentah_Bekerja.csv'

df_kerja = pd.read_csv(url,
        delimiter=';', 
        header='infer', 
        index_col=False)
X = df_kerja[['Jenis_Kelamin','Jurusan','Kota','Linier','Kerjasama','BKK']]
Y = df_kerja['UMR']
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25,random_state=123) # 75% training and 25% test
#Import svm model
from sklearn import svm
#Create a svm Classifier
clf_svm = svm.SVC(kernel='linear',probability=True) # Linear Kernel
#Train the model using the training sets
clf_svm.fit(X_train, y_train.values.ravel())
#Predict the response for test dataset

from sklearn.naive_bayes import GaussianNB
# Mengaktifkan/memanggil/membuat fungsi klasifikasi Naive Bayes
modelnb = GaussianNB()
# Memasukkan data training pada fungsi klasifikasi Naive Bayes
clf_nb = modelnb.fit(X_train, y_train.values.ravel())    

from sklearn.neighbors import KNeighborsClassifier  
clf_knn = KNeighborsClassifier(n_neighbors=5)  
clf_knn.fit(X_train, y_train.values.ravel())

nama = st.text_input('Nama')
jk = st.radio('Jenis Kelamin',options=('Laki-Laki','Perempuan'))
jurusan = st.selectbox('Jurusan', options=['Akuntansi dan Keuangan Lembaga','Bisnis Daring dan Pemasaran','Otomatisasi dan Tata Kelola Perkantoran','Multimedia','Rekayasa Perangkat Lunak','Teknik Komputer dan Jaringan'])

kota = st.selectbox('Kota tempat kalian akan bekerja', options=['Probolinggo','Kota Probolinggo','Jember','Gresik'])

linier = st.selectbox('Pekerjaan Linier dengan jurusan', options=['Ya','Tidak'])

kerjasama = st.selectbox('Tempat bekerja yang kalian inginkan bekerja sama dengan sekolah', options=['Ya','Tidak'])

bkk = st.selectbox('Butuh bantuan BKK untuk masuk ke tempat kerja ?', options=['Ya','Tidak'])

if st.button('Prediksi'):
    mybar = st.progress(0)
    jk = 0 if jk == 'Laki-Laki' else 1
    if jurusan == 'Akuntansi dan Keuangan Lembaga':
        jurusan = 1    
    elif jurusan == 'Bisnis Daring dan Pemasaran':
        jurusan = 2
    elif jurusan == 'Otomatisasi dan Tata Kelola Perkantoran':
        jurusan = 3
    elif jurusan == 'Multimedia':
        jurusan = 4
    elif jurusan == 'Rekayasa Perangkat Lunak':
        jurusan = 5
    elif jurusan == 'Teknik Komputer dan Jaringan':
        jurusan = 6
    kotaa = 0
    if kota == 'Probolinggo':
        kotaa =1
    elif kota == 'Kota Probolinggo':
        kotaa = 2
    elif kota == 'Jember':
        kotaa = 3
    elif kota == 'Gresik':
        kotaa = 4
    
    linier = 1 if linier == 'Ya' else 0
    
    kerjasama = 1 if kerjasama == 'Ya' else 0

    bkk = 1 if bkk == 'Ya' else 0
    tes = [[jk,jurusan,kotaa,linier,kerjasama,bkk]]

    
    hasil_svm = clf_svm.predict(tes)
    akurasi_svm = clf_svm.predict_proba(tes)
    hasil_nb = clf_nb.predict(tes)
    akurasi_nb = clf_nb.predict_proba(tes)
    hasil_knn = clf_knn.predict(tes)
    akurasi_knn = clf_knn.predict_proba(tes)

    for persen in range(100):
        time.sleep(0.01)
        mybar.progress(persen+1)

    st.subheader('Support Vector Machine')
    if hasil_svm[0]==1:
        st.write('Dengan menggunakan metode SVM maka {} akan bekerja dengan **GAJI DIATAS/SAMA DENGAN UMR** wilayah {} dengan tingkat peluang {}%'.format(nama,kota,round(akurasi_svm[0][1]*100),3))
    else:
        st.write('Dengan menggunakan metode SVM maka {} akan bekerja dengan **GAJI DIBAWAH UMR** wilayah {} dengan tingkat peluang {}%'.format(nama,kota,round(akurasi_svm[0][1]*100),3))

    st.subheader('Naive Bayes')
    if hasil_nb[0]==1:
        st.write('Dengan menggunakan metode Naive Bayes maka {} akan bekerja dengan **GAJI DIATAS/SAMA DENGAN UMR** wilayah {} dengan tingkat peluang {}%'.format(nama,kota,round(akurasi_nb[0][1]*100),3))
    else:
        st.write('Dengan menggunakan metode Naive Bayes maka {} akan bekerja dengan **GAJI DIBAWAH UMR** wilayah {} dengan tingkat peluang {}%'.format(nama,kota,round(akurasi_nb[0][1]*100),3))

    st.subheader('K-Nearest Neighbor')
    if hasil_knn[0]==1:
        st.write('Dengan menggunakan metode KNN maka {} akan bekerja dengan **GAJI DIATAS/SAMA DENGAN UMR** wilayah {} dengan tingkat peluang {}%'.format(nama,kota,round(akurasi_knn[0][1]*100),3))
    else:
        st.write('Dengan menggunakan metode KNN maka {} akan bekerja dengan **GAJI DIBAWAH UMR** wilayah {} dengan tingkat peluang {}%'.format(nama,kota,round(akurasi_knn[0][1]*100),3))
    





