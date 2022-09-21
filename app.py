from flask import Flask, request, render_template, redirect, flash, session
from surveys import satisfaction_survey as s_survey
from surveys import personality_quiz as p_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "a secret!"

responses = []

@app.route("/")
def pick_survey():
    return render_template("welcome.html")

@app.route("/personality-quiz")
def personality_quiz():
    title = s_survey.title
    instructions = s_survey.instructions
    return render_template("personality.html", title=title, instructions=instructions)

@app.route("/satisfaction-survey")
def satisfaction_survey():
    title = p_survey.title
    instructions = p_survey.instructions
    return render_template("satisfaction.html", title=title, instructions=instructions)

@app.route("/thank-you")
def thank_you():
    return render_template("thanks.html")