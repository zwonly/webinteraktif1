import streamlit as st
from PIL import Image,ImageFilter
import io

def konversi_gambar(image, format):
    gambar_konversi = image.convert("RGB")
    image_bytes = io.BytesIO()
    gambar_konversi.save(image_bytes, format = format)
    return image_bytes.getvalue()
def buat_filter(image, jenis_filter):
    if jenis_filter == "BLUR":
        gambar_filter = image.filter(ImageFilter.BLUR)
    elif jenis_filter == "CONTOUR":
        gambar_filter = image.filter(ImageFilter.CONTOUR)
    elif jenis_filter == "EMBOSS":
        gambar_filter = image.filter(ImageFilter.EMBOSS)
    elif jenis_filter == "SHARPEN":
        gambar_filter = image.filter(ImageFilter.SHARPEN)
    elif jenis_filter == "FIND_EDGES":
        gambar_filter = image.filter(ImageFilter.FIND_EDGES)
        
    return gambar_filter

def main():
    unggah_gambar = st.file_uploader('Pilih Gambar:', type=["jpg","jpeg","png"])
    if unggah_gambar is not None :
        gambar = Image.open(unggah_gambar)
        kolom1, kolomtengah, kolom2 =st.columns(3)
        pilih_filter = kolomtengah.selectbox("Pilih Jenis Filter",["BLUR","CONTOUR","EMBOSS","SHARPEN","FIND_EDGES"])
        
        kolom1.image(gambar, caption="Gambar Asli", width=200)
        filtered_image = buat_filter(gambar,pilih_filter.upper())
        kolom2.image(filtered_image,caption="Hasil Filter",width=200)
        
        image_bytes = konversi_gambar(filtered_image,"PNG")
        kolomtengah.download_button(label="Download", data = image_bytes, file_name="Hasilzahwa.png")