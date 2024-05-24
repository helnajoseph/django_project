import pandas as pd
import joblib


def predict():
        df1=pd.read_csv('media/input/test/test.csv')

        df1.head()


        df=df1.iloc[:,1:-1]

        model=joblib.load("ML/ds1.joblib")



        file=open("ml/map.txt","r")
        maps=file.read()
        file.close()
        maps=eval(maps)
        maps

        pred=model.predict(df)
        pred[0]


        if pred[0]==0:
                out='Antivirus'
        elif pred[0]==1:
                out='Manual Scan'
        elif pred[0]==2:
                out='Firewall Detection'
         
        return out

