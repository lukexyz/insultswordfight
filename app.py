import os
import time
import pandas as pd
import streamlit as st
import nlpcloud

from insultswordfight.core import get_insult_data, create_input_string, generate_comeback

from prodb.core import generate_db, insert_row, utc_now, readable_df
import arrow


def fight(insult, client, df): 
    outputs = 1
    training_examples = 7

    if insult == "test insult": st.session_state.zingers = ['comeback #1', "comeback #2"]
    else: 
        st.session_state.zingers = generate_comeback(insult, client, df, outputs, training_examples)
        st.session_state.count += outputs

    ecol1, ecol2 = st.columns([2,12])
    with ecol1: st.image('media/guybrush-threepwood50.gif')

    with ecol2: 
        st.write(f'Insult: ☠️ {insult} \n')
        for zinger in st.session_state.zingers:
            st.write(f"\tComeback 🤖: `{zinger}` 🔥🔥🔥\n")



def burn_book():
    col1, col2 = st.columns([1, 1])
    with col2:
        with st.form(key='my_form'):
            submission = st.selectbox("Select", st.session_state.zingers)
            submit_form = st.form_submit_button(label='Submit')
            if submit_form: 
                st.balloons()





def main():

    # -------------------- initialize burn book -------------------- #
    dbpath = 'bb.csv'
    if not os.path.isfile(dbpath): 
        bb = generate_db(dbpath=dbpath, cols=['time_utc', 'insult', 'comeback'])
    else: bb = pd.read_csv(dbpath)

    # ------------------------ control flow ------------------------ #
    if 'count' not in st.session_state: 
        st.session_state.count = 0
        st.session_state.fire_flag = False
        st.session_state.burn_book_flag = False
        st.session_state.zingers = []

    # --------------------------- header  -------------------------- #
    # Hack for centering image
    pcol1, pcol2, pcol3 = st.columns([1,3,1])
    with pcol1: st.write("")
    with pcol2: st.image('media/Splash_Header_small.png')
    with pcol3: st.write("")

    st.markdown("<h2 style='text-align: center;'>Insult Sword Fighting</h2>", unsafe_allow_html=True)
    st.write("`Pirates` ☠️ vs. 🤖 `GPT-J`") 


    # --------------------------- header  -------------------------- #
    df = get_insult_data()
    with st.expander("Learn more about Monkey Island 🌄", expanded=False):
        st.write("`Insult Sword Fighting` is a word-puzzle from the video game [Monkey Island](https://monkeyisland.fandom.com/wiki/Insult_Sword_Fighting) (1990). As you progress through the game you learn more insults, and win fights by using the right comeback at the right time.")
        ecol1, ecol2, ecol3 = st.columns([1,4,1])
        with ecol1: st.write("")
        with ecol2: st.image('media/The_Making_of_Monkey_Island_30th_Anniversary_Documentary_cropped.gif')
        with ecol3: st.write("")
        
        st.write('Here are some of the original insult/comback pairs from the game, which form the training dataset.')
        rows = st.slider('How many training exmples to display?', 1, 15, 5)
        st.table(df.head(rows))
        st.write("`You can try using some of these insults to get started, but it's more fun coming up with your own!` 💅")

    st.write("")
    client = nlpcloud.Client("gpt-j", st.secrets["nlpcloud_token"], gpu=True)
    df = get_insult_data()

    insults = [ "test insult", 
                "I've seen better moves in a senior citizen Zumba class!",
                "This girl is the nastiest skank bitch I've ever met"]

    icol1, icol2 = st.columns([5,1])
    with icol1: insult = st.text_input(label="👇 Input your insult", value=insults[1])
    with icol2: generate_button = st.button('🤖 Generate Comeback ')
    if generate_button: st.session_state.fire_flag = True


    placeholder_a = st.empty()

    if st.session_state.fire_flag == True:
        with placeholder_a.container():
            fight(insult, client, df)
            st.session_state.fire_flag = False


    st.write("")
 

    if st.session_state.zingers:
        st.markdown("---")
        st.markdown("<p1 style='text-align: right; color: black;'> <i>Been hurt by a savage zinger? We're here to help.</i></p1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: right; color: black;'> Share it in the burn book 💔 </h3>", unsafe_allow_html=True)
        with st.expander("Open Burnbook", expanded=False):
            # if insult not in example_insults
            zinger = st.session_state.zingers

            if zinger:
                st.write(f'Insult: ☠️ {insult}\n')
                if st.session_state.zingers[0]:
                    st.write(f'\tComeback 🤖: `{zinger}` 🔥🔥🔥\n')
                    if st.button('+ add to burn book'):
                        data = {'time_utc':utc_now(), 'insult':f"☠️ {insult}",
                                'comeback': st.session_state.zingers[0]+" 🔥🔥🔥"}
                        bb = insert_row(bb, data, dbpath)
            else: st.write('Generate zinger above')

            st.table(readable_df(bb, max_rows=5)[['human_time', 'insult', 'comeback']][::-1])
    # -------------------------------------------------------- #
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(f'API count = `{st.session_state.count}`')

    # Custom button colours
    m = st.markdown("""
            <style>
            div.stButton > button:first-child {
                background-color: #0099ff;
                color:#ffffff;
            }
            div.stButton > button:hover {
                background-color: #00ff00;
                color:#ff0000;
                }
            </style>""", unsafe_allow_html=True)

if __name__ == '__main__':
    st.set_page_config(page_title="Insult Sword Fighting",
        page_icon="☠️",
        layout="centered",
        initial_sidebar_state="auto")
    main()