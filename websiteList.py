import pandas as pd
import os

date_path = "data/Rides/combined_datetime.csv"
save_path = "data/Rides/date_url.csv"
website = 'https://www.thrill-data.com/waits/park/dlr/disneyland/'
df = pd.read_csv(date_path)

df = df.drop_duplicates(subset=['Date'], keep='first')

# Drop the columns you don't want (e.g., 'column_to_drop1', 'column_to_drop2')
df = df.drop(columns=['Date/Time', 'Time', 'Day of Week', 'Weekend'])

df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by the 'Date' column
df_sorted = df.sort_values(by='Date')

# Convert the sorted dates to string format (YYYY/MM/DD)
df_sorted['Formatted_Date'] = df_sorted['Date'].dt.strftime('%Y/%m/%d')

# Append each formatted date to the base website URL and store it in a new column
df_sorted['Website_with_Date'] = website + df_sorted['Formatted_Date']

df_sorted = df_sorted.drop(columns=['Formatted_Date'])

# Display the result
df_sorted.to_csv(save_path, index=False)

os.makedirs(os.path.dirname(save_path), exist_ok=True)
absolute_path = os.path.abspath(save_path)

print(f"DataFrame successfully saved to '{absolute_path}'")
