import pandas as pd

# df = pd.DataFrame({
#     "Name":["Shadow", "Blaze", "Requiem", "Glitch", "Flash Fire", "Tidal Wave", "Howling Wind", "Striking Quake", "Gello"],
#     "Age":[15, 15, 15, 16, 17, 16, 17, 18, 15],
#     "Place of Origin":["Raven Mountain", "Raven Mountain", "Spectral Realm", "End District Underdepths", "Cienfuegos District", "Aqueous Palace", "Vientos Village", "Skystreak Mountain", "Poco Town"]    
# })

# #Prints what's in the arrays
# #Default: only prints 5
# print(df.head())
# print(df.head(9))

# #tells you the number of rows and columns
# print(df.shape)

# # Gives the typical summary of the data - very nerdy schtuff
# print(df.info())

# #Gives the important calculations on the numerical columns
# print(df.describe())

# #shows a specific column
# print(df["Name"])

# #Also all previous numpy operations work on the columns
# print(df["Age"].max())
# print(df["Age"].shape)

#loading data from a file
data = pd.read_csv("Titanic.csv")
print(data.head(886))
print(data.info())

#prints all the ones older than 35
above35 = data[data["Age"] > 35]
print(above35.head())
print(above35.shape)