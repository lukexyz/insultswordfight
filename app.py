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
    with st.expander("Monkey Island 🌄", expanded=False):
        st.write("The Curse of Monkey Island (1995)")
        st.write("")

    st.markdown("<h1 style='text-align: center;'>Insult Sword Fight</h1>", unsafe_allow_html=True)
    st.write("`Pirate` ☠️ vs. 🤖 `GPT-J`") 

    client = nlpcloud.Client("gpt-j", st.secrets["nlpcloud_token"], gpu=True)
    df = get_insult_data()

    insults = [ "test insult", 
                "I've seen better moves in a senior citizen Zumba class!",
                "This girl is the nastiest skank bitch I've ever met"]

    st.write(df.Insult.head(5))
    insult = st.text_input(label="Input", value=insults[2])

    if st.button('Fire!'):
        st.session_state.fire_flag = True

    placeholder_a = st.empty()

    if st.session_state.fire_flag == True:
        with placeholder_a.container():
            fight(insult, client, df)
    st.write('if you got burnt by a savage zinger, share it in the burn book')
    if st.button('add to burn book v2'):
        data = {'time_utc':utc_now(), 'insult':insult, 'comeback': st.session_state.zingers[0]}
        bb = insert_row(bb, data, dbpath)

    st.table(readable_df(bb, max_rows=10))
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