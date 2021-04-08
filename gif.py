from flask import Flask, render_template, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import urllib
import json

class gifinput(FlaskForm):
	phrase = StringField('Input', validators=[DataRequired()])
	submit = SubmitField('To Giphy')


app = Flask(__name__)
app.config['SECRET_KEY'] = '1h4h5h29b2b5bsjq838'

url = "http://api.giphy.com/v1/gifs/search?"


@app.route('/')
@app.route('/input', methods=['GET', 'POST'])
def input():
	form = gifinput()
	return render_template('input.html', title='input', form=form)


@app.route('/output', methods=['GET', 'POST'])
def output():

	if request.method == 'POST':
		elements = [x for x in request.form['text'].split()]
	
	return render_template('output.html', title='gifs')



