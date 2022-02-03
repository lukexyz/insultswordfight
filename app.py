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

    st.write(f'Insult: ☠️ {insult} ☠️\n')
    for zinger in st.session_state.zingers:
        st.write(f"\tComeback: `{zinger}` 🔥🔥🔥\n")


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
    with pcol2: st.image('media/monkey_island_dock_splash_transparent.png', width=400)
    with pcol3: st.write("")

    st.markdown("<h1 style='text-align: center;'>Insult Sword Fighting</h1>", unsafe_allow_html=True)
    st.write("`Pirates` ☠️ vs. 🤖 `GPT-J`") 


    # --------------------------- header  -------------------------- #
    df = get_insult_data()
    with st.expander("Examples from Monkey Island 🌄", expanded=False):
        st.write("* Insult Sword Fighting is a battle of wits from the 90s game [Monkey Island](https://monkeyisland.fandom.com/wiki/Insult_Sword_Fighting).")
        st.write("* As you progress you learn more insults, and more importantly, know when to use them.")
        st.image('media/The_Making_of_Monkey_Island_30th_Anniversary_Documentary.gif')
        st.write('Here are some of the original insult/comback pairs from the game, which form the training dataset.')
        st.table(df.head(5))
        st.write("You can try using some of these insults to get started, but it's more fun coming up with your own 💅")


    client = nlpcloud.Client("gpt-j", st.secrets["nlpcloud_token"], gpu=True)
    df = get_insult_data()

    insults = [ "test insult", 
                "I've seen better moves in a senior citizen Zumba class!",
                "This girl is the nastiest skank bitch I've ever met"]
 
    insult = st.text_input(label="☠️ Submit Your Insult ☠️", value=insults[2])

    if st.button('Fire!'):
        st.session_state.fire_flag = True

    placeholder_a = st.empty()

    if st.session_state.fire_flag == True:
        with placeholder_a.container():
            fight(insult, client, df)
            st.session_state.fire_flag = False

    st.write("")
    st.markdown("---")

    if st.session_state.zingers:
        st.write('Been hurt by a savage zinger? Share it in the burn book 💔💔💔')
        with st.expander("Open Burnbook", expanded=False):
            # if insult not in example_insults
            zinger = st.session_state.zingers

            if zinger:
                st.write(f'Insult: ☠️ {insult} ☠️\n')
                if st.session_state.zingers[0]:
                    st.write(f'\tComeback: `{zinger}` 🔥🔥🔥\n')
                    if st.button('+ add to burn book'):
                        data = {'time_utc':utc_now(), 'insult':f"☠️ {insult} ☠️",
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



if __name__ == '__main__':
    st.set_page_config(page_title="Insult Sword Fighting",
        page_icon="☠️",
        layout="centered",
        initial_sidebar_state="auto")
    main()