from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def tablero():
    return render_template('index.html',num1=8,num2=8)

@app.route('/<int:x>/<int:y>')
def chess_num(x,y):
    return render_template('index.html',num1=x,num2=y)
'''
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def chess_colors(x,y,color1,color2):
    return render_template('index.html',num1=x,num2=y,color1=color1,color2=color2)
'''
if __name__ == "__main__": 
    app.run(debug=True)