import pandas as pd
import numpy as np

df = pd.read_csv("Weather Dataset.csv")

print(df)

print("Total NUlll values :- \n ")
print(pd.isnull(df).sum())

#remove duplicates
df.drop_duplicates(inplace=True)

df["Date"] = pd.to_datetime(df["Date"],format="mixed" , errors="coerce")
df["Date"]= df["Date"].fillna(df["Date"].mean())
df["Date"]= df["Date"].dt.date



"""


df[["Weather" , "City"]] = df[["Weather" , "City"]].fillna(df[["Weather" , "City"]].mode().iloc[0])

print("Weather dtype :- ",df["Weather"].dtype)
df["Weather"] = df["Weather"].astype(str)

print("\n")

df["Weather"] = df["Weather"].str.lower()
df["Weather"] = df["Weather"].str.capitalize()
print(df["Weather"] , "\n")

#know the how Values missin gin Wind speed 
print("Wind speed missing - \t ",df["Wind_Speed"].isnull().sum() , "\n")

#description 
print(df["Wind_Speed"].describe())

#np.where (condition , true , false)
df["Wind_Speed"] = np.where((df["Wind_Speed"]<=200) ,df["Wind_Speed"].mean() , np.nan )

#filling the nan values 
df["Wind_Speed"] = df["Wind_Speed"].fillna(df["Wind_Speed"].mean())

print("Wind speed missing - \t ",df["Wind_Speed"].isnull().sum() , "\n")
"""

# Check missing values in Wind Speed
print("Wind speed missing - \t", df["Wind_Speed"].isnull().sum(), "\n")

# Convert Wind_Speed into numeric format
df["Wind_Speed"] = pd.to_numeric(df["Wind_Speed"], errors="coerce")

# Check statistics
print(df["Wind_Speed"].describe())

# Replace invalid values (greater than 200) with mean value
mean_wind_speed = df["Wind_Speed"].mean()

df["Wind_Speed"] = np.where(df["Wind_Speed"] > 200,mean_wind_speed,df["Wind_Speed"]
)

# Fill remaining missing values with mean
df["Wind_Speed"] = df["Wind_Speed"].fillna(mean_wind_speed)

df["Wind_Speed"]= df["Wind_Speed"].astype(int)
# Check missing values after cleaning
print("\nWind speed missing - \t", df["Wind_Speed"].isnull().sum(), "\n")

print(df["Wind_Speed"])

print("\n Already cheked Date , City , Rainfall , Weather no need to Clean \ n")


# Convert Rainfall to numeric
df["Rainfall"] = pd.to_numeric(df["Rainfall"], errors="coerce")

# Replace invalid values (less than 0) with NaN
df["Rainfall"] = np.where(
    df["Rainfall"] < 0,np.nan,df["Rainfall"]
)

df["Rainfall"] = df["Rainfall"].fillna(df["Rainfall"].mean())
df["Rainfall"] = df["Rainfall"].astype(int)




#humadity should have between 0 to 100
#df.loc[Conditon,"col"]= value  - select the specific rows and col and fill nan value 
df.loc[
    (df["Humidity"]<0 )| (df["Humidity"]>100) , "Humidity"
] = np.nan

#filling null values
df["Humidity"] = df["Humidity"].fillna(df["Humidity"].median())
#print(df)





print(df["Temperature"].describe())
print("\n")

#Temperature should have in valid instead of notreal
df.loc[
    (df["Temperature"]<-40) | (df["Temperature"]>60),"Temperature"
] = np.nan


df["Temperature"] = df["Temperature"].fillna(df["Humidity"].median())

"""#Remove extra space 
df["Temperature"] = df["Temperature"].astype(str).str.strip()
df["Temperature"] = df["Temperature"].str.lstrip("0")

#convert backe to numeric
df["Temperature"] = pd.to_numeric(df["Temperature"],errors="coerce")

"""
df["Temperature"] = df["Temperature"].astype(int)






df.to_csv("Weather Dataset Cleaned.csv",index=False)

print(df.isnull().sum())

print(" \n Cleaning Dataset - Done \n ")

