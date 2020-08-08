from flask import Flask, render_template, request

app_guvi = Flask(__name__)


@app_guvi.route('/')
def index_guvi():
	return render_template('C:\Users\yuva0\Desktop\arunGUVI\Flask\flask_template\templates\marks.html')


if __name__ == "__main__":
	app_guvi.run()
