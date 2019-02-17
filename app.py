from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    years = [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050]
    values = [86,114,106,106,107,111,133,221,783,2478]
    values2 = [2478,783,123,445,320,111,133,221,783,86]
    
    return render_template('index.html', values=values, years=years, values2 = values2)

if __name__ == '__main__':
    app.run(debug = True)