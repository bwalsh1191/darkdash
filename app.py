from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_name():
   user="Google"
   return render_template('hello.html', chart_name = user)

if __name__ == '__main__':
   app.run(debug = True)