import pandas as pd
from random import randint
from time import sleep
import streamlit as st

st.title(':movie_camera: AWESOME MOVIE PICKER :movie_camera:')
st.header('For CAFE')

# @st.cache
def get_movie_data():

    df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRnJSiajjr_c9JvB-AwFGXJftAKUcZSKSylD4yhJRojK30bZO5BNxeIVafRACILnKAZIRsMlKbGKJZK/pub?output=csv", sep=',')
    return df



def main():
    df = get_movie_data()

    st.header("Pick some genres:")
    genres = st.multiselect(
        "(or leave it empty to use the whole list)", list(df.GENRE.unique()), []
    )
    if not genres:
        st.warning("Please select at least one genre.")

    if st.button('Pick a movie!'):
        choose_film(df, genres)
            # clf, confusion_matrix = train_rf(df, cols_to_train)
        st.balloons()
            # st.pyplot(confusion_matrix)



def print_prog_bar():
    """just for fun"""
    progress_bar = st.progress(0)
    for i in range(1,101):
        progress_bar.progress(i)
        sleep(0.025)

def choose_film(movie_df, genres_list):
    """
    a movie picker for the wg 77a2R!!!
    """

    filtered_movies=(movie_df[movie_df[
        'GENRE'].isin(genres_list) & movie_df['WATCHED']==False])
    random_num=randint(1, len(filtered_movies)-1)
    st.text(f"performing super complex calculations\nto pick an awesome {genres_list} movie ")
    st.header(" \n\n Tonight you will watch: ")
    print_prog_bar()


    st.title(f":fire:{filtered_movies['MOVIE_TITLE'][random_num]}:fire::fire:")

# selected_genres

if __name__ == "__main__":
    main()
