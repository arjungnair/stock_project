import os
import urllib.request, json
import pandas as pd
import datetime as dt
api_key = '1Z88CFAX1HRVPOFH'
# Computer Security 
i=["CYBR","FTNT","PANW","ZIXI","CHKP","RDWR","PFPT","QLYS","VRNS","FEYE"]
for ticker in i:
    url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=5min&outputsize=full&apikey=%s"%(ticker,api_key)
    file_to_save = '%s.json'%ticker
    if not os.path.exists(file_to_save):
        with urllib.request.urlopen(url_string) as url:
            data = json.loads(url.read().decode())
            data = data['Time Series (5min)']
            df = pd.DataFrame(columns=['Date','Low','High','Close','Open'])
            for k,v in data.items():
                date = dt.datetime.strptime(k, '%Y-%m-%d %H:%M:%S')
                data_row = [date.date(),float(v['3. low']),float(v['2. high']),
                            float(v['4. close']),float(v['1. open'])]
                df.loc[-1,:] = data_row
                df.index = df.index + 1
        print('Data saved to : %s'%file_to_save)        
        df.to_json(file_to_save)
    else:
        print('File already exists. Loading data from CSV')
        df = pd.read_json(file_to_save)