
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import cross_validate
from sklearn import model_selection
from matplotlib.pyplot import figure

def prepare(csv):
    df = pd.read_csv(csv)
    df['Date'] = pd.to_datetime(df['Date'])
    df['year'], df['month'],df['day'] = df['Date'].apply(lambda x: x.year), df['Date'].apply(lambda x: x.month),df['Date'].apply(lambda x: x.day)
    return df

def linear(x_train, y_train):
    from sklearn import linear_model
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    return regr

def svm(x_train, y_train):
    from sklearn.svm import SVR
    clf = SVR(gamma='scale', C=1.0, epsilon=0.2)
    clf.fit(x_train, y_train) 
    return clf

def plot(df):
    plt.plot(df["Date"], df["Close Price"],  color='green')
    plt.xlabel("date")
    plt.ylabel("closed price")
    plt.show()
    fig=plt.gcf()
    fig.set_size_inches(8,4, forward=True)
    fig.savefig("C:\\Users\\anton\\Desktop\\ML\\",c,".png", dpi=100)

def prediction(model,x_test, y_test):
    cross_validate(model, x_test, y_test, cv=3,return_train_score=True)
    results = model_selection.cross_val_score(model,x_test, y_test, cv=3)
    #print(results.mean())
    import datetime
    day=int(datetime.datetime.now().strftime ("%d"))
    m=int(datetime.datetime.now().strftime ("%m"))
    array=[]
    dt = datetime.datetime(2019, 3, 17)
    end = datetime.datetime(2019, 4, 16)
    step = datetime.timedelta(days=1)
    
    result = []

    for i in range(0,30):
        result=[dt.strftime('%Y-%m-%d'),]
        array.append(result,)
        dt += step
    X=np.array(array)
    p=pd.DataFrame(X)
    #print(p)
    p[0] = pd.to_datetime(p[0])
    p['year'], p['month'],p['day'] = p[0].apply(lambda x: x.year),p[0].apply(lambda x: x.month),p[0].apply(lambda x: x.day)
    #print(p)
    Y = model.predict(p[['day','month','year']])
    #print(Y)
    q=pd.DataFrame(Y)
    plt.plot(p[0],q[0], color="blue")
    plt.show()
    fig=plt.gcf()
    fig.set_size_inches(8,4, forward=True)
    fig.savefig('C:\\Users\\anton\\Desktop\\ML\\3.png', dpi=100)
    return Y
    
def main():
    cdf=prepare("C:\\Users\\anton\\Downloads\\1.csv")
    msk = np.random.rand(len(cdf)) < 0.5
    train = cdf[msk]
    test = cdf[~msk]
    plot(cdf[msk])
    plot(cdf[~msk])
    x_train = np.asanyarray(train[['day','month','year']])
    y_train = np.asanyarray(train[['Close Price']])
    x_test = np.asanyarray(test[['day','month','year']])
    y_test = np.asanyarray(test[['Close Price']])
    model1=linear(x_train, y_train)
    model2=svm(x_train, y_train)
    prediction(model1,x_test, y_test)
    prediction(model2,x_test, y_test)
    y_pre1=model1.predict(x_train)
    y_pre2=model2.predict(x_train)
    m1=pd.DataFrame(y_pre1)
    m2=pd.DataFrame(y_pre2)
    plt.plot(test["Date"], m1[0],  color='black')
    plt.xlabel("date")
    plt.ylabel("closed price")
    fig=plt.gcf()
    fig.set_size_inches(8,4, forward=True)
    fig.savefig('C:\\Users\\anton\\Desktop\\ML\\8.png', dpi=100)
    plt.plot(test["Date"], m2[0],  color='black')
    plt.xlabel("date")
    plt.ylabel("closed price")
    fig=plt.gcf()
    fig.set_size_inches(8,4, forward=True)
    fig.savefig('C:\\Users\\anton\\Desktop\\ML\\9.png', dpi=100)
    
    
    

    











if __name__ == '__main__':
    main()


