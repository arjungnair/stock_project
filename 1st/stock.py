import os
import urllib.request, json
import pandas as pd
import datetime as dt
import time
api_key = '1Z88CFAX1HRVPOFH'
# Computer Security 
i=["CYBR","FTNT","PANW","ZIXI","CHKP","RDWR","PFPT","QLYS","VRNS","FEYE"]
#IT Services
j=["SCWX","FICO","FSCT","EPAM","NOW","CDW","CSGP","WIX","INFY","INOV","UIS","MAMS","DAVA","LXFT","PSDO","STCN","SAIC","NTNX","CDK","MHH","BZUN","ASGN","DOX","PRSP","DXC","GIT","CLPS","DTSS","ABIL","ANY"]
#COMPUTERS - Peripheral Equpt
k=["MRCY","SSYS","INVE","LOGI","EFII","LPL","VJET","IMMR","TACT","VUZI"]
#Lasers - Systems and Components
l=["CYBE","MVIS","LITE","IPGP","CUTR"]
#COMMUNICATION NETWORK SOFTWWARE
m=["ATEN","RBBN","DZSI","AVYA","EVOL"]
#Internet Commerce
n=["W","CVNA","TZOO","MELI","IAC","TRIP","AMZN","EXPE","CTRP","BABA","TVPT","EBAY","PDD","CARS","JD","STMP","PETS"]
#Food Items Wholesale
o=["PFGC","NGVC","VSI","SFM","FARM","SPTN"]
#Mobile and TV Production
p=["WWE","FOX","FOXA","IMAX","EROS","MSGN","LGF-A"]
#Wholesale Computers and Peripheral Equipment
q=["TECO","PLUS","SCSC","PSDO","SNX"]
#Gaming
r=["ZNGA","DDE","ERI","CNTY","AGS","UWN","MCRI","CHDN","MLCO","RRR","BYD","LVS","PENN","MGM","WBAI","WYNN","CZR","FLL","TSG","IGT","GDEN","NYNY"]
b=[i,j,k,l,m,n,o,p,q,r]
for a in b
    for ticker in a:
        url_string = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=%s&interval=5min&outputsize=full&apikey=%s"%(ticker,api_key)
        #file_to_save = '%s.csv'%ticker
        #if not os.path.exists(file_to_save):
        with urllib.request.urlopen(url_string) as url:
            data = json.loads(url.read().decode())
            data = data['Time Series (5min)']
            df = pd.DataFrame(columns=['Date','Low','High','Close','Open'])
            for k,v in data.items():
                date = dt.datetime.strptime(k, '%Y-%m-%d %H:%M:%S')
                data_row = [date.date(),float(v['3. low']),float(v['2. high']),float(v['4. close']),float(v['1. open'])]
                df.loc[-1,:] = data_row
                df.index = df.index + 1
        time.sleep(7)
        print (df)
        #print('Data saved to : %s'%file_to_save)        
        #df.to_csv(file_to_save)
    #else:
        #print('File already exists. Loading data from CSV')
        #df = pd.read_csv(file_to_save)
