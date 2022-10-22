#!/usr/bin/env python
# coding: utf-8

from transformers import pipeline, GPT2LMHeadModel, GPT2Tokenizer
import gradio as grad, random, re

model_path = "model/"
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path, pad_token_id=tokenizer.eos_token_id)
pipe = pipeline('text-generation', model=model, tokenizer=tokenizer)

title = "Stable Diffusion Prompt Generator"
article = 'This is a demo of the model series: "MagicPrompt", in this case, aimed at: "Stable Diffusion". To use it, simply submit your initial prompt on the left. To learn more about the model, [click here](https://huggingface.co/Gustavosta/MagicPrompt-Stable-Diffusion).<br>'

grad.Interface.from_pipeline(pipe,
                             title=title,
                             article=article,
                             allow_flagging='manual').launch(server_name="0.0.0.0",server_port=8088, show_api=False, debug=True, favicon_path="favicon.png")

# # 
