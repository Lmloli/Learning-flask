#from distutils.log import debug
#from re import T
from flask  import Flask, render_template
skills_app = Flask(__name__)

@skills_app.route("/")
def index():
    return render_template('index.html')



if __name__ == "__main__":
    skills_app.run(debug=True)