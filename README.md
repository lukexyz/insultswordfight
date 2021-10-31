
<p align="center">
  <img src="https://github.com/lukexyz/insultswordfight/blob/master/media/transformer.png?raw=true" width=100%> 
</p>

## Setup environment with `nbdev`

* Ubuntu / WSL
```
conda create -n swordfight python=3.9 jupyter pip nbdev twine
conda activate swordfight  
git clone https://github.com/lukexyz/insultswordfight.git  
pip install -r requirements.txt  
```
  
  
* Install githooks from project folder  
```
nbdev_install_git_hooks
```

## during develoment:  
### 1. 🏗️ **Build lib** from notebooks  
> `nbdev_build_lib` 


### 2. 📝 **Build docs** from notebooks  
> `nbdev_build_docs` 

## References
ISF at Monkey Island Fandom 🐒
https://monkeyisland.fandom.com/wiki/Insult_Sword_Fighting
https://strategywiki.org/wiki/The_Secret_of_Monkey_Island/Sword-Fighting_Insults
GPT-Neo  
https://huggingface.co/blog/few-shot-learning-gpt-neo-and-inference-api
OpenAI GPT-3 Playground  
https://beta.openai.com/playground/p/oahgFuR1ABeP2h8zO32caUNf


