#!/usr/bin/env python
# coding: utf-8

import os
from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer
import gradio as grad, random, re

model_path = "model/"
model_chk = os.path.exists('model/pytorch_model.bin')
csv_chk = os.path.exists('flagged/log.csv')

if model_chk is False:
    dir_chk = os.path.exists('model/')
    if dir_chk is False:
        os.makedirs('model')
    
    repo = "Gustavosta/MagicPrompt-Stable-Diffusion"
    tokenizer_dl = GPT2Tokenizer.from_pretrained(repo)
    model_dl = GPT2LMHeadModel.from_pretrained(repo)
    tokenizer_dl.save_pretrained(model_path)
    model_dl.save_pretrained(model_path)
    print('model cloned from Hugging Face')

tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path, pad_token_id=tokenizer.eos_token_id)
pipe = pipeline('text-generation', model=model, tokenizer=tokenizer, max_new_tokens=100)

title = "Stable Diffusion Prompt Generator"
article = 'This is a demo of the model series: "MagicPrompt", in this case, aimed at: "Stable Diffusion". To use it, simply submit your initial prompt on the left. To learn more about the model, [click here](https://huggingface.co/Gustavosta/MagicPrompt-Stable-Diffusion).<br>'

grad.Interface.from_pipeline(pipe,
                             title=title,
                             article=article,
                             allow_flagging='manual', flagging_dir='.').launch(server_name="0.0.0.0",server_port=8088, show_api=False, debug=True, favicon_path="favicon.png")

# # 
