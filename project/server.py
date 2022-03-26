from flask import Flask, request
from pyhtml import html # TODO add imports

app = Flask(__name__)
app.config['SECRET_KEY'] = '08ccc5b937fa253dfb0462d9289aa05d7ae5d3ada0ce1876f5743b1f3b88bd3e'

@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == 'POST':
        # TODO you received form data, handle it
        # (usually produce HTML)
        pass
    else:
        # TODO you didn't receive form data
        # (usually produce HTML)
        pass
        
    response = html(
        # TODO put your pyhtml code here
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)