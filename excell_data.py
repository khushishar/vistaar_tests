import pandas as pd 
import os
def datastore(name,email,salary,occupation):
    if os.path.isfile("user_data.xlsx"):
        df=pd.read_excel("user_data.xlsx")
        df.append([name,email,salary,occupation])
        df.to_excel("user_data.xlsx",index=False)
    else:
         df=pd.DataFrame([name,email,salary,occupation],columns=["Name","Email","Salary","Occupation"])
         df.to_excel("user_data.xlsx",index=False)


         