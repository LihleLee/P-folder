# Import necessary libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the CSV file
file_path = 'ABMatchData(FULL).csv'
match_data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Information:")
print(match_data.info())
print("\nSummary Statistics:")
print(match_data.describe())

# Check for missing values
print("\nMissing Values:")
print(match_data.isnull().sum())

# Handle missing data: fill with 0 or drop as appropriate (modify as per your dataset)
match_data.fillna(0, inplace=True) 

# Remove duplicate data
match_data.drop_duplicates(inplace=True)

# Ensure appropriate data types
match_data['Date'] = pd.to_datetime(match_data['Date']) 
sorted_data = match_data.sort_values(by='Date')

# Set up the figure and axes for subplots
fig, axs = plt.subplots(3, 1, figsize=(14, 17))  

# Plot 1: Debutants (User vs Opposition)
sns.lineplot(ax=axs[0], x=sorted_data['Date'], y=sorted_data['Debutants'], label='Team Debutants', marker='o')
sns.lineplot(ax=axs[0], x=sorted_data['Date'], y=sorted_data['Opposition Debutants'], label='Opposition Debutants', marker='o')
axs[0].set_title('Debutants Over Time')
axs[0].set_xlabel('Date')
axs[0].set_ylabel('Number of Debutants')
axs[0].legend()

# Plot 2: Tries in last 5 games (User vs Opposition)
sns.lineplot(ax=axs[1], x=sorted_data['Date'], y=sorted_data['Tries in last 5 games'], label='Team Tries', marker='o')
sns.lineplot(ax=axs[1], x=sorted_data['Date'], y=sorted_data['Opposition tries in last 5 games'], label='Opposition Tries', marker='o')
axs[1].set_title('Tries in Last 5 Games')
axs[1].set_xlabel('Date')
axs[1].set_ylabel('Number of Tries')
axs[1].legend()

# Plot 3: Team Ratings (User vs Opposition)
sns.lineplot(ax=axs[2], x=sorted_data['Date'], y=sorted_data['Rating'], label='Team Rating', marker='o')
sns.lineplot(ax=axs[2], x=sorted_data['Date'], y=sorted_data['Opposition Rating'], label='Opposition Rating', marker='o')
axs[2].set_title('Team Ratings Over Time')
axs[2].set_xlabel('Date')
axs[2].set_ylabel('Rating')
axs[2].legend()

# Add overall title
plt.suptitle('Comprehensive Match Data Analysis', fontsize=16)

# Adjust layout for better visualization
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show the plot
plt.show()

# Additional Data Exploration: Histogram of Tries in last 5 games
plt.figure(figsize=(10, 6))
sns.histplot(match_data['Tries in last 5 games'], bins=10, kde=True)
plt.title('Distribution of Tries in Last 5 Games')
plt.xlabel('Number of Tries')
plt.ylabel('Frequency')
plt.show()

# Data Analysis: Correlation between tries and ratings
correlation = match_data[['Tries in last 5 games', 'Rating']].corr()
print("\nCorrelation between Tries and Ratings:")
print(correlation)
