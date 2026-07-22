import pandas as pd 

# convert csv file into dataframe

df = pd.read_csv("student.csv")
print(df)

# convert dataframe into csv
df.to_csv("student1.csv")

# read json file 
df1 = pd.read_json("employee.json")

print(df1)

# convert dataframe into json 

df1.to_json("new_employee.json")

print(df1[df1["empname"]=="Rohit"])
print(df1[df1["role"]=="Admin"])
print("===============")
print(df1[df1["age"]>15])
print(df1[(df1["age"]>15)&(df1["role"]=="salesman")])

print("=================")

# read titanic.csv file 

data = pd.read_csv("titanic.csv")
print(data)

# print dimensions
print(data.shape)

# print all column names 

print(data.columns)

# print information about dataset 
print(data.info())

# print all statisics info about dataset 

print(data.describe())

# check how many null values in dataset 

print(data.isnull().sum())

# fill missing values using Mean/Median/Mode

data["age"] = data["age"].fillna(data["age"].mean())
# data["Age"] = data["Age"].fillna(data["Age"].median())
# data["Age"] = data["age"].fillna(data["age"].mode())
# data["Age"] = data["age"].fillna(data["age"].ffill())
# data["age"] = data["age"].fillna(data["age"].bfill())
# data["age"] = data["age"].fillna(0)


# count null values

print(data.isnull().sum())

data["embark_town"] = data["embark_town"].ffill()

print(data.isnull().sum())

# drop column 

data.drop("deck",axis=1,inplace=True)

print(data.isnull().sum())





