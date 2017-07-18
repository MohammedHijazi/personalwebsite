from flask import Flask,render_template
import random
app = Flask(__name__)








@app.route("/")
def home_page():
	nam=["mohammed", "Bakiza" , "odai" , "khaled"]
	return render_template("index.html",name=random.choice(nam))


@app.route("/about")
def about_me():
	return render_template("aboutme.html")



if __name__ == "__main__":
	app.run(port=5052)

