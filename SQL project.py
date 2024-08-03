#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Replace 'file_path' with your actual file path
df = pd.read_csv('Wal.csv')


# In[3]:


print(df.head())
print(df.info())


# In[6]:


# Drop duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.dropna(inplace=True)

# Convert data types if necessary
df['date'] = pd.to_datetime(df['Date'])


# In[7]:


# Example: Extract day of the week and month
df['day_name'] = df['date'].dt.day_name()
df['month'] = df['date'].dt.month_name()


# In[8]:


# Example: Calculate VAT and total revenue
df['VAT'] = 0.05 * df['cogs']
df['total_revenue'] = df['cogs'] + df['VAT']


# In[9]:


print(df.describe())


# In[10]:


# Example: Bar plot of total revenue by month
plt.figure(figsize=(10, 6))
sns.barplot(x='month', y='total_revenue', data=df, estimator=sum, ci=None)
plt.title('Total Revenue by Month')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.show()


# In[12]:


# Example: Calculate total revenue by product line
revenue_by_product_line = df.groupby('Product line')['total_revenue'].sum().reset_index()
print(revenue_by_product_line)


# In[15]:


# Example: Number of unique cities
unique_cities = df['City'].nunique()
print(f"Number of unique cities: {unique_cities}")

# Example: Most common payment method
common_payment_method = df['Payment'].mode()[0]
print(f"Most common payment method: {common_payment_method}")


# In[ ]:




