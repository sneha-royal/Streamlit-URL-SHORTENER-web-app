import streamlit as st
import pyshorteners as pyst
import pyperclip
shortener=pyst.Shortener()
def copying():
    pyperclip.copy(shorted_url)
with open("url.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>",unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center;'>URL SHORTENER",unsafe_allow_html=True)
form=st.form("name")
url=form.text_input("URL HERE")
s_btn=form.form_submit_button("SHORT")

if s_btn:
    shorted_url=shortener.tinyurl.short(url)
    #print(shorted_url)
    st.markdown("<h3>Shorted Url</h3",unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align:center;'>{shorted_url}</h6>",unsafe_allow_html=True)
    st.button("copy",on_click=copying)

