import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
# st.write("Coding Club 2024 Rev")
# df = pd.DataFrame({
#     'No': [1,2,3,4],
#     'Names': ['Angga','Nadlip','Zahwa','Nadia'],
#     'Nilai': [80,23,99,8]
# })

# df

def page_1():
    st.title("Halaman 1")
    st.write('Halaman ini digunakan untuk Intro')
def page_2():
    st.title("Halaman 2")
    st.write('Halaman ini digunakan untuk Menampilkan Youtube')
def page_3():
    st.title("Halaman 3")
    st.write('Halaman ini digunakan untuk Menampilkan Rumus Matematika')
    
PAGES = {
    "Page 1" : page_1,
    "Page 2" : page_2,
    "Page 3" : page_3
}

st.sidebar.image("zahwa.jpeg", width=200)
page = st.sidebar.radio("Halaman", list(PAGES.keys()))
PAGES[page]()
