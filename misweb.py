from flask import Flask, render_template,request

from datetime import datetime



app = Flask(__name__)

@app.route("/")

def index():
	homepage = "<h1>吳致葦Python網頁</h1>"

	homepage += "<a href=/mis>MIS</a><br>"

	homepage += "<a href=/today>顯示日期時間</a><br>"

	homepage += "<a href=/welcome?nick=吳致葦>傳送使用者暱稱</a><br>"

	homepage += "<a href=/about>吳致葦簡介網頁</a><br>"

	return homepage

@app.route("/mis")

def course():

	return "<h1>資訊管理導論</h1>"

@app.route("/today")

def today():

	now = datetime.now()

	return render_template("today.html", datetime = str(now))

@app.route("/welcome", methods=["GET", "POST"])

def welcome():

	user = request.values.get("nick")

	return render_template("welcome.html", name=user)

@app.route("/about")

def aboutme():
	return render_template("aboutme.html")
	
if __name__ == "__main__":

	app.run()