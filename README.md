<p align="center">
  <img src="https://raw.githubusercontent.com/lukexyz/insultswordfight/master/media/splash_header_3_small.jpg" width=60%> 
  <h1 align="center">☠️ <a href="https://lukexyz-insultswordfight-app-skg8pm.streamlitapp.com/">Insult Sword Fighting</a> ☠️</h1>
</p>

<p align="center">
<a href="Open In Streamlit"><del>https://lukexyz-insultswordfight-app-skg8pm.streamlitapp.com/</del></a> 
</p>

Built with [streamlit](streamlit.io) and `GPT-J` using few shot learning with [nlpcloud](nlpcloud.io).

# Community Zingers 🔥🔥🤨
Worst of the worst. Third degree burns submitted by users to the [**📓 `burn_book`**](./data/premium_zingers.csv) from over a thousand users on the subreddit.

> → 📓 [burnbook_prod.csv](./data/burnbook_prod.csv)  

> → ⚠️⚠️ [**premium_zingers.csv**](./data/premium_zingers.csv)

## Vanilla Zingers (example) 🍒

☠️ Insult: I once owned a dog that was smarter than you. ☠️  
`Comeback: (0) I hope you lost him.` 🔥🔥🔥

☠️ Insult: Heaven preserve me! You look like something that's died! ☠️  
`Comeback: (0) If you ever need an autopsy, I'd be glad to do it.` 🔥🔥🔥

☠️ Insult: Killing you would be justifiable homicide! ☠️  
`Comeback: (0) Unless it was murder, then you'd be guilty of suicide.` 🔥🔥🔥  
<br />

<p align="center">
  <img src="https://raw.githubusercontent.com/lukexyz/insultswordfight/master/media/grandma_insult.PNG" width=60%>  
</p>

## Few Shot Learning

Using the monkey island insult database, I create a text block showing the examples which I want the model to emulate. In this case, it's 3 pairs of `insult`: `comeback` pairs.

The final portion is the user input `insult`, and then the non-closure text "`comeback: `". This gives the language model no other option but to reply with what it thinks is the most appropriate response.

```py
# example API call
generation = client.generation("""Insult: You fight like a dairy Farmer!
            Comeback: How appropriate. You fight like a cow!
            ###
            Insult: This is the END for you, you gutter crawling cur!
            Comeback: And I've got a little TIP for you, get the POINT?
            ###
            Insult: I've spoken with apes more polite than you!
            Comeback: I'm glad to hear you attended your family reunion!
            ###
            Insult: Soon you'll be wearing my sword like a shish kebab!
            Comeback: First you'd better stop waving it like a feather duster.
            ###
            Insult: I once owned a dog that was smarter than you.
            Comeback: """,
    max_length=100,
    length_no_input=True,
    end_sequence="\n###",
    remove_input=True)

print('\n🔥🔥🔥 ', generation["generated_text"])
```

And few-shot learning in illustrated form,

<p align="center">
  <img src="https://raw.githubusercontent.com/lukexyz/insultswordfight/master/media/few_shot_learning.PNG" width=50%>  
</p>


## Development Notebook using `GPT-J`

> :bookmark_tabs: [zingers_GPT-J.ipynb](https://github.com/lukexyz/insultswordfight/blob/master/notebooks/00_zingers_GPT-J.ipynb)

## Online App

Streamlit script

> :bookmark_tabs: [app.py](https://github.com/lukexyz/insultswordfight/blob/master/app.py)

The web app is running online at [~~pirateinsults.com~~](http://pirateinsults.com), which allows you to try out different insults, and add them to the hall of fame if you wish.

The web app is created with streamlit, hosted (free) by streamlit.io, and I've created a blind redirect for a custom domain [~~pirateinsults.com~~](http://pirateinsults.com) to go to the internal streamlit IP they gave me.

<p align="center"><del>
<a href="https://pirateinsults.com">www.pirateinsults.com</a> </del>
</p>
<p align="center">
  <a href="https://pirateinsults.com">
  <img src="https://raw.githubusercontent.com/lukexyz/insultswordfight/master/media/full_screenshot1_border.PNG" width=50%> 
  </a>
</p>

## References

ISF at Monkey Island Fandom 🐒  
→ https://monkeyisland.fandom.com/wiki/Insult_Sword_Fighting  
→ https://strategywiki.org/wiki/The_Secret_of_Monkey_Island/Sword-Fighting_Insults

GPT-Neo  
→ https://huggingface.co/blog/few-shot-learning-gpt-neo-and-inference-api

OpenAI GPT-3 Playground  
→ https://beta.openai.com/playground/p/oahgFuR1ABeP2h8zO32caUNf

Effectively using GPT-J and GPT-Neo, the GPT-3 open-source alternatives, with few-shot learning  
→ https://nlpcloud.io/effectively-using-gpt-j-gpt-neo-gpt-3-alternatives-few-shot-learning.html

Thanks for a lot of the insults gameplay coming from Orson Scott Card and his children for coming up with the originial insults! (https://youtu.be/xgqEneDNQto?t=3469)

<p align="center">
  <img src="https://github.com/lukexyz/insultswordfight/blob/master/media/transformer.png?raw=true" width=80%> 
</p>

[/u/crumpuppet](https://www.reddit.com/r/MonkeyIsland/comments/if1wcs/i_made_a_monkey_island_sword_fighting_insult)

## Setup develoment environment with `nbdev`

- Ubuntu / WSL

```
conda create -n swordfight python=3.9 jupyter twine
conda activate swordfight
pip install nbdev
git clone https://github.com/lukexyz/insultswordfight.git
pip install -r requirements.txt
```

- Install githooks from project folder

```
nbdev_install_git_hooks
```

### Nbdev commands

#### 1. 🏗️ **Build lib** from notebooks

> `nbdev_build_lib`

#### 2. 📝 **Build docs** from notebooks

> `nbdev_build_docs`

> Image generated by [/u/crumpuppet](https://www.reddit.com/r/MonkeyIsland/comments/if1wcs/i_made_a_monkey_island_sword_fighting_insult).
