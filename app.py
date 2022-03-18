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
        bb = generate_db(dbpath=dbpath, cols=['time_utc', 'mood', 'insult', 'comeback'])
    else: bb = pd.read_csv(dbpath)

    # ------------------------ control flow ------------------------ #
    if 'count' not in st.session_state: 
        st.session_state.count = 0  # API count
        st.session_state.fire_flag = False
        st.session_state.burn_book_flag = False
        st.session_state.zingers = []
        st.session_state.page_nav = "frontpage"

    # --------------------------- header  -------------------------- #
    # Hack for centering image
    pcol1, pcol2, pcol3 = st.columns([1,4,1])
    with pcol1: st.write("")
    with pcol2: st.image('media/Vertical_Intro_Splash_3.jpg')
    with pcol3: st.write("")

    if st.session_state.page_nav == "frontpage":
        #st.markdown("<h2 style='text-align: center;'>Insult Sword Fighting</h2>", unsafe_allow_html=True)
        gcol1, gcol2, gcol3 = st.columns([1,1,1])
        with gcol1: st.write("")
        with gcol2: st.write("`Pirates` ☠️ vs. 🤖 `GPT-J`") 
        with gcol3: st.write("")
        
        # --------------------------- header  -------------------------- #
        df = get_insult_data()
        with st.expander("Monkey Island? Insult Sword Fighting? 🌄", expanded=False):
            st.write("`Insult Sword Fighting` is a puzzle from the 1990 video game [Monkey Island](https://monkeyisland.fandom.com/wiki/Insult_Sword_Fighting). Throughout the game you learn new insults, and win fights by using the right comeback at the right time.")
            ecol1, ecol2, ecol3 = st.columns([1,4,1])
            with ecol1: st.write("")
            with ecol2: st.image('media/The_Making_of_Monkey_Island_30th_Anniversary_Documentary_cropped.gif')
            with ecol3: st.write("")
            st.write("Below you can submit an insult, and the app will generate a devastating comeback that will leave you broken and afraid. For example,")
            
            pcol1, pcol2, pcol3 = st.columns([1,3,1])
            with pcol1: st.write("")
            with pcol2: st.image('media/hurt_feelings.JPG')
            with pcol3: st.write("")
            
            st.write('Here are some of the original `Insult : Comeback` pairs from the game. These form the training dataset using [few-shot learning](https://nlpcloud.io/effectively-using-gpt-j-gpt-neo-gpt-3-alternatives-few-shot-learning.html) and the [GPT-J language model](https://huggingface.co/EleutherAI/gpt-j-6B).')
            rows = st.slider('How many training examples to display?', 1, 15, 5)
            st.table(df.head(rows))
            st.write("`You can try using some of these insults to get started, but it's more fun coming up with your own!` 💅")

        st.write("")
        client = nlpcloud.Client("gpt-j", st.secrets["nlpcloud_token"], gpu=True)
        df = get_insult_data()

        insults = [ "test insult", 
                    "My great grandmother can fight better than you!",
                    "I've seen better moves in a senior citizen Zumba class!",
                    "This girl is the nastiest skank bitch I've ever met"]

        icol1, icol2 = st.columns([5,1])
        with icol1: insult = st.text_input(label="👇 Type your insult", value=insults[1])
        with icol2: generate_button = st.button('🤖 Generate Comeback ')
        if generate_button: st.session_state.fire_flag = True

        placeholder_a = st.empty()

        if st.session_state.fire_flag == True:
            with placeholder_a.container():
                if any(word in insult.lower() for word in st.secrets["banned_words"].split()): 
                    insult = "I am an asshole"
                fight(insult, client, df)
                st.session_state.fire_flag = False

        st.write("")

        if st.session_state.zingers:
            st.markdown("---")
            st.markdown("<p1 style='text-align: right; color: black;'> <i>Been hurt by a savage zinger? Share it in the burn book.</i></p1>", unsafe_allow_html=True)
            if st.session_state.count > 1: # pro UX move
                expand = True
            else: expand = False
            with st.expander("Open burn book", expanded=expand):
                # if insult not in example_insults
                zinger = st.session_state.zingers
                if zinger:
                    st.write(f'Insult: ☠️ {insult}\n')
                    if st.session_state.zingers[0]:
                        st.write(f'\tComeback 🤖: `{zinger}` 🔥🔥🔥\n')

                        c1, c2 = st.columns((1, 7))
                        emoji = '🔥🔥 😲 😭 😎 👹 ☠️ 💅 😇 💖'.split(" ")
                        feel = c1.selectbox('Feeling', emoji)
                        c2.write('')
                        c2.write('')
                        if c2.button('+ add to burn book 🍒'):
                            data = {'time_utc':utc_now(),
                                    'mood':feel,
                                    'insult':f"{insult}",
                                    'comeback': st.session_state.zingers[0]}
                            bb = insert_row(bb, data, dbpath)
                        
                    else: st.write('Generate zinger above')
                placeholder = st.empty()

                # ================= metrics ================= #
                col0, col1, col2, col3 = st.columns([1, 1, 1, 1])
                file_size = os.path.getsize(dbpath)
                col0.metric(f"💾 {dbpath}", f"{bb.shape[0]}", "total rows")
                col1.metric("📁 filesize", f"{file_size/1000:0.2f}", 'kb')
                burn_rows = col3.slider('🎲 latest burns', 1, min(25, bb.shape[0]), 6)
                #col3.image('media/burnbook_img.png', width=200)

                placeholder.table(readable_df(bb, max_rows=50)[['human_time', 'mood', 'insult', 'comeback']][::-1].rename(columns={"human_time": "when"}).iloc[:burn_rows, :])
                with open(dbpath, 'rb') as f:
                    st.download_button('Download .csv', f, file_name='burnbook.csv')


        # -------------------------------------------------------- #
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        f1, f2 = st.columns((4,1))
        f2.write("Source 🌐 [Github](https://github.com/lukexyz/insultswordfight)")
        #st.write(f'API count = `{st.session_state.count}`')

        # Custom button colours
        m = st.markdown("""
                <style>
                div.stButton > button:first-child {
                    background-color: #1F43B2;
                    color:#ffffff;
                }
                div.stButton > button:hover {
                    background-color: #FF5FFD;
                    color: #000000;
                    }
                </style>""", unsafe_allow_html=True)

    elif st.session_state.page_nav == "burnbook":
        st.markdown("<h2 style='text-align: center;'>Secrets from the Burn Book</h2>", unsafe_allow_html=True)
        bcol1, bcol2 = st.columns([12, 3])
        with bcol2: st.image('media/burnbook_img.png', width=120)
        with bcol1: st.warning('"With great power, comes great responsibility" - Mêlée Island Sword Master')
        st.table(readable_df(bb, max_rows=20)[['human_time', 'mood', 'insult', 'comeback']][::-1].head(20))
        if st.button('🖱️🖱️ Double Click for Frontpage'): 
            st.session_state.page_nav = "frontpage"
            st.session_state.zingers = []
            

if __name__ == '__main__':
    st.set_page_config(page_title="Insult Sword Fighting",
        page_icon="☠️",
        layout="centered",
        initial_sidebar_state="auto")

    # Remove streamlit boilerplate
    hide_streamlit_style = """
        <style>
        /* This is to hide hamburger menu completely */
        #MainMenu {visibility: hidden;}
        /* This is to hide Streamlit footer */
        footer {visibility: hidden;}
        /*
        If you did not hide the hamburger menu completely,
        you can use the following styles to control which items on the menu to hide.
        */
        ul[data-testid=main-menu-list] > li:nth-of-type(4), /* Documentation */
        ul[data-testid=main-menu-list] > li:nth-of-type(5), /* Ask a question */
        ul[data-testid=main-menu-list] > li:nth-of-type(6), /* Report a bug */
        ul[data-testid=main-menu-list] > li:nth-of-type(7), /* Streamlit for Teams */
        ul[data-testid=main-menu-list] > div:nth-of-type(2) /* 2nd divider */
            {display: none;}
        </style>
    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # Remove padding from top of page
    padding = 0
    st.markdown(f""" <style>
        .reportview-container .main .block-container{{
            padding-top: {padding}rem;
        }} </style> """, unsafe_allow_html=True)

    main()