from flask import Flask, render_template, request
import google.generativeai as palm

palm.configure(api_key="AIzaSyB-Fj1hTUvBxzqftvz9W3J7jJtvtj6l1bM")
model = {'model': "models/chat-bison-001"}

import replicate
import os

os.environ["REPLICATE_API_TOKEN"]="r8_JsQ9AuMJGNGlelYjaYLCDUhqIEG6XZC1yaN6o"

import requests
from PIL import Image


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
   return(render_template("main.html"))

@app.route("/palm", methods=["GET", "POST"])
def palm_ff():
   q = request.form.get("qns")
   r = palm.chat(**model, messages=q)
   print(r.last)
   return(render_template("reply.html", r = r.last))

@app.route("/stable", methods=["GET", "POST"])
def stable_f():
   q = request.form.get("img_prompt")
   r = replicate.run(
       "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4",
       input={"prompt": q}
   )
   print (r[0])
   return(render_template("reply.html", r = r[0]))

if __name__ == "__main__":
    app.run()
