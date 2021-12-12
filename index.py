from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/home/<item>")
def item(item):
    return render_template('item.html', product=item)

if __name__ == '__main__':
    app.run(debug= True)

