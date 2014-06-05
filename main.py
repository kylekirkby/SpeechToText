import requests, json

import subprocess

wav_file = "test.wav"

def get_access_token_json():

	p = subprocess.Popen(['curl', 'https://api.att.com/oauth/token',
				'--header','Content-Type: application/x-www-form-urlencoded',
				'--header','Accept: application/json',
				'--data',
	'client_id=9bncobuoqblxoanqmm44vdxtjs4d8rs5&client_secret=g9tqrffri9ljen8ujzwijqxiw1gyzund&scope=SPEECH&grant_type=client_credentials',
				'--request','POST'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()

	return out


def speech_to_text(token, wav_file_path):


	p = subprocess.Popen(['curl', 'https://api.att.com/speech/v3/speechToText',
				'--header','Authorization: Bearer '+ token + '',
				'--header','Accept: application/json',
				'--header','Content-Type: audio/x-wav',
				'--data-binary', '@' + wav_file_path,
				'--request','POST'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()

	return out


def get_token():

   	res = get_access_token_json()

	dictionary = json.loads(res)

	token = dictionary.get('access_token')

	return token

def get_text(output):

	text = json.loads(output)
	
	print text

if __name__ == "__main__":

	token = get_token()

	out = speech_to_text(token, wav_file)

	get_text(out.decode('utf-8'))
