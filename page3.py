import streamlit as st
def page_3():
    st.title("Taraaaaaa")
    st.write('Ini dia salah satu kejutannya. Halaman ini Menampilkan Rumus Matematika')
    st.write('Sebelum nonton kartun, yuk belajar matematika bareng. Jangan lupa tonton video dibawah ini yaa^^')
    st.video('https://youtu.be/BfrBmOqN-Aw?si=uiCHtTZZsowz0YhK')
    st.write('Matematika ilmu yang menyenangkan bukan?')
    with open('Untitled61 (1).md','r') as file:
        isi_teks = file.read()
    st.markdown(isi_teks)