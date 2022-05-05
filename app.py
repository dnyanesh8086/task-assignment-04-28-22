from flask import Flask


app=Flask(__name__)

@app.route("/")
def hello():
    return"Hello World"


@app.route("/number")
def randomnum():
    import random
    from random import randint

    a=random.randint(100,200)
    return str(a)






    










if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")