from turtle import clear, title
from flask import Flask, render_template, url_for
from Gateway import  get_next_package_number, get_package,get_current_package_number,get_graph
from GP import run

app = Flask(__name__)

app.config['SECRET_KEY'] = '78d21395b973931b08fb5c69b84e0dec'





@app.route("/home")
def home():
    current_package_number = get_current_package_number()
    return render_template("Home.html",posts= current_package_number)

@app.route("/about")
def about():
   return get_package()


@app.route("/next")
def about1():
  current_package_number = get_next_package_number()
  return render_template("Home.html",posts= current_package_number)


@app.route("/send")
def send():  
    global package
    package = get_package()
    print(package)
    current_package_number = get_current_package_number()
    value = [current_package_number,run()]
    return  render_template("next.html",posts= value)

@app.route("/construct")
def construct():
    
    return get_graph()



if __name__ == '__main__':
    app.run(debug=True,port=8000)