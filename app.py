# 2.0.0
from flask import Flask, jsonify, render_template

import pyjokes
app = Flask(__name__)

def get_meme():

    url = "<https://meme-api.herokuapp.com/gimme>"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit
@app.route("/")
def home():


    return render_template('index.html')




@app.route('/joke')
def joke():
    


    joke = pyjokes.get_joke(language="en")
    return(joke)
@app.route('/meme')
def meme():
    meme_pic,subreddit = get_meme()
    return render_template("meme.html",
    meme_pic=meme_pic)
    
    
    




if __name__ == "__main__":
    app.run(debug=False)
   
    
