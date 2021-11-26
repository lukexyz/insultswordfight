import streamlit as st
from insultswordfight.core import create_input_string, generate_comeback

st.set_page_config(page_title="Insult Sword Fighting", page_icon="☠️")

if 'count' not in st.session_state:
    st.session_state.count = 0

# -------------------------------------------------------- #
with st.expander("The Curse of Monkey Island 🌄", expanded=False):
    st.write("They are zingers")
    st.write("")

st.header('Insult Sword Fighting')
st.write("`Pirates` ☠️ vs. 🤖 `GPT-J`")

# -------------------------------------------------------- #

t = create_input_string("People fall at my feet when they see me coming!", training_examples=3)
st.write(t)

if st.button(label='Run'):
    st.session_state.count += 1

st.write('Current Count = ', st.session_state.count)

