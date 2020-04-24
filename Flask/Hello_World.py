from flask import Flask, render_template, url_for, json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

df = pd.read_json("../data/books.json")

@app.route('/')
def index():
    return "Hello world!"

@app.route('/books')
def books():
    return df.to_json(orient='records', lines=True)

@app.route('/book', defaults={'isbn': None})
@app.route('/book/<isbn>')
def select_one(isbn):
    if isbn is None:
        abort(404)
    else:
        return df[df['isbn'] == isbn].to_json(orient='records', lines=True)

if __name__ == "__main__":
    app.run()