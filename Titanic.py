#!/usr/bin/env python
# coding: utf-8

# In[22]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd.read_csv('C:/Users/Harsha/Downloads/titanic.csv')
print(titanic_data.head())


# In[12]:


columns_to_drop = ['embarked', 'who', 'adult_male', 'embark_town', 'alive', 'alone']
titanic_data = titanic_data.drop(columns=columns_to_drop)

# Display the first few rows of the updated dataset
print(titanic_data.head())


# In[15]:


print(titanic_data.columns)


# In[16]:


# Count passengers without deck information
missing_deck_info = titanic_data['deck'].isna().sum()

# Display the result
print(f"Number of passengers without deck information: {missing_deck_info}")



# In[17]:


# Count the number of infants (age < 3)
infants_count = len(titanic_data[titanic_data['age'] < 3])

# Count the number of children (ages 5-10)
children_count = len(titanic_data[(titanic_data['age'] >= 5) & (titanic_data['age'] <= 10)])

# Display the results
print(f"Number of infants on board: {infants_count}")
print(f"Number of children (ages 5-10) on board: {children_count}")


# In[19]:


# Create a new column 'age_group' based on age ranges
titanic_data['age_group'] = pd.cut(
    titanic_data['age'],
    bins=[-1, 3, 18, 90],  # Define age ranges
    labels=['infants', 'children', 'adults']
)

# Display the first few rows to verify the new column
print(titanic_data[['age', 'age_group']].head())
print(titanic_data[['age', 'age_group']])


# In[23]:


# KDE plot for the 'age' variable, excluding missing values
plt.figure(figsize=(10, 6))
sns.kdeplot(titanic_data['age'].dropna(), shade=True)

# Set plot title and labels
plt.title('Kernel Density Estimation Plot for Age')
plt.xlabel('Age')
plt.ylabel('Density')

# Display the plot
plt.show()


# In[ ]:




