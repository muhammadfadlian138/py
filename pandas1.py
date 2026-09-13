import pandas as pd 
print(pd.__version__)

#df = pd.read_csv('datasets.csv')
#print(df.to_string())

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar2 = pd.Series(calories)
print(myvar2)
