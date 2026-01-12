import pandas as pd 

df1=pd.read_csv("data/daily_sales_data_0.csv")
df2=pd.read_csv("data/daily_sales_data_1.csv")
df3=pd.read_csv("data/daily_sales_data_2.csv")

df1=df1[df1["product"]=="pink morsel"]
df2=df2[df2["product"]=="pink morsel"]
df3=df3[df3["product"]=="pink morsel"]

df1["sales"]=df1["quantity"]*df1["price"]
df2["sales"]=df2["quantity"]*df2["price"]
df3["sales"]=df3["quantity"]*df3["price"]

df1 = df1[["sales","date","region"]]
df2 = df2[["sales","date","region"]]
df3 = df3[["sales","date","region"]]

df=pd.concat([df1,df2,df3],ignore_index=True)

df.to_csv("sales_data.csv", index=False)