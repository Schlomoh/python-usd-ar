import os

from flask import Flask, request
import tempfile

app = Flask(__name__)

MAX_FILESIZE = 52428800 # 50MB


def convert(data):
	"""Calls the usdzconvert python script"""

	# use temp directory
	with tempfile.TemporaryDirectory() as tmpdirname:
		# save data to temp directory as temp file
		with open(tmpdirname + 'temp.glb', 'wb') as f:
			f.write(data)

		# call usdzconvert
		os.system('python3 usdzconvert/usdzconvert.py ' + tmpdirname + 'temp.glb')

@app.route('/', methods=['POST'])
def handle_convert():
	"""Calls the usdzconvert python script"""

	error = None

	try:
		# get requests query param (filesize) and check if it's bigger than 50MB
		file_size = request.args.get('filesize')
		if file_size > MAX_FILESIZE:
			raise Exception('Filesize too big')

		file_data = request.get_json()['data']
		convert(file_data)
	except Exception as e:
		error = e
		print(error)
  
	# get glb binary data from request
	return 'test'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
