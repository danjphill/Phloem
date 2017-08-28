from flask import Flask, request, render_template
import os
import socket


app = Flask(__name__)


@app.route('/')
def index():
    return "Server"


@app.route('/vidlist')
def vidlist():
	file_names = []
	file_paths = []
	for file in os.listdir(os.getcwd()+"/static/video"):
 		if file.endswith(".mp4") or file.endswith(".mkv"): 
 			file_names.append(file)

	return render_template('vidlist.html',file_names=file_names, file_paths=file_paths)

@app.route('/vidplayer/<path>')
def vidplayer(path):
	path = path.replace("%%","/")
	title = path[path.rfind("/")+1:path.rfind(".")]
	print path
	return render_template('videoplayer.html',path=path,title=title)

@app.route('/filepath/<path>')
def filepath(path):	
	
	path = path.replace("%%","/")
	path_crumbs = path.split("/")
	print path
	files=[]
	folders=[]

	for file in os.listdir(os.getcwd()+"/static/"+path):
		try:
	 		for innerfile in os.listdir(os.getcwd()+"/static/"+path+"/"+file):
	 			break
	 		folders.append(file)
	 	except:
	 		files.append(file)
	
	return render_template('filelist.html',path=path, files=files, folders=folders, path_crumbs=path_crumbs)


if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.106')
	