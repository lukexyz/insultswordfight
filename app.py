import os
import time
import pandas as pd
import streamlit as st
import nlpcloud
from insultswordfight.core import get_insult_data, create_input_string, generate_comeback

st.set_page_config(page_title="Insult Sword Fighting", page_icon="☠️")

if ['count', 'fire', 'zingers', 'burn_book'] not in st.session_state:
    st.session_state.count = 0
    st.session_state.zingers = ""
    st.session_state.burn_book = False
    st.session_state.burn_book = False

# -------------------------------------------------------- #
with st.expander("Learn more about Monkey Island 🌄", expanded=False):
    st.write("The Curse of Monkey Island (1995)")
    st.write("")

st.header('Insult Sword Fighting')
st.write("`Pirates` ☠️ vs. 🤖 `GPT-J`") 

# -------------------------------------------------------- # 


client = nlpcloud.Client("gpt-j", st.secrets["nlpcloud_token"], gpu=True)
df = get_insult_data()

insults = [ "test insult", 
            "This girl is the nastiest skank bitch I've ever met!",
            "I've seen better fighting in a senior citizen Zumba class!"]

insult = st.text_input(label="Input", value=insults[0])

st.session_state.fire = st.button(label='Fire!')
if st.session_state.fire:
    #st.session_state.burn_book = False
    outputs = 1
    if insult == "test insult": st.session_state.zingers = ['comeback #1', "comeback #2"]
    else: 
        st.session_state.zingers = generate_comeback(insult, client, df, outputs, training_examples=7)
        st.session_state.count += outputs

    st.write(f'Insult: ☠️ {insult} ☠️\n')
    for zinger in st.session_state.zingers:
        st.write(f"\tComeback: `{zinger}` 🔥🔥🔥\n")


# submit to burn book
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("submit to burn book +"):
        st.session_state.burn_book = True
    #st.session_state.burn_book = False


if st.session_state.burn_book == True:
    with st.form(key='my_form'):
        submission = st.selectbox("Select", st.session_state.zingers)
        submit_form = st.form_submit_button(label='Submit')
        if submit_form: 
            st.balloons()
    
    # if st.button('Submit'):
    #     
    #     st.write(f'You submitted {submission} to the burn book')

st.write("")
st.write('Burn book', st.session_state.burn_book)
st.write('zingers', st.session_state.zingers)
st.write(f'API count = `{st.session_state.count}`')
