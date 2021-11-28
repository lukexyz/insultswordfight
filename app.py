import os
import time
import pandas as pd
import streamlit as st
import nlpcloud
from insultswordfight.core import get_insult_data, create_input_string, generate_comeback


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
    # ------------------------ control flow ------------------------ #
    if 'count' not in st.session_state: 
        st.session_state.count = 0
        st.session_state.fire_flag = False
        st.session_state.burn_book_flag = False
        st.session_state.zingers = []

    # --------------------------- header  -------------------------- #
    with st.expander("More about Monkey Island 🌄", expanded=False):
        st.write("The Curse of Monkey Island (1995)")
        st.write("")

    st.markdown("<h1 style='text-align: center;'>Insult Sword Fight</h1>", unsafe_allow_html=True)
    st.write("`Pirates` ☠️ vs. 🤖 `GPT-J`") 

    client = nlpcloud.Client("gpt-j", st.secrets["nlpcloud_token"], gpu=True)
    df = get_insult_data()

    insults = [ "test insult", 
                "I've seen better moves in a senior citizen Zumba class!",
                "This girl is the nastiest skank bitch I've ever met"]

    st.write(df.Insult.head(5))
    insult = st.text_input(label="Input", value=insults[0])

    if st.button('Fire!'):
        st.session_state.fire_flag = True

    placeholder_a = st.empty()

    if st.session_state.fire_flag == True:
        with placeholder_a.container():
            fight(insult, client, df)

            col1, col2 = st.columns([2, 1])
            with col2:
                st.write("")
                st.write("")
                if st.button('+ add to burn book'):
                    st.session_state.burn_book_flag = True
            placeholder_b = st.empty()
            if st.session_state.burn_book_flag == True:

                with placeholder_b.container():
                    burn_book()
                    col1, col2 = st.columns([2, 1])
                    with col2:
                        if st.button('- close burn book'):
                            st.session_state.burn_book_flag = False
                            placeholder_b.empty()

            if st.button('Reset'):
                st.session_state.fire_flag = False
                placeholder_a.empty()

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