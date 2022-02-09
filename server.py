from flask import Flask
import random

app = Flask(__name__)
x = random.randint(0, 9)


@app.route('/')
def hi():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media3.giphy.com/media/fAo1Tv1OGE6AQZ2s0T/200w.webp?cid=ecf05e471x9xp0vl8qd5mhmtgbscblrsiq0oji8oqrgnm4gl&rid=200w.webp&ct=g' width='400px'>"


@app.route('/<int:guess>')
def response(guess):
    if guess > x:
        return '<h1 style="color: red">Too high, Try again!</h1>' \
               '<img src="https://media0.giphy.com/media/l2YWy9pD8sZEUMF0s/200w.webp?cid=ecf05e47r9r6ekf35dnj850nh9zv8wpp8s5ycke7v1j1e27m&rid=200w.webp&ct=g" width="400px">'
    elif guess < x:
        return '<h1 style="color: red">Too low, Try again!</h1>' \
               '<img src="https://media4.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/200w.webp?cid=ecf05e4784yr3r9jjmrjs7gs5nj8twq112ilr2va3oe73y2t&rid=200w.webp&ct=g" width="400px">'
    else:
        return '<h1 style="color: green">Yesss you got it!!!</h1>' \
               '<img src="https://media4.giphy.com/media/UVqjTRkl3dkfHuJ3FY/200w.webp?cid=ecf05e472st5bqi36o2x0469fqnikhpe71ofndd3tbrhv9x9&rid=200w.webp&ct=g" width="400px">'


if __name__ == "__main__":
    app.run(debug=True)