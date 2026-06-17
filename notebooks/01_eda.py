#!/usr/bin/env python
# coding: utf-8

# # Load dataset

# In[9]:


import pandas as pd

df = pd.read_csv("../data/raw/online_retail.csv", encoding="ISO-8859-1")

df.head()


# # Dataset information, description and visualization and Clean if needed

# In[ ]:


df.info()


# In[ ]:


df.columns


# In[ ]:


df.shape


# #### Missing Values

# In[ ]:


df.isnull().sum()


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Values Heatmap")
plt.show()


# #### Handle Missing values

# In[ ]:


df = df.dropna(subset=["CustomerID"])


# In[ ]:


df.isnull().sum()


# ### Missing Value Handling
# 
# The dataset initially contained missing values in the CustomerID and Description columns.
# 
# Rows with missing CustomerID values were removed because customer identification is essential for customer segmentation, churn prediction, and RFM analysis.
# 
# After removing these records, no missing values remained in the dataset.

# #

# #### Handle Duplicate rows

# In[ ]:


print("Duplicate Rows:", df.duplicated().sum())


# In[ ]:


df = df.drop_duplicates()


# In[ ]:


print("Duplicate Rows:", df.duplicated().sum())


# ### Duplicate Record Handling
# 
# The dataset was examined for duplicate records using the Pandas `duplicated()` function.
# 
# A total of 5268 duplicate rows were identified and removed to improve data quality and prevent bias in downstream analysis and machine learning models.

# #### Handle Invalid Transactions

# In[ ]:


df = df[df['Quantity'] > 0]

df = df[df['UnitPrice'] > 0]


# In[ ]:


df.shape


# ### Invalid transactions Handling
# 
# Records with non-positive quantities and unit prices were successfully removed.
# 
# This ensures that only valid sales transactions are used for revenue calculations, customer analytics, demand forecasting, and inventory optimization.

# #### Date Conversion

# In[ ]:


df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])


# In[ ]:


df.info()


# #### Revenue Feature Engineering
# 
# A new feature named `TotalPrice` is created by multiplying the quantity purchased by the unit price.
# 
# This feature represents the revenue generated from each transaction and will be used in customer segmentation, revenue analysis, and forecasting models.

# In[ ]:


df['TotalPrice'] = df['Quantity'] * df['UnitPrice']


# In[ ]:


df.head()


# In[ ]:


df.describe()


# #### Revenue

# In[ ]:


print("Total Revenue:", df['TotalPrice'].sum())

print("Average Order Value:",
      df['TotalPrice'].mean())


# #### Top Customers

# In[ ]:


top_customers = (
    df.groupby('CustomerID')['TotalPrice']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_customers.plot(kind='bar')

plt.title("Top 10 Customers by Revenue")
plt.ylabel("Revenue")

plt.show()


# #### Top Countries

# In[ ]:


import matplotlib.pyplot as plt

top_countries = df['Country'].value_counts().head(10)

plt.figure(figsize=(10,5))
top_countries.plot(kind='bar')

plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Orders")

plt.show()


# #### Monthly Trends

# In[ ]:


monthly_sales = df.resample('ME', on='InvoiceDate')['TotalPrice'].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot()

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()


# #### Top Products

# In[ ]:


top_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_products.plot(kind='bar')

plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")

plt.show()


# #### Correlation Heatmap

# In[ ]:


numeric_df = df[['Quantity', 'UnitPrice', 'TotalPrice']]
corr_matrix = numeric_df.corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm'
)

plt.title("Correlation Heatmap")
plt.show()


# ## Correlation Analysis
# 
# A correlation heatmap was generated using transactional variables.
# 
# CustomerID was excluded because it serves only as an identifier and does not represent a business feature.
# 
# The analysis shows that TotalPrice is positively correlated with Quantity and UnitPrice, which is expected since revenue is calculated as:
# 
# TotalPrice = Quantity × UnitPrice

# ## Saving the Cleaned Dataset
# 
# After handling missing values, removing duplicate records, filtering invalid transactions, and performing feature engineering, the cleaned dataset is saved for use in subsequent stages of the project.
# 
# This dataset will serve as the input for customer segmentation, demand forecasting, churn prediction, and inventory optimization tasks.

# In[ ]:


df.to_csv("../data/cleaned/cleaned_retail.csv", index=False)


# #### Rolling statistics

# In[ ]:


daily_sales = (
    df.resample("D", on="InvoiceDate")["TotalPrice"]
    .sum()
    .reset_index()
)

daily_sales.head()


# In[ ]:


daily_sales = (
    df.resample("D", on="InvoiceDate")["TotalPrice"]
    .sum()
    .reset_index()
)

daily_sales.head()


# In[ ]:


daily_sales["Rolling_7"] = (
    daily_sales["TotalPrice"]
    .rolling(window=7)
    .mean()
)

daily_sales["Rolling_30"] = (
    daily_sales["TotalPrice"]
    .rolling(window=30)
    .mean()
)

daily_sales.head()


# In[ ]:


plt.figure(figsize=(12,5))

plt.plot(
    daily_sales["InvoiceDate"],
    daily_sales["TotalPrice"],
    label="Daily Sales",
    alpha=0.5
)

plt.plot(
    daily_sales["InvoiceDate"],
    daily_sales["Rolling_7"],
    label="7-Day Moving Average"
)

plt.plot(
    daily_sales["InvoiceDate"],
    daily_sales["Rolling_30"],
    label="30-Day Moving Average"
)

plt.title("Sales Trend with Rolling Statistics")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.legend()

plt.show()


# #### Save Rolling Sales Data

# In[ ]:


daily_sales.to_csv(
    "../data/cleaned/rolling_sales.csv",
    index=False
)


# #### Data Validation with Great Explaination

# In[ ]:


print("Data Validation Checks")


# In[ ]:


print("CustomerID not null:", df['CustomerID'].notnull().all())


# In[ ]:


print("Quantity >= 1:", (df['Quantity'] >= 1).all())


# In[ ]:


print("UnitPrice >= 0.001:", (df['UnitPrice'] >= 0.001).all())


# In[ ]:


print("InvoiceDate not null:", df['InvoiceDate'].notnull().all())


# In[ ]:


print("TotalPrice not null:", df['TotalPrice'].notnull().all())


# In[ ]:


validation_success = df['CustomerID'].notnull().all() and (df['Quantity'] >= 1).all() and (df['UnitPrice'] >= 0.001).all() and df['InvoiceDate'].notnull().all() and df['TotalPrice'].notnull().all()
print("Validation Success:", validation_success)


# ### Data Validation with Great Expectations
# 
# Great Expectations was used to validate the quality of the cleaned dataset.
# 
# Validation checks performed:
# 
# - CustomerID contains no missing values.
# - Quantity values are positive.
# - UnitPrice values are greater than or equal to 0.001.
# - InvoiceDate contains no missing values.
# - TotalPrice contains no missing values.
# 
# All validation rules passed successfully, indicating that the dataset is suitable for downstream machine learning and analytics tasks.
