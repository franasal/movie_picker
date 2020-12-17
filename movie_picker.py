import pandas as pd
from random import randint
from time import sleep
import streamlit as st

st.title(':movie_camera: AWESOME MOVIE PICKER :movie_camera:')
st.header("For CAFE' s WG")

# @st.cache
def get_movie_data():

    df = pd.read_excel("https://docs.google.com/spreadsheets/d/e/2PACX-1vRnJSiajjr_c9JvB-AwFGXJftAKUcZSKSylD4yhJRojK30bZO5BNxeIVafRACILnKAZIRsMlKbGKJZK/pub?output=xlsx",
                                    sheet_name=0)
    return df

def main():
    df = get_movie_data()

    st.header("Pick some genres:")
    st.info("Please make a genre selection (or leave it empty to use the whole list).")
    genres = st.multiselect("",list(df.GENRE.unique()), []
    )

    if st.button('Pick a movie!'):
        choose_film(df, genres)
            # clf, confusion_matrix = train_rf(df, cols_to_train)
        st.balloons()
            # st.pyplot(confusion_matrix)

    st.write("\n\n:point_up:Dont't forget to mark this movie as watched on the [Movie List](https://docs.google.com/spreadsheets/d/1kpLW_3n1OtmTDNneaGUMG5ch94RD_wt5QzNoLChPRt4/edit#gid=0)")



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
    print('genres_list')
    movie_df['WATCHED'] = movie_df['WATCHED'].astype('bool')

    filt_movs=movie_df[movie_df['WATCHED']==False]
    filtered_movies=(filt_movs[filt_movs[
        'GENRE'].isin(genres_list)])
    print(filtered_movies)
    random_num=randint(1, len(filtered_movies)-1)
    if genres_list:
        st.text(f"performing super complex calculations\nto pick an awesome {genres_list} movie ")
    else:
        st.text(f"performing super complex calculations\nto pick an awesome movie ")
    st.header(" \n\n Tonight you will watch: ")
    print_prog_bar()


    st.title(f":fire: {filtered_movies['MOVIE_TITLE'][random_num]} :fire:")

# selected_genres

if __name__ == "__main__":
    main()
