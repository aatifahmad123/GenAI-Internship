import pandas as pd

print("\nDataset 1\n")

df1 = pd.read_excel("01 Call-Center-Dataset.xlsx")
print("Preview:")
print(df1.head())
print("\n")

print("Shape:")
print(df1.shape)
print("\n")

print("Info:")
print(df1.info())
print("\n")

print("Missing Values:")
print(df1.isnull().sum())
print("\n")

df1_cleaned = df1.dropna()
print("Shape after cleaning:",df1_cleaned.shape)
print("\n")

print("Distribution of Topic:")
print(df1_cleaned['Topic'].value_counts())
print("\n")

print("\nDataset 2\n")

df2 = pd.read_csv("customer_call_transcriptions.csv")

print("Preview:")
print(df2.head())
print("\n")

print("Shape:")
print(df2.shape)
print("\n")

print("Info:")
print(df2.info())
print("\n")

print("Missing Values:")
print(df2.isnull().sum())
print("\n")

print("Distribution of sentiment label:")
print(df2['sentiment_label'].value_counts())
print("\n")

negative_row = df2.iloc[0,:]
print("Text:",negative_row['text'])
print("Sentiment Label:",negative_row['sentiment_label'])
print("\n")

positive_row = df2.iloc[16,:]
print("Text:",positive_row['text'])
print("Sentiment Label:",positive_row['sentiment_label'])
print("\n")

neutral_row = df2.iloc[1,:]
print("Text:",neutral_row['text'])
print("Sentiment Label:",neutral_row['sentiment_label'])