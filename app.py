from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        print(customer,comments)
        return render_template('success.html')
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run()