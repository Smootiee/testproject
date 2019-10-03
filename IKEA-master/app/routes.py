from flask import render_template
from app import app

# Routes go here!

# Decoration to specify what function to run for what route on the website
@app.route('/')
def login():
    return render_template('loginPage.html')

@app.route('/landing')
def land():
    return render_template('landingPage.html')

@app.route('/create')
def create():
    return render_template('createPage.html')

# Overview page should be routed from landing page...