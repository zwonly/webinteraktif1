import streamlit as st
def page_3():
    st.title("Halaman 3")
    st.write('Halaman ini Menampilkan Rumus Matematika')
    st.write('Setelah nonton kartun, yuk belajar matematika bareng. Matematika ilmu yang menyenangkan bukan? Jangan lupa ditonton yaa^^')
    st.video('https://youtu.be/BfrBmOqN-Aw?si=uiCHtTZZsowz0YhK')
    with open('Untitled61 (1).md','r') as file:
        isi_teks = file.read()
    st.markdown(isi_teks)