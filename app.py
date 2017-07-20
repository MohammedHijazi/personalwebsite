from flask import Flask,render_template, request
import random
app = Flask(__name__)



@app.route("/")
def home_page():
	nam=["mohammed", "Bakiza" , "odai" , "khaled"]
	return render_template("index.html",name=random.choice(nam))


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
	return render_template ("formdata.html",userfirstname=user_firstname,userlastname=user_lastname,
	usermessage=user_message,usergender=user_gender)




if __name__ == "__main__":
	app.run(port=5052)