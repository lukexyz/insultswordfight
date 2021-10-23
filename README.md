
## Setup environment and `nbdev`

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