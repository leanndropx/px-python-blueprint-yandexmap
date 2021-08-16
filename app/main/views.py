from . import main
from flask import render_template
from app import functions

@main.route ("/")
def home():
    return render_template("index.html")

