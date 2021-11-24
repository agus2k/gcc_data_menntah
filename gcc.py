from re import S
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn
import time
import seaborn as sn

st.set_option('deprecation.showPyplotGlobalUse', False)
option = st.sidebar.selectbox('Silahkan Pilih :',('Home','Data Kuliah','Data Kerja','Tes Klasifikasi','Prediksi') )

if option == 'Home' or option == '':
    st.title("Penelusuran Tamatan SMKN 1 Kraksaan tahun 2021") #menampilkan halaman utama
    st.header('Dengan menggunakan Hasil Penelusuran tamatan, maka saya akan memvisualisasikan data hasil penelusuran tamatan')
    url = 'https://raw.githubusercontent.com/agus2k/gcc_data_menntah/2a71f4a4c0460604e0a546dc0221ad11da379f9b/Data_Mentah_Keseluruhan.csv'
    df = pd.read_csv(url,
        delimiter=';', 
        header='infer', 
        index_col=False)
    st.table(df.head(5))
    counts = [
          df[df['Jenis_Kelamin']==0].shape[0],
          df[df['Jenis_Kelamin']==1].shape[0]
    ]
    #print(counts)
    labels = ['Laki - Laki','Perempuan']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    st.subheader('Jenis Kelamin Alumni 2021 yang mengisi survei')

    st.pyplot(fig)

    plt.figure(figsize=(5,7))
    plt.bar(labels, counts, color=['blue','red'])

    plt.title('Jumlah Alumni Yang Mengisi Survei Berdasarkan Gender', size=10)
    plt.ylabel('Jumlah Alumni', size=9)
    plt.xlabel('Gender', size=12)
    plt.xticks(size=9)
    plt.yticks(size=12)

    st.pyplot()
    st.write('Dari Sini kita bisa melihat bahwa yang mengisi survei lebih banyak dari Jenis Kelamin Perempuan dibanding Laki - Laki. Disini bisa dimaklumi dikarenakan memang siswa SMKN 1 Kraksaan mayoritas gender lebih banyak Perempuan dibanding Laki-Laki')
    st.header('Sebaran Alumni')
    st.subheader('Lalu kita buat Pie Chart dan Bar Chart Berdasarkan Pekerjaan mereka pada saat lulus, disini ada 5 pilihan yaitu :')
    st.write('1. Kuliah/Kursus (Melanjutkan Studi)')
    st.write('2. PNS/ASN')
    st.write('3. Karyawan Swasta')
    st.write('4. Wirausaha')
    st.write('5. Belum Bekerja')
    counts = [
          df[df['Pekerjaan']==1].shape[0],
          df[df['Pekerjaan']==2].shape[0],
          df[df['Pekerjaan']==3].shape[0],
          df[df['Pekerjaan']==4].shape[0],
          df[df['Pekerjaan']==5].shape[0],
    ]
    labels = ['Kuliah/Kursus','PNS','Karyawan Swasta','Wirausaha','Belum Bekerja']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Pekerjaan Alumni tahun 2021')

    st.pyplot(fig)

    plt.figure(figsize=(15,7))
    plt.bar(labels, counts, color=['blue','red','purple','green','navy'])

    plt.title('Pekerjaan Alumni 2021', size=16)
    plt.ylabel('Jumlah Alumni', size=14)
    plt.xlabel('Pekerjaan', size=12)
    plt.xticks(size=9)
    plt.yticks(size=12)

    st.pyplot()
    st.write('Disini kita bisa simpulkan bahwa alumni yang lulus tahun 2021 paling banyak Belum bekerja, disusul Kuliah/Kursus, lalu Karyawan, Wirausaha dan paling sedikit adalah PNS/ASN')
    st.write('Belum Bekerja memang paling banyak dikarenakan pada saat mereka lulus kondisi masih pandemi serta perusahaan yang biasa membuka lowongan pun tidak membuka lowongan dikarenakan pandemi Covid 19')
    pekerjaan = []
    for i in range(1, 6):
        d = []
        for j in range(1,7):
            d.append(df[(df.Jurusan == j) & (df.Pekerjaan == i)].count()['Pekerjaan'])
        pekerjaan.append(d)

    jurusan = ['Akuntansi dan Keuangan Lembaga',
            'Bisnis Daring dan Pemasaran',
            'Otomatisasi dan Tata Kelola Perkantoran',
            'Multimedia',
            'Rekayasa Perangkat Lunak',
            'Teknik Komputer dan Jaringan']
    x = np.arange(len(jurusan))
    width = 0.15

    fig, ax = plt.subplots(figsize=(20, 7))

    pk1 = ax.bar(x + 0.00, pekerjaan[0], width, label='Kuliah', color='steelblue')
    pk2 = ax.bar(x + 0.15, pekerjaan[1], width, label='PNS', color='lightcoral')
    pk3 = ax.bar(x + 0.30, pekerjaan[2], width, label='Karyawan Swasta', color='blue')
    pk4 = ax.bar(x + 0.45, pekerjaan[3], width, label='Wirausaha', color='yellow')
    pk5 = ax.bar(x + 0.60, pekerjaan[4], width, label='Belum Bekerja', color='red')

    ax.set_title('Sebaran Pekerjaan Alumni Setelah Lulus', size=16)
    ax.set_ylabel('Jumlah', size=14)
    ax.set_xticks(x+0.3)
    ax.set_xticklabels(jurusan, size=10)
    ax.legend(fontsize=14)

    st.subheader('Sebaran Pekerjaan alumni SMKN 1 Kraksaan yang lulus tahun 2021 berdasarkan Jurusan Sekolah')
    st.pyplot()
    st.write('Disini dapat kita simpulkan bahwa memang seperti data global bahwa lulusan 2021 banyak yang belum bekerja.')
    st.write('Tetapi ada yang menarik di Jurusan Bisnis Daring dan Pemasaran bahwa alumni nya lebih banyak yang bekerja dibandingkan yang kuliah, dibandingkan dengan jurusan lain yang melanjutkan kuliah lebih banyak daripada yang bekerja')
elif option == 'Data Kuliah':
    st.title('Visualisasi Data Alumni yang melanjutkan studi')
    url = 'https://raw.githubusercontent.com/agus2k/gcc_data_menntah/main/Data_Mentah_Kuliah.csv'
    df_kuliah = pd.read_csv(url,
            delimiter=';', 
            header='infer', 
            index_col=False)
    st.table(df_kuliah.head())
    st.header('Institusi')
    st.subheader('Visualisasi institusi apa yang dipilih atau menjadi tempat melanjutkan studi alumni. Disini ada 4 pilihan yaitu :')
    st.write('1.   Universitas')
    st.write('2.   Politeknik')
    st.write('3.   Kursus')
    st.write('4.   Sekolah Tinggi')
    counts = [
          df_kuliah[df_kuliah['Institusi']==1].shape[0],
          df_kuliah[df_kuliah['Institusi']==2].shape[0],
          df_kuliah[df_kuliah['Institusi']==3].shape[0],
          df_kuliah[df_kuliah['Institusi']==4].shape[0]
    ]
    #print(counts)
    labels = ['Universitas','Politeknik','Kursus','Sekolah Tinggi']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Institusi yang diambil Alumni SMKN 1 Kraksaan')

    st.pyplot(fig)
    plt.figure(figsize=(5,7))
    plt.bar(labels, counts, color=['blue','red','navy','lightcoral'])

    plt.title('Institusi yang diambil Alumni SMKN 1 Kraksaan', size=10)
    plt.ylabel('Jumlah Alumni', size=9)
    plt.xlabel('Institusi', size=12)
    plt.xticks(size=9)
    plt.yticks(size=12)

    st.pyplot()
    st.write('Disini bisa disimpulkan bahwa Alumni yang lulus tahun 2021 paling banyak melanjutkan studi di Universitas')
    institusi = []
    st.subheader('Sebaran Institusi Alumni yang melanjutkan studi per Jurusan')
    for i in range(1,5):
        d = []
        for j in range(1,7):
            d.append(df_kuliah[(df_kuliah.Jurusan == j) & (df_kuliah.Institusi == i)].count()['Institusi'])
        institusi.append(d)

    jurusan = ['Akuntansi dan Keuangan Lembaga',
            'Bisnis Daring dan Pemasaran',
            'Otomatisasi dan Tata Kelola Perkantoran',
            'Multimedia',
            'Rekayasa Perangkat Lunak',
            'Teknik Komputer dan Jaringan']

    x = np.arange(len(jurusan))
    width = 0.15

    fig, ax = plt.subplots(figsize=(20, 7))

    pk1 = ax.bar(x-0.15 , institusi[0], width, label='Universitas', color='navy')
    pk1 = ax.bar(x , institusi[1], width, label='Politeknik', color='red')
    pk1 = ax.bar(x +0.15, institusi[2], width, label='Kursus', color='yellow')
    pk1 = ax.bar(x +0.30, institusi[3], width, label='Sekolah Tinggi', color='lightcoral')

    ax.set_title('Institusi yang diambil oleh Alumni', size=16)
    ax.set_ylabel('Jumlah', size=14)
    ax.set_xticks(x)
    ax.set_xticklabels(jurusan, size=10)
    ax.legend(fontsize=14)

    st.pyplot()
    st.write('Disini bisa disimpulkan bahwa Alumni yang lulus tahun 2021 paling banyak melanjutkan studi di Universitas')

    institusi = []
    for i in range(1,5):
        d = []
        for j in range(1,7):
            d.append(df_kuliah[(df_kuliah.Jurusan == j) & (df_kuliah.Institusi == i)].count()['Institusi'])
        institusi.append(d)

    jurusan = ['Akuntansi dan Keuangan Lembaga',
            'Bisnis Daring dan Pemasaran',
            'Otomatisasi dan Tata Kelola Perkantoran',
            'Multimedia',
            'Rekayasa Perangkat Lunak',
            'Teknik Komputer dan Jaringan']

    x = np.arange(len(jurusan))
    width = 0.15

    fig, ax = plt.subplots(figsize=(20, 7))

    pk1 = ax.bar(x-0.15 , institusi[0], width, label='Universitas', color='navy')
    pk1 = ax.bar(x , institusi[1], width, label='Politeknik', color='red')
    pk1 = ax.bar(x +0.15, institusi[2], width, label='Kursus', color='yellow')
    pk1 = ax.bar(x +0.30, institusi[3], width, label='Sekolah Tinggi', color='lightcoral')

    ax.set_title('Institusi yang diambil oleh Alumni', size=16)
    ax.set_ylabel('Jumlah', size=14)
    ax.set_xticks(x)
    ax.set_xticklabels(jurusan, size=10)
    ax.legend(fontsize=14)

    st.pyplot()
    st.write('Kesimpulannya bahwa Otomatisasi dan Tata Kelola Perkantoran paling banyak yang melanjutkan studi di Universitas.')

    st.write('Selanjutnya kita kelompokkan berdasarkan Kota tempat alumni melanjutkan studi. Disini kita pakai transformasi data dengan data yaitu :')
    st.write('1.   Probolinggo')
    st.write('2.   Malang')
    st.write('3.   Jember')
    st.write('4.   Banyuwangi')
    st.write('5.   Kediri')
    st.write('6.   Bondowoso')
    st.write('7.   Bali')

    counts = [
          df_kuliah[df_kuliah['Kota']==1].shape[0],
          df_kuliah[df_kuliah['Kota']==2].shape[0],
          df_kuliah[df_kuliah['Kota']==3].shape[0],
          df_kuliah[df_kuliah['Kota']==4].shape[0],
          df_kuliah[df_kuliah['Kota']==5].shape[0],
          df_kuliah[df_kuliah['Kota']==6].shape[0],
          df_kuliah[df_kuliah['Kota']==7].shape[0]
    ]
    #print(counts)
    labels = ['Probolinggo','Malang','Jember','Banyuwangi','Kediri','Bondowoso','Bali']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Kota tempat Kuliah yang diambil Alumni SMKN 1 Kraksaan')

    st.pyplot(fig)

    plt.figure(figsize=(12,7))
    plt.bar(labels, counts, color=['blue','red','navy','lightcoral'])

    plt.title('Kota Tempat Kuliah yang diambil Alumni SMKN 1 Kraksaan', size=15)
    plt.ylabel('Jumlah Alumni', size=9)
    plt.xlabel('Institusi', size=12)
    plt.xticks(size=9)
    plt.yticks(size=12)
    st.pyplot()

    st.write('Disini bisa kita simpulkan bahwa alumni memang kebanyakan melanjutkan studi di Probolinggo. Tetapi ada hal yang menarik bahwa ada juga alumni yang melanjutkan studi di luar Provinsi Jawa Timur, yaitu Bali.')
    st.write('Disini bisa dibuat peluang sekolah agar bisa bekerjasama dengan wilayah yang lebih luas lagi, bukan hanya di dalam Provinsi, tetapi bisa diluar provinsi juga')

    st.subheader('Selanjutnya kita visualisasikan data bahwa alumni melanjutkan studi dengan konseling ke Guru BK sebelumnya atau tidak')

    counts = [
          df_kuliah[df_kuliah['Konseling']==0].shape[0],
          df_kuliah[df_kuliah['Konseling']==1].shape[0]
    ]
    labels = ['Tidak Konseling','Konseling']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Alumni Kuliah dengan bantuan Konseling Guru BK')

    st.pyplot()

    st.write('Disini bisa kita simpulkan bahwa 26.2 % alumni konseling ke BK terlebih dahulu dan kebanyakan tidak konseling atau memutuskan sendiri tanpa konseling ke BK')

    konseling = []
    for i in range(0,2):
        d = []
        for j in range(1,7):
            d.append(df_kuliah[(df_kuliah.Jurusan == j) & (df_kuliah.Konseling == i)].count()['Konseling'])
        konseling.append(d)

    jurusan = ['Akuntansi dan Keuangan Lembaga',
            'Bisnis Daring dan Pemasaran',
            'Otomatisasi dan Tata Kelola Perkantoran',
            'Multimedia',
            'Rekayasa Perangkat Lunak',
            'Teknik Komputer dan Jaringan']

    x = np.arange(len(jurusan))
    width = 0.15

    fig, ax = plt.subplots(figsize=(20, 7))

    pk1 = ax.bar(x - width/2, konseling[0], width, label='Tidak Konseling', color='red')
    pk2 = ax.bar(x + width/2, konseling[1], width, label='Konseling', color='navy')

    ax.set_title('Alumni Kuliah dengan bantuan Konseling Guru BK', size=16)
    ax.set_ylabel('Jumlah', size=14)
    ax.set_xticks(x)
    ax.set_xticklabels(jurusan, size=10)
    ax.legend(fontsize=14)

    st.pyplot()
    st.write('Lalu dibagi perjurusan pun hasilnya sama bahwa kebanyakan alumni melanjutkan studi tanpa konsul dulu dengan BK. Lalu bisa dilihat juga jurusan Multimedia bahwa alumni yang melanjutkan studi tidak ada yang konsul dengan BK terlebih dahulu, data ini bisa jadi catatan untuk Guru BK agar bisa menarik minat calon alumni agar bisa konsul dulu ke BK')

    st.subheader('Selanjutnya kita visualisasikan data bahwa alumni apakah melanjutkan studi linier dengan jurusan mereka pada saat mereka sekolah')

    counts = [
          df_kuliah[df_kuliah['Linier']==0].shape[0],
          df_kuliah[df_kuliah['Linier']==1].shape[0]
    ]
    labels = ['Tidak Linier','Linier']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Linieritas Alumni yang Kuliah dengan Jurusan Sekolah')

    st.pyplot()
    st.write('Bisa kita lihat dari diagram diatas bahwa labih dari 70 persen jurusan alumni yang melanjutkan studi linier dengan jurusan nya pada saat sekolah')
    linier = []
    for i in range(0,2):
        d = []
        for j in range(1,7):
            d.append(df_kuliah[(df_kuliah.Jurusan == j) & (df_kuliah.Linier == i)].count()['Linier'])
        linier.append(d)

    jurusan = ['Akuntansi dan Keuangan Lembaga',
            'Bisnis Daring dan Pemasaran',
            'Otomatisasi dan Tata Kelola Perkantoran',
            'Multimedia',
            'Rekayasa Perangkat Lunak',
            'Teknik Komputer dan Jaringan']

    x = np.arange(len(jurusan))
    width = 0.15

    fig, ax = plt.subplots(figsize=(20, 7))

    pk1 = ax.bar(x - width/2, linier[0], width, label='Tidak Linier', color='red')
    pk2 = ax.bar(x + width/2, linier[1], width, label='Linier', color='navy')

    ax.set_title('Linieritas Alumni yang Kuliah dengan Jurusan Sekolah', size=16)
    ax.set_ylabel('Jumlah', size=14)
    ax.set_xticks(x)
    ax.set_xticklabels(jurusan, size=10)
    ax.legend(fontsize=14)

    st.pyplot()
    st.write('Begitu juga untuk per jurusan bahwa banyak yang Linier dengan jurusan mereka pada saat sekolah, akan tetapi tidak dengan jurusan Rekayasa Perangkat Lunak. Untuk Jurusan Rekayasa Perangkat Lunak lebih banyak yang tidak Linier dibandingkan yang linier')
elif option == 'Data Kerja':
    st.title('Data Alumni yang Bekerja')
    st.subheader('Disini Kita akan mengolah data dari data global menjadi spesifik untuk data yang alumni yang bekerja')
    url = 'https://raw.githubusercontent.com/agus2k/gcc_data_menntah/main/Data_Mentah_Bekerja.csv'

    df_kerja = pd.read_csv(url,
            delimiter=';', 
            header='infer', 
            index_col=False)
    st.table(df_kerja.head())
    st.subheader('Lalu kita visualisasi data untuk dengan menggunakan pie chart dan bar diagram')

    st.write('Disini kita akan membandingkan apakah yang Bekerja berdasarkan Jenis Kelamin')

    counts = [
          df_kerja[df_kerja['Jenis_Kelamin']==0].shape[0],
          df_kerja[df_kerja['Jenis_Kelamin']==1].shape[0]
    ]
    #print(counts)
    labels = ['Laki - Laki','Perempuan']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Sebaran Alumni 2021 yang Bekerja Berdasarkan Jenis Kelamin')

    st.pyplot(fig)

    plt.figure(figsize=(5,7))
    plt.bar(labels, counts, color=['blue','red'])

    plt.title('Jumlah Alumni Yang Bekerja Berdasarkan Gender', size=10)
    plt.ylabel('Jumlah Alumni', size=9)
    plt.xlabel('Gender', size=12)
    plt.xticks(size=9)
    plt.yticks(size=12)
    st.pyplot()
    st.subheader('Per Jurusan')
    counts = [
          df_kerja[df_kerja['Jurusan']==1].shape[0],
          df_kerja[df_kerja['Jurusan']==2].shape[0],
          df_kerja[df_kerja['Jurusan']==3].shape[0],
          df_kerja[df_kerja['Jurusan']==4].shape[0],
          df_kerja[df_kerja['Jurusan']==5].shape[0],
          df_kerja[df_kerja['Jurusan']==6].shape[0],
    ]
    labels = ['Akuntansi dan Keuangan Lembaga','Bisnis Daring dan Pemasaran','Otomatisasi dan Tata Kelola Perkantoran','Multimedia','Rekayasa Perangkat Lunak','Teknik Komputer dan Jaringan']

    plt.figure(figsize=(20,7))
    plt.bar(labels, counts, color=['blue','red','purple','yellow','green','navy'])

    plt.title('Jumlah Alumni Yang Bekerja per Jurusan', size=16)
    plt.ylabel('Jumlah Alumni', size=14)
    plt.xlabel('Jurusan', size=12)
    plt.xticks(size=9)
    plt.yticks(size=12)

    st.pyplot()
    st.write('Disini bisa kita simpulkan bahwa Jurusan Otomatisasi dan Tata Kelola Perkantoran lebih banyak menyumbang alumni nya yang bekerja dibandingkan jurusan yang lain')

    st.subheader('Lalu kita visualisasikan data alumni yang bekerja berdasarkan tempat mereka bekerja, disini ada 4 kota/wilayah alumni bekerja yaitu ')
    st.write('1. Kabupaten Probolinggo')
    st.write('2. Kota Probolinggo')
    st.write('3. Jember')
    st.write('4. Gresik')

    counts = [
          df_kerja[df_kerja['Kota']==1].shape[0],
          df_kerja[df_kerja['Kota']==2].shape[0],
          df_kerja[df_kerja['Kota']==3].shape[0],
          df_kerja[df_kerja['Kota']==4].shape[0]
    ]
    #print(counts)
    labels = ['Kab Probolinggo','Kota Probolinggo','Jember','Gresik']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Sebaran Alumni 2021 yang Bekerja Berdasarkan Kota Tempat Bekerja')

    st.pyplot(fig)

    plt.figure(figsize=(10,7))
    plt.bar(labels, counts, color=['blue','red'])

    plt.title('Jumlah Alumni 2021 yang Bekerja Berdasarkan Kota Tempat Bekerja', size=10)
    plt.ylabel('Jumlah Alumni', size=9)
    plt.xlabel('Kota', size=12)
    plt.xticks(size=9)
    plt.yticks(size=12)

    st.pyplot()
    st.write('Kesimpulannya bahwa alumni yang lulus di tahun 2021 banyak yang bekerja di wilayah Kabupaten Probolinggo, lalu Kota Probolinggo dan Jember sama jumlahnya dan sebagian kecil di Gresik')

    st.subheader('Selanjutnya kita Visualisasikan apakah tempat alumni bekerja telah melakukan kerjasama atau mempunyai MoU dengan sekolah')

    counts = [
          df_kerja[df_kerja['Kerjasama']==0].shape[0],
          df_kerja[df_kerja['Kerjasama']==1].shape[0]
    ]
    labels = ['Tidak Kerjasama','Kerjasama']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Tempat Alumni Bekerja telah Bekerjasama dengan Sekolah')

    st.pyplot(fig)

    st.write('Ternyata dari semua tempat alumni bekerja, lebih dari 70 persen belum melakukan kerjasama dengan sekolah, ini merupakan kesempatan besar untuk menjaring IDUKA yang bisa diajak kerjasama dengan sekolah agar keterserapan Alumni bisa lebih banyak lagi di tahun tahun berikutnya')

    kerjasama = []
    for i in range(0,2):
        d = []
        for j in range(1,7):
            d.append(df_kerja[(df_kerja.Jurusan == j) & (df_kerja.Kerjasama == i)].count()['Kerjasama'])
        kerjasama.append(d)

    jurusan = ['Akuntansi dan Keuangan Lembaga',
            'Bisnis Daring dan Pemasaran',
            'Otomatisasi dan Tata Kelola Perkantoran',
            'Multimedia',
            'Rekayasa Perangkat Lunak',
            'Teknik Komputer dan Jaringan']

    x = np.arange(len(jurusan))
    width = 0.15

    fig, ax = plt.subplots(figsize=(20, 7))

    pk1 = ax.bar(x - width/2, kerjasama[0], width, label='Tidak Kerjasama', color='red')
    pk2 = ax.bar(x + width/2, kerjasama[1], width, label='Kerjasama', color='navy')

    ax.set_title('Tempat Alumni Bekerja telah Bekerjasama dengan Sekolah', size=16)
    ax.set_ylabel('Jumlah', size=14)
    ax.set_xticks(x)
    ax.set_xticklabels(jurusan, size=10)
    ax.legend(fontsize=14)

    st.pyplot()

    st.write('Lalu dilihat dari pembagian berdasarkan jurusan juga banyak yang belum bekerjasama dengan sekolah, sehingga bisa dimanfaatkan. Lalu untuk Bisnis Daring dan Pemasaran bisa dilanjutkan kerjasamanya dikarenakan keterserapan nya lebih banyak yang kerjasama dibandingkan yang tidak kerjasama. Ini menunjukkan bahwa kerjasama di Jurusan Bisnis Daring dan Pemasaran telah terjalin dengan baik')

    st.subheader('Selanjutnya kita visualisasikan alumni yang bekerja apakah Linier dengan jurusan mereka pada saat sekolah')

    counts = [
          df_kerja[df_kerja['Linier']==0].shape[0],
          df_kerja[df_kerja['Linier']==1].shape[0]
    ]
    labels = ['Tidak Linier','Linier']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Pekerjaan Alumni Linier dengan jurusan pada saat Sekolah')

    st.pyplot(fig)

    linier = []
    for i in range(0,2):
        d = []
        for j in range(1,7):
            d.append(df_kerja[(df_kerja.Jurusan == j) & (df_kerja.Linier == i)].count()['Kerjasama'])
        linier.append(d)

    jurusan = ['Akuntansi dan Keuangan Lembaga',
            'Bisnis Daring dan Pemasaran',
            'Otomatisasi dan Tata Kelola Perkantoran',
            'Multimedia',
            'Rekayasa Perangkat Lunak',
            'Teknik Komputer dan Jaringan']

    x = np.arange(len(jurusan))
    width = 0.15

    fig, ax = plt.subplots(figsize=(20, 7))

    pk1 = ax.bar(x - width/2, linier[0], width, label='Tidak Linier', color='red')
    pk2 = ax.bar(x + width/2, linier[1], width, label='Linier', color='navy')

    ax.set_title('Pekerjaan Alumni Linier dengan jurusan pada saat Sekolah', size=16)
    ax.set_ylabel('Jumlah', size=14)
    ax.set_xticks(x)
    ax.set_xticklabels(jurusan, size=10)
    ax.legend(fontsize=14)

    st.pyplot()
    st.write('Ternyata untuk kebanyakan jurusan banyak yang tidak linier kecuali jurusan Bisnis Daring dan Pemasaran')

    st.subheader('Lalu kita lanjut memvisualisasikan data Alumni yang bekerja, apakah alumni bisa bekerja dari mendapatkan info atau dibantu BKK terkait rekrutmen')

    counts = [
          df_kerja[df_kerja['BKK']==0].shape[0],
          df_kerja[df_kerja['BKK']==1].shape[0]
    ]
    labels = ['Tidak','Ya']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Alumni Bekerja karena info dari BKK')

    st.pyplot(fig)

    st.write('Dari diagram diatas bisa disimpulkan bahwa sedikit sekali alumni yang bekerja dengan dibantu BKK terkait info dan rekrutmen, dari data ini bisa dibuat dasar agar BKK bisa lebih aktif memberikan info agar lebih banyak yang bisa terekrut')

    bkk = []
    for i in range(0,2):
        d = []
        for j in range(1,7):
            d.append(df_kerja[(df_kerja.Jurusan == j) & (df_kerja.BKK == i)].count()['BKK'])
        bkk.append(d)

    jurusan = ['Akuntansi dan Keuangan Lembaga',
            'Bisnis Daring dan Pemasaran',
            'Otomatisasi dan Tata Kelola Perkantoran',
            'Multimedia',
            'Rekayasa Perangkat Lunak',
            'Teknik Komputer dan Jaringan']

    x = np.arange(len(jurusan))
    width = 0.15

    fig, ax = plt.subplots(figsize=(20, 7))

    pk1 = ax.bar(x - width/2, bkk[0], width, label='Tidak', color='red')
    pk2 = ax.bar(x + width/2, bkk[1], width, label='Ya', color='navy')

    ax.set_title('Alumni Bekerja karena info dari BKK berdasarkan Jurusan', size=16)
    ax.set_ylabel('Jumlah', size=14)
    ax.set_xticks(x)
    ax.set_xticklabels(jurusan, size=10)
    ax.legend(fontsize=14)

    st.pyplot()
    st.write('Dan apabila dibagi per jurusan hanya jurusan Bisnis Daring dan Pemasaran saja yang berhasil bekerja dengan bantuan dan info dari BKK')

    st.subheader('Selanjutnya kita visualisasikan alumni yang bekerja apakah mendapatkan gaji sesuai dengan UMR wilayah tempat mereka bekerja atau belum ')

    counts = [
          df_kerja[df_kerja['UMR']==0].shape[0],
          df_kerja[df_kerja['UMR']==1].shape[0]
    ]
    labels = ['Tidak','Ya']
    fig, ax = plt.subplots()
    ax.pie(counts, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.title('Alumni Bekerja dengan Gaji diatas/sama dengan UMR Wilayah')

    st.pyplot(fig)

    st.write('Disini disimpulkan bahwa banyak alumni yang belum mendapatkan gaji sesuai upah minimun regional (UMR)')

    umr = []
    for i in range(0,2):
        d = []
        for j in range(1,7):
            d.append(df_kerja[(df_kerja.Jurusan == j) & (df_kerja.UMR == i)].count()['UMR'])
        umr.append(d)

    jurusan = ['Akuntansi dan Keuangan Lembaga',
            'Bisnis Daring dan Pemasaran',
            'Otomatisasi dan Tata Kelola Perkantoran',
            'Multimedia',
            'Rekayasa Perangkat Lunak',
            'Teknik Komputer dan Jaringan']

    x = np.arange(len(jurusan))
    width = 0.15

    fig, ax = plt.subplots(figsize=(20, 7))

    pk1 = ax.bar(x - width/2, bkk[0], width, label='Tidak', color='red')
    pk2 = ax.bar(x + width/2, bkk[1], width, label='Ya', color='navy')

    ax.set_title('Alumni Bekerja dengan Gaji diatas/sama dengan UMR berdasarkan Jurusan', size=16)
    ax.set_ylabel('Jumlah', size=14)
    ax.set_xticks(x)
    ax.set_xticklabels(jurusan, size=10)
    ax.legend(fontsize=14)

    st.pyplot()

    st.write('Dan dilihat dari per jurusan pun hanya jurusan Bisnis Daring dan Pemasaran dan Teknik Komputer dan Jaringan saja yang alumni nya mendapatkan gaji diatas/sama dengan UMR wilayah mereka bekerja')
elif option == 'Tes Klasifikasi':
    st.title('Machine Learning')
    st.subheader('Kita klasifikasikan apakah alumni yang bekerja bisa mendapatkan gaji sesuai atau diatas UMR berdasarkan Jenis Kelamin, Jurusan pada saat sekolah, Kota tempat mereka bekerja, Tempat Kerja telah bekerjasama dengan sekolah,Pekerjaan Alumni Linier dengan jurusan pada saat Sekolah dan terekrut dikarenakan info dan bantuan dari BKK')
    url = 'https://raw.githubusercontent.com/agus2k/gcc_data_menntah/main/Data_Mentah_Bekerja.csv'
    df_kerja = pd.read_csv(url,
            delimiter=';', 
            header='infer', 
            index_col=False)
    X = df_kerja[['Jenis_Kelamin','Jurusan','Kota','Linier','Kerjasama','BKK']]
    Y = df_kerja['UMR']


    # Import train_test_split function
    from sklearn.model_selection import train_test_split

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25,random_state=123) # 75% training and 25% test


    st.header('1. Support Vector Machine')
    #Import svm model
    from sklearn import svm
    #Create a svm Classifier
    clf = svm.SVC(kernel='linear') # Linear Kernel
    #Train the model using the training sets
    clf.fit(X_train, y_train.values.ravel())
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    from sklearn.metrics import confusion_matrix
    confusion_matrix(y_test, y_pred)

    from sklearn.metrics import classification_report
    akurasi = classification_report(y_test, y_pred)
    st.write(akurasi)
    cm = confusion_matrix(y_test, y_pred)
 
    #membuat plotting confusion matrix
    plt.figure (figsize=(10,7))
    sn.heatmap(cm, annot=True)
    plt.xlabel('Predicted')
    plt.ylabel('Truth')
    st.pyplot()

    st.write('Dari pengujian menggunakan metode Support Vector Machine akurasi yang didapatkan adalah **94%**')

    st.header('2. Naive Bayes')
    from sklearn.naive_bayes import GaussianNB
    # Mengaktifkan/memanggil/membuat fungsi klasifikasi Naive Bayes
    modelnb = GaussianNB()
    # Memasukkan data training pada fungsi klasifikasi Naive Bayes
    nbtrain = modelnb.fit(X_train, y_train.values.ravel())
    y_pred_nb = nbtrain.predict(X_test)
    st.write(classification_report(y_test, y_pred_nb))

    cm = confusion_matrix(y_test, y_pred_nb)
    
    plt.figure (figsize=(10,7))
    sn.heatmap(cm, annot=True)
    plt.xlabel('Predicted')
    plt.ylabel('Truth')

    st.pyplot()


    st.write('Dari pengujian menggunakan metode Naive Bayes akurasi yang didapatkan adalah **94%**')


    st.header('3. K-Nearest Neighbor')
    from sklearn.neighbors import KNeighborsClassifier  
    classifier = KNeighborsClassifier(n_neighbors=5)  
    classifier.fit(X_train, y_train.values.ravel())
    y_pred_knn = classifier.predict(X_test)
    from sklearn.metrics import confusion_matrix
    st.write(classification_report(y_test, y_pred_knn))

    cm = confusion_matrix(y_test, y_pred_knn)
 
    plt.figure (figsize=(10,7))
    sn.heatmap(cm, annot=True)
    plt.xlabel('Predicted')
    plt.ylabel('Truth')
    st.pyplot()
    st.write('Dari pengujian menggunakan metode K-Nearest Neighbor akurasi yang didapatkan adalah **81%**')





elif option == 'Prediksi':
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
            st.write('Dengan menggunakan metode SVM maka {} akan bekerja dengan **GAJI DIATAS/SAMA DENGAN UMR** wilayah {} dengan tingkat akurasi {}%'.format(nama,kota,round(akurasi_svm[0][1]*100),3))
        else:
            st.write('Dengan menggunakan metode SVM maka {} akan bekerja dengan **GAJI DIBAWAH UMR** wilayah {} dengan tingkat akurasi {}%'.format(nama,kota,round(akurasi_svm[0][1]*100),3))

        st.subheader('Naive Bayes')
        if hasil_nb[0]==1:
            st.write('Dengan menggunakan metode Naive Bayes maka {} akan bekerja dengan **GAJI DIATAS/SAMA DENGAN UMR** wilayah {} dengan tingkat akurasi {}%'.format(nama,kota,round(akurasi_nb[0][1]*100),3))
        else:
            st.write('Dengan menggunakan metode Naive Bayes maka {} akan bekerja dengan **GAJI DIBAWAH UMR** wilayah {} dengan tingkat akurasi {}%'.format(nama,kota,round(akurasi_nb[0][1]*100),3))

        st.subheader('K-Nearest Neighbor')
        if hasil_knn[0]==1:
            st.write('Dengan menggunakan metode KNN maka {} akan bekerja dengan **GAJI DIATAS/SAMA DENGAN UMR** wilayah {} dengan tingkat akurasi {}%'.format(nama,kota,round(akurasi_knn[0][1]*100),3))
        else:
            st.write('Dengan menggunakan metode KNN maka {} akan bekerja dengan **GAJI DIBAWAH UMR** wilayah {} dengan tingkat akurasi {}%'.format(nama,kota,round(akurasi_knn[0][1]*100),3))
        




    



