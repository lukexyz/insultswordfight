
<p align="center">
  <img src="https://github.com/lukexyz/insultswordfight/blob/master/media/transformer.png?raw=true" width=80%> 
</p>  

Image generated by [/u/crumpuppet](https://www.reddit.com/r/MonkeyIsland/comments/if1wcs/i_made_a_monkey_island_sword_fighting_insult).  

## Generated zingers 🍒
☠️ Insult: Heaven preserve me! You look like something that's died! ☠️  
`Comeback: (0)  If you ever need an autopsy, I'd be glad to do it.`  🔥🔥🔥   

☠️ Insult: Killing you would be justifiable homicide! ☠️  
`Comeback: (0)  Unless it was murder, then you'd be guilty of suicide.` 🔥🔥🔥   

☠️ Insult: I once owned a dog that was smarter than you. ☠️  
`Comeback: (0) I hope you lost him.` 🔥🔥🔥   

___

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


___


## Setup develoment environment with `nbdev`

* Ubuntu / WSL
```
conda create -n swordfight python=3.9 jupyter twine
conda activate swordfight  
pip install nbdev
git clone https://github.com/lukexyz/insultswordfight.git  
pip install -r requirements.txt  
```
  
  
* Install githooks from project folder  
```
nbdev_install_git_hooks
```

### Nbdev commands  

#### 1. 🏗️ **Build lib** from notebooks  
> `nbdev_build_lib` 


#### 2. 📝 **Build docs** from notebooks  
> `nbdev_build_docs` 
