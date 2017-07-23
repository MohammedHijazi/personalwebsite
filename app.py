from flask import Flask,render_template, request
import dataset
import random
app = Flask(__name__)


# db=dataset.connect("postgres://yowahpfaxtsjoc:89e78de430594fa7bffec234ce5bc8ac9193cef0a864378fd900ddd573d65651@ec2-23-23-244-83.compute-1.amazonaws.com:5432/dbn2rcviq5s3i4")
# table=db["hijazi_user"]



@app.route("/")
def home_page():
	return render_template("index.html") 


@app.route("/about")
def about_me():
	return render_template("aboutme.html")


@app.route("/contact")
def contact_us():
	return render_template("contactus.html")




@app.route("/form_response",methods=["POST"])
def form_res():
	user_firstname = request.form["firstname"]
	user_lastname = request.form["lastname"]
	user_message = request.form["message"]
	user_gender = request.form["gender"]

	# hijazi_user.insert(dict(name=user_firstname
							# ,userlastname=user_lastname
							# ,usermassege=user_message
							# ,usergender=user_gender))
	# print hijazi_user

# @app.route("/displayinfo")
# def display():
# 	dis=hijazi_user.findone(name="user_firstname")
# 	return render_template("dis.html")






if __name__ == "__main__":
	app.run(port=5052)