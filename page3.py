import streamlit as st
def page_3():
    st.title("Halaman 3")
    st.write('Halaman ini Menampilkan Rumus Matematika Turunan Fungsi')
    
    with open('Untitled61 (1).md','r') as file:
        isi_teks = file.read()
    st.markdown(isi_teks)