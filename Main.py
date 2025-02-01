import pandas as pd

df = pd.DataFrame({
    "Name":["Shadow", "Blaze", "Requiem", "Glitch", "Flash Fire", "Tidal Wave", "Howling Wind", "Striking Quake", "Gello"],
    "Age":[15, 15, 15, 16, 17, 16, 17, 18, 15],
    "Place of Origin":["Raven Mountain", "Raven Mountain", "Spectral Realm", "End District Underdepths", "Cienfuegos District", "Aqueous Palace", "Vientos Village", "Skystreak Mountain", "Poco Town"]    
})

#Prints what's in the arrays
#Default: only prints 5
print(df.head())
print(df.head(9))

#tells you the number of rows and columns
print(df.shape)

# Gives the typical summary of the data - very nerdy schtuff
print(df.info())

#Gives the important calculations on the numerical columns
print(df.describe())

#shows a specific column
print(df["Name"])

#Also all previous numpy operations work on the columns
print(df["Age"].max())
print(df["Age"].shape)

#loading data from a file
data = pd.read_csv("C:/Users/diego/JetLearn/Data Science/Lesson 3/Titanic.csv")
print(data.head(886))
print(data.info())

#prints all the ones older than 35
above35 = data[data["Age"] > 35]
print(above35.head())
print(above35.shape)

#selecting certain 'people' whos' classes were 2 and 3
class_2_and_3 = data[data["Pclass"].isin([2,3])]
print(class_2_and_3[["Name","Pclass",]].head())
print(class_2_and_3.shape)

#For combining different conditions, we can use OR (|), or AND (&)
class_2_and_3 = data[(data["Pclass"] == 2) | (data["Pclass"] == 3)]
print(class_2_and_3[["Name","Pclass",]].head())
print(class_2_and_3.shape)

male_class_1 = data[(data["Pclass"] == 1) & (data["Sex"] == "male")]
print("The mean fare for a man in 1st class was",male_class_1["Fare"].mean())
female_class_1 = data[(data["Pclass"] == 1) & (data["Sex"] == "female")]
print("The mean fare for a woman in 1st class was",female_class_1["Fare"].mean())

male_class_2 = data[(data["Pclass"] == 2) & (data["Sex"] == "male")]
print("The mean fare for a man in 2nd class was",male_class_2["Fare"].mean())
female_class_2 = data[(data["Pclass"] == 2) & (data["Sex"] == "female")]
print("The mean fare for a woman in 2nd class was",female_class_2["Fare"].mean())

male_class_3 = data[(data["Pclass"] == 3) & (data["Sex"] == "male")]
print("The mean fare for a man in 3rd class was",male_class_3["Fare"].mean())
female_class_3 = data[(data["Pclass"] == 3) & (data["Sex"] == "female")]
print("The mean fare for a woman in 3rd class was",female_class_3["Fare"].mean())

male = data[(data["Sex"] == "male")]
print("The mean fare for a man was",male["Fare"].mean())
female = data[(data["Sex"] == "female")]
print("The mean fare for a woman was",female["Fare"].mean())
