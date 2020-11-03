from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


app.route("/<qu>")
def get_data(qu):
    message = []

    url = f"https://newsapi.org/v2/everything?q={qu}&apiKey=ee58adf745244c7e8c30e9c0ac322a3e"
    response = requests.get(url)
    response = response.json()
    r = ""
    for item in response['articles']:
        headlines = (item['title'])
        author = ((item['source'])["name"])
        image = item["urlToImage"]
        message.append([headlines, author, image])
    for items in message:
        if (items[0] != None and items[1] != None and items[2] != None):
            r += ('<tr><td><h3>' + items[0] + '<br><small><h2>-' + items[
            1] + '</h2></small></h3></td><td><img src="' +
            items[2] + '" class="img-fluid" style=" max-height: 200px;" alt="Cinque Terre"></td></tr>')
    print(message)
    return message


@app.route("/", methods=["POST", "GET"])
def helloworld():
    if request.method == "POST":
        query = request.form["topic"]
        return render_template("news.html", result = get_data(query))
    else:
        return render_template("news.html")

if __name__ == '__main__':
    app.run(debug=True)
