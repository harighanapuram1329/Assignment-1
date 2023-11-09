import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the provided CSV file
data = pd.read_csv("generic_ballot_averages.csv")

# Define a function to group dates into date ranges
def group_dates(date_series, date_format="%Y-%m-%d", range_format="%b '%y"):
    date_series = pd.to_datetime(date_series)
    date_ranges = date_series.dt.strftime(range_format)
    return date_ranges

# Apply the date grouping to the 'date' column
data['date_ranges'] = group_dates(data['date'])

# Function to create a line plot with date ranges on the x-axis
def create_line_plot(data):
    plt.figure(figsize=(12, 6))
    for party in data['candidate'].unique():
        party_data = data[data['candidate'] == party]
        plt.plot(party_data['date_ranges'], party_data['pct_estimate'], label=party)

    plt.xlabel('Date Range')
    plt.ylabel('Percentage Estimate')
    plt.title('Line Plot of Generic Ballot Averages')
    plt.legend()
    
    plt.xticks(rotation=45, ha="right")
    
    plt.tight_layout() 
    plt.show()

# Function to create a bar chart
def create_bar_chart(data):
    plt.figure(figsize=(10, 6))
    party_data = data.groupby('candidate')['pct_estimate'].mean()
    party_data.plot(kind='bar')
    plt.xlabel('Party')
    plt.ylabel('Average Percentage Estimate')
    plt.title('Bar Chart of Generic Ballot Averages')
    plt.xticks(rotation=0)
    plt.show()

# Function to create a scatter plot
def create_scatter_plot(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['lo'], data['hi'], c=data['pct_estimate'], cmap='viridis', alpha=0.5)
    plt.colorbar(label='Percentage Estimate')
    plt.xlabel('Low Estimate')
    plt.ylabel('High Estimate')
    plt.title('Scatter Plot of Generic Ballot Averages')
    plt.show()

# Create the line plot with date ranges on the x-axis
create_line_plot(data)

# Create a bar chart
create_bar_chart(data)

# Create a scatter plot
create_scatter_plot(data)
