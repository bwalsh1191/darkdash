from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

API_KEY = '4HNDQOUQ2A1G90RW'


@app.route('/')
def hello_world():

    symbol='aapl'
    days, avg_price = make_df(symbol)
    
    return render_template('index.html', days=days, symbol=symbol, avg_price=avg_price)
'''
def get_data():
    years = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
    values = [86,114,106,106,107,111,133,221,783,2478]
    return(years, values)
'''

def make_df(symbol): 
    #use this one for testing
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + symbol + '&outputsize=full&datatype=csv&apikey=' + API_KEY
    df = pd.read_csv(url, index_col="timestamp", parse_dates = True, na_values = ' ')
    df['close'] = df['adjusted_close']
    df.index.names = ['date']

    #mod df starts here
    df['date'] = df.index
    df['day'] = df['date'].dt.day_name()
    df['month'] = df['date'].dt.month_name()
    df['year'] = df['date'].dt.year
    close_price = list(reversed(df['close'].tolist()))
    #close_price = list(reversed(close_price))
    #days= list(reversed(df['date'].tolist()))
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
    avg_price = df['close'].groupby(df['day']).mean().reindex(days).tolist()

    #return(close_price, week_df)
    return(days, avg_price)


#THIS HAST TO BE THE END OF THE FILE
if __name__ == '__main__':
    app.run(debug = True)
