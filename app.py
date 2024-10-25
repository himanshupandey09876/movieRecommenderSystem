import streamlit as st
import pickle
import time
import pandas as pd
from recommend import recommend
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

st.title('WELCOME TO #P RECOMMENDATIONS')

selected_movie = st.selectbox(
    'Which number do you like best?',
     movies['title'].values)


# if st.button("Recommend"):
#     recommendationsmovie,recommendationsposter=recommend(selected_movie)
#     for recommov in recommendationsmovie:
#         st.write(recommov)

if st.button("Recommend"):
     
     recommendationsmovie,recommendationsposter=recommend(selected_movie)
     cols=st.columns(5)   
     for col,movie,poster in zip(cols,recommendationsmovie,recommendationsposter):
          with col:
               st.text(movie)
               st.image(poster)
    
if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False
    st.session_state.show_image = False

if not st.session_state.button_clicked:
    if st.button("GIFT FOR MY-Dear One's; PEOPLE JUST CLICK ME"):
        st.session_state.button_clicked = True
        st.session_state.show_image = True
        st.experimental_rerun()

if st.session_state.show_image:
    st.header("PAGAL BANAYA TUMKO")
    st.image("https://media1.tenor.com/m/hYo-YcEBW4UAAAAC/chutiya-banaya-tumko-mirzapur.gif")
    time.sleep(5)
    st.session_state.show_image = False
    st.experimental_rerun()


# if st.button("GIFT FOR CHHICHORE PEOPLE JUST CLICK ME"):
#      st.header("SBKO GIRLFRIEND MILEGI IIT MEI AASHIRVAAD")
#      st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTndyLifLazHgxyVfGDD60nIu9JT02HbqSZcA&s")