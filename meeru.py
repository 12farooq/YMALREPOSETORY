from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def home ():
    return render_template('xyz.html')
@app.route('/abc')
def next():
    return "meeran"
if __name__=="__main__":
    app.run(debug=True)
