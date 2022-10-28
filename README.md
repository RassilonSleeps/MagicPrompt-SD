### Credit to [Gustavosta](https://huggingface.co/Gustavosta) on Hugging Face for model

Based on Gustavosta's app.py script used for his [Hugging Face Spaces](https://huggingface.co/spaces/Gustavosta/MagicPrompt-Stable-Diffusion)
This is a trimmed and simplified implementation intended for running locally directly with python or via notebook

### Requirements:
	- Python 3.4 or higher
	- Git-LFS 
### Recommended:
	Use of virtual environments via venv or conda
	- Included Windows batch files implement venv during install

# How to use:

### (Windows): Batch files included for all of the following methods
### (Unix): Shell scripts are planned, but not implemented

###		Python
	- From terminal use " pip install -r requirements.txt " to grab dependencies
	- Run python MagicPrompt.py
	- Visit localhost:8088 in browser (substitute 'localhost' with devices ip address if run remotely)
###		Jupyter Notebook
	- From terminal use " pip install -r notebook-requirements.txt " to grab dependencies
	- Run " jupyter notebook MagicPrompt.ipynb "
###		Google Colab
	- Visit https://colab.research.google.com
	- Choose Upload tab
	- Browse to file " MagicPrompt.ipynb "
	
	- ***  Using Google's free servers: ***
	- Just click connect in top right
	- Use Runtime menu to run all
	
	- ***  For local:  ***
	- From terminal use " pip install -r notebook-requirements.txt " to grab dependencies
	- Run " jupyter notebook --no-browser --NotebookApp.allow_origin="https://colab.research.google.com" --port=8888 --NotebookApp.port_retries=0 "
	- Copy URL containing token (e.g. http://localhost:8888/?token=5bbec....)
	- In Colab, use dropdown next to connect and select 'Connect to a local runtime'
	- Paste URL into the 'Backend URL' box and click connect
	- Use Runtime menu to run all
	

### **From original README.md**
> This is a model from the MagicPrompt series of models, which are [GPT-2](https://huggingface.co/gpt2) models intended to generate prompt texts for imaging AIs, in this case: [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion).
> This model was trained with 150,000 steps and a set of about 80,000 data filtered and extracted from the image finder for Stable Diffusion: "[Lexica.art](https://lexica.art/)". It was a little difficult to extract the data, since the search engine still doesn't have a public API without being protected by cloudflare, but if you want to take a look at the original dataset, you can have a look here: [datasets/Gustavosta/Stable-Diffusion-Prompts](https://huggingface.co/datasets/Gustavosta/Stable-Diffusion-Prompts).
> If you want to test the model with a demo, you can go to: "[spaces/Gustavosta/MagicPrompt-Stable-Diffusion](https://huggingface.co/spaces/Gustavosta/MagicPrompt-Stable-Diffusion)".

# Changes from 'Spaces' app.py
* Model is saved to local folder allowing for offline use
* Colab-style notebook file for easy editing and use of gradio's in line interface
* Enabled gradio flagging feature, allows saving of prompt to log.csv
* Trimmed code by switching gradio's '.interface()' to '.interface.from_pipeline'
	- This was done to simplify code and prevent log.csv from filling with unwanted prompts
	- Likely going to change once I better learn python and the options of the transformers library
* Added requirements.txt for quick terminal deployment via 'pip install -r requirements.txt'
* Also added a seperate notebook-requirements.txt for use with jupyter notebook
* Changed port from gradio's standard to allow running at the same time as another gradio interface (e.g. Automatic1111's WebUI using default ports)
* Changed listening address from '127.0.0.1' (local host only) to '0.0.0.0' (network wide)
	- allows for access from other devices, useful for deployment on headless server
* Removed use of ideas.txt for examples
	- While some would consider it a nice addition, I find no value for my use case
* Added a favicon :hugs:

###Pull requests welcome, I have no former python experience

## 💻 You can see other MagicPrompt models:

- For Dall-E 2: [Gustavosta/MagicPrompt-Dalle](https://huggingface.co/Gustavosta/MagicPrompt-Dalle)
- For Midjourney: [Gustavosta/MagicPrompt-Midourney](https://huggingface.co/Gustavosta/MagicPrompt-Midjourney) **[⚠️ In progress]**
- MagicPrompt full: [Gustavosta/MagicPrompt](https://huggingface.co/Gustavosta/MagicPrompt) **[⚠️ In progress]**

## ⚖️ Licence:

[MIT](https://huggingface.co/models?license=license:mit)

When using this model, please credit: [Gustavosta](https://huggingface.co/Gustavosta)

**Thanks for reading this far! :)**
