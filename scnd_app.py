import logging

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session, context
import json
import os
app = Flask(__name__)

ask = Ask(app, "/")
app.config['ASK_VERIFY_REQUESTS'] = True
#logging.getLogger("flask_ask").setLevel(logging.DEBUG)

bio = ['food scraps','coffee grounds', 'paper towels', 'toilet paper', 'newspapers', 'junk mail', 'paper plates', 'paper cups', 'clothing','towels','printer paper', 'paper towels', 'toilet paper', 'paper plates', 'bowls','cups', 'textbooks', 'notebooks', 'paper folders','cardboard boxes','weeds', 'grass', 'plant clipping', 'leaves', 'peat pots', 'plant stakes' ,'plant-based pesticides','paper','books','wood', ]



n_bio = ['plastic','almunium','grocery bags', 'plastic bags', 'water bottles','metals', 'metal cans', 'tins', 'metal scraps','construction waste', 'rubber tires', 'nylon' ,'glass', 'cds', 'dvd', 'cellophane', 'processed woods', 'cable wires', 'Styrofoam',] 



@ask.launch
def new_game():
	welcome_msg = render_template('welcome')

	reprompt = render_template('reprompt')
	return question(welcome_msg).reprompt(reprompt)

@ask.intent("AMAZON.HelpIntent")

def help():
	msg = render_template('help')
	cross = render_template('cross')
	return question(msg).reprompt(cross)
	
@ask.intent("AskIntent")
def code(object):

	if object in bio:
		msg = render_template('Yess',object = object)
		
	elif object in n_bio:
		msg = render_template('Noo', object = object)
	else:
		msg = render_template('reprompt_m')
	return question(msg)

@ask.intent('AMAZON.StopIntent')
def stop():
	bye_text = render_template('bye')
	return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel():
	bye_text = render_template('bye')
	return statement(bye_text)


@ask.session_ended
def session_ended():
	return "{}", 200
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)