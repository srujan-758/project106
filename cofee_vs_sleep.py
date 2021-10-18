import csv
import numpy as np
import plotly.express as px

def getdataSource(data_path):
   cups_of_cofee=[]
   hours_of_sleep=[]

   with open(data_path) as csv_file:
     csv_reader=csv.DictReader(csv_file)

     for row in csv_reader:
       hours_of_sleep.append(float(row["sleep in hours"]))
       cups_of_cofee.append(float(row["Coffee in ml"]))

   return{"x":cups_of_cofee, "y":hours_of_sleep}

def findCorrelation(dataSource):
   correlation=np.corrcoef(dataSource["x"],dataSource["y"])
   print("correlation of coffee drank & hours of sleep is:-",correlation[0,1])       

def setup():
  data_path="cups of coffee vs hours of sleep.csv"

  dataSource=getdataSource(data_path)  
  findCorrelation(dataSource)

with open("cups of coffee vs hours of sleep.csv") as csv_file:
  df= csv.DictReader(csv_file)
  fig= px.scatter(df, x="Coffee in ml", y="sleep in hours")
  fig.show()    

setup()