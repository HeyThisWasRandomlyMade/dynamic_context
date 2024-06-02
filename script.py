import os
import gradio as gr
from datetime import datetime

def	custom_generate_chat_prompt(user_input, state, **kwargs):
	'''
	This extension will replace all instances of
	{{time}} and {{date}} with the current
	time and date, respectively
	Additionally replaces {{weekday}} with the day of the week.
	'''
	now = datetime.now()
	state['context'] = state['context'].replace('{{time}}', now.strftime("%I:%M %p"))
    	state['context'] = state['context'].replace('{{date}}', now.strftime("%Y %B, %d"))
    	state['context'] = state['context'].replace('{{weekday}}', now.strftime("%A"))
	state['context'] = state['context'].replace('{{timezone}}', now.strftime("%Z"))
	# print(f'<<context, changed>>')
	# print(f'{state["context"]}')
	return 
