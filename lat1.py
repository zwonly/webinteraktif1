import streamlit as st
from page1 import page_1
from page2 import page_2
from page3 import page_3
from page4 import page_4
from page5 import page_5
#import pandas as pd
#import matplotlib.pyplot as plt
# st.write("Coding Club 2024 Rev")
# df = pd.DataFrame({
#     'No': [1,2,3,4],
#     'Names': ['Angga','Nadlip','Zahwa','Nadia'],
#     'Nilai': [80,23,99,8]
# })

# df

PAGES = {
    "Page 1" : page_1,
    "Page 2" : page_2,
    "Page 3" : page_3,
    "Page 4" : page_4,
    "Page 5" : page_5
}

st.sidebar.image("cropped_image.png", width=180)
page = st.sidebar.radio("Pages", list(PAGES.keys()))
PAGES[page]()
