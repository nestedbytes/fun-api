from flask import Flask, jsonify, render_template
import random
import pyjokes
app = Flask(__name__)

@app.route("/")
def home():


    return render_template('index.html')




@app.route('/joke')
def joke():
    


    joke = pyjokes.get_joke(language="en")
    return(joke)



    



if __name__ == "__main__":
    app.run(debug=False)
   
    
