import gspread
from flask import Flask, render_template, request
app = Flask(__name__)

gc = gspread.service_account(filename="flask-profile.json")
sh = gc.open('flask-app')

shProfile = sh.get_worksheet(0)

@app.route('/')
def home():
    profile = {
        'about':shProfile.acell('B1').value,
        'intrests':shProfile.acell('B2').value,
        'experience':shProfile.acell('B3').value,
        'education':shProfile.acell('B4').value,
    }
    return render_template('index.html', profile=profile)

