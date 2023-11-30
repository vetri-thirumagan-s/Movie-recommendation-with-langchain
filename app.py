import streamlit as st
import model


st.set_page_config("Movie recommendation")
st.title("MOVIE RECOMMENDATION")
movie_name=st.text_input('Enter the movie you like to watch')

if movie_name:
    output=model.recommend(movie_name)
    st.write(output)