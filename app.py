import os
import pandas as pd
import streamlit as st
import nlpcloud
from insultswordfight.core import get_insult_data, create_input_string, generate_comeback

st.set_page_config(page_title="Insult Sword Fighting", page_icon="☠️")

if 'count' not in st.session_state:
    st.session_state.count = 0

# -------------------------------------------------------- #
with st.expander("Learn more about Monkey Island 🌄", expanded=False):
    st.write("The Curse of Monkey Island (1995)")
    st.write("")

st.header('Insult Sword Fighting')
st.write("`Pirates` ☠️ vs. 🤖 `GPT-J`") 

# -------------------------------------------------------- # 


client = nlpcloud.Client("gpt-j", st.secrets["nlpcloud_token"], gpu=True)
df = get_insult_data()

insults = ["This girl is the nastiest skank bitch I've ever met!",
           "I've seen better fighting in a senior citizen Zumba class!"]

insult = st.text_input(label="Input", value="This girl is the nastiest skank bitch I've ever met!")

if st.button(label='Run'):
    outputs = 2
    zingers = generate_comeback(insult, client, df, outputs, training_examples=7)
    st.session_state.count += outputs

    st.write(f'Insult: ☠️ {insult} ☠️\n')
    for zinger in zingers:
        st.write(f"\tComeback: `{zinger}` 🔥🔥🔥\n")

    # submit to burn book

st.write(f'API count = `{st.session_state.count}`')