# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the CSV file
file_path = 'ABMatchData(FULL).csv'
match_data = pd.read_csv(file_path)

# Sorting data by Date to display matches in chronological order
match_data['Date'] = pd.to_datetime(match_data['Date'])  # Convert Date column to datetime
sorted_data = match_data.sort_values(by='Date')

# Plotting the match results (Result column) for each opposition
plt.figure(figsize=(12, 6))

# Bar plot showing results for each match
sns.barplot(y=sorted_data['Opposition Name'], x=sorted_data['Result'], hue=sorted_data['Opposition Name'], palette='coolwarm', dodge=False)

# Adding title and labels
plt.title('Match Results Against Opponents', fontsize=16)
plt.xlabel('Result (Point Difference)', fontsize=12)
plt.ylabel('Opposition Name', fontsize=12)

# Remove the legend as it's not needed
plt.legend([], [], frameon=False)

# Show the plot
plt.tight_layout()
plt.show()
