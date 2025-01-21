#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import os
import re
import pandas as pd
import matplotlib.pyplot as plt


# In[17]:


print("Display the results of the asymptotic analysis on the Sorting Algorithms:")


# In[18]:


# Get the current working directory
current_folder = os.getcwd()
print("Current folder:", current_folder)


# In[19]:


# List all files in the current folder that contain the information about the execution times

files = []

# Iterate over all items in the folder
for item in os.listdir(current_folder):
    if os.path.isfile(os.path.join(current_folder, item)):
        files.append(item)

print("Files in the current folder:")
print(files)


# In[20]:


# Pilot Code
# Show the content of a FIRST file in the folder, verify its content and prepare a DATAFRAME to store the RESULTS

if files:
    first_file = files[0]          # Get the first file
    first_file_path = os.path.join(current_folder, first_file)

    # Open and read the content of the first file
    with open(first_file_path, 'r') as file:
        content = file.read()

        # Original filename :  
        print("File name:", first_file)

        # Use a regular expression to extract the desired part of the filename
        match = re.search(r'\d+', first_file)

        # Check if the pattern is found
        if match:
           extracted_name = match.group()  # Extract the matched text
           print(f"Variable name: {extracted_name}")
        else:
           print("Pattern not found in the filename.")
else:
    print("No files found in the folder.")


# In[6]:


# Apply the same procedure for all the files that contain the execution times for each sorting algorithm


# In[21]:


# List to store data for the DataFrame
data = []

# Process each file in the folder
for afile in files:
    print("\nProcessing file:", afile)

    # Step 1: Extract the file name
    match = re.search(r'\d+', afile)

    if match:
        variable_name = match.group() 
        print(f"Recorded name: {variable_name}")
    else:
        print("Pattern not found in the filename.")
        continue  # Skip to the next file if pattern is not found

    # Step 2: Extract the information from the file content
    try:
        with open(os.path.join(current_folder, afile), 'r') as file:
            for line in file:
                if "Execution Time for" in line:
                    
                    # Extract sort type and execution time
                    parts = line.split(":")
                    algorithm = parts[0].replace("Execution Time for", "").strip()
                    time_in_seconds = float(parts[1].strip().split()[0])  # Extract time as float
                    
                    # Append the variable name, algorithm, and time to the data list
                    data.append([variable_name, algorithm, time_in_seconds])

    except Exception as e:
        print(f"Could not process file '{afile}': {e}")

# Step 3: Create a DataFrame from the collected data
df = pd.DataFrame(data, columns=["patients", "algorithm", "time"])

# Display the DataFrame
print("\nDataFrame of Execution Times:")
print(df)

# Save the DataFrame to a CSV file
# df.to_csv("the_execution_times_summary.csv", index=False)


# In[ ]:





# In[22]:


# Exclude rows with "Insertion Sort"
df2 = df[df['algorithm'] != 'Insertion Sort']

# Display the updated DataFrame
print(df2)

# Exclude rows with 10000 patients
# df3 = df2[df2['patients'] != 10000]

# Display the updated DataFrame
# print(df3)


# In[23]:


df = df2
# Save the DataFrame to a CSV file
df.to_csv("the_execution_times_summary.csv", index=False)


# In[24]:


# Display the AVERAGE RUNNING TIMES of each algorithm

average_times = df.groupby('algorithm')['time'].mean().sort_values()
print(average_times)

plt.figure(figsize=(4, 4))
average_times.plot(kind='bar')
plt.title('Average Execution Time by Algorithm')
plt.ylabel('Time (seconds)')
plt.xlabel('Algorithm')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[25]:


# Filter the DataFrame to exclude "Bubble Sort" and "Selection Sort"
df2 = df[df['algorithm'].isin(['Bubble Sort', 'Selection Sort']) == False]
print(df2)

# Calculate the mean execution times for the filtered algorithms
average_times2 = df2.groupby('algorithm')['time'].mean().sort_values()

# Create a bar plot
plt.figure(figsize=(4, 4))
average_times2.plot(kind='bar')
plt.title('Average Execution Time by Algorithm (Excluding Bubble and Selection Sort)', fontsize=10)
plt.ylabel('Time (seconds)')
plt.xlabel('Algorithm')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[26]:


df_pivot = df.pivot(index='patients', columns='algorithm', values='time')
print(df_pivot)

df2_pivot = df2.pivot(index='patients', columns='algorithm', values='time')
print(df2_pivot)


# In[27]:


# Sort the dataframe indexes

df_pivot.index = df_pivot.index.astype(int)
df_pivot_sorted = df_pivot.sort_index()
print(df_pivot_sorted)

df2_pivot.index = df2_pivot.index.astype(int)
df2_pivot_sorted = df2_pivot.sort_index()
print(df2_pivot_sorted)


# In[28]:


# Plot a line for each algorithm
plt.figure(figsize=(10, 8))
for algorithm in df_pivot_sorted.columns:
    plt.plot(df_pivot_sorted.index, df_pivot_sorted[algorithm], marker='o', label=algorithm)

# Add titles and labels
plt.title('Execution Times by Algorithm Across Different Patient Sizes', fontsize=14)
plt.xlabel('Number of Patients', fontsize=12)
plt.ylabel('Time (seconds)', fontsize=12)
plt.legend(title='Algorithm')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[29]:


# Plot a line for each algorithm
plt.figure(figsize=(10, 8))
for algorithm in df2_pivot_sorted.columns:
    plt.plot(df2_pivot_sorted.index, df2_pivot_sorted[algorithm], marker='o', label=algorithm)

# Add titles and labels
plt.title('Execution Times by Algorithm Across Different Patient Sizes', fontsize=14)
plt.xlabel('Number of Patients', fontsize=12)
plt.ylabel('Time (seconds)', fontsize=12)
plt.legend(title='Algorithm')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[31]:


# Filter the DataFrame to keep only "Quick Sort" and "Heap Sort"
df3 = df2[df2['algorithm'].isin(['Quick Sort', 'Heap Sort']) == True]
print(df3)

# Calculate the mean execution times for the filtered algorithms
average_times3 = df3.groupby('algorithm')['time'].mean().sort_values()

# Pivot / reshape the table
df3_pivot = df3.pivot(index='patients', columns='algorithm', values='time')
print(df3_pivot)

# Sort the dataframe indexes
df3_pivot.index = df3_pivot.index.astype(int)
df3_pivot_sorted = df3_pivot.sort_index()
print(df3_pivot_sorted)


# In[32]:


# Plot a line for each algorithm
plt.figure(figsize=(10, 8))
for algorithm in df3_pivot_sorted.columns:
    plt.plot(df3_pivot_sorted.index, df3_pivot_sorted[algorithm], marker='o', label=algorithm)

# Add titles and labels
plt.title('Execution Times by Algorithm Across Different Patient Sizes', fontsize=14)
plt.xlabel('Number of Patients', fontsize=12)
plt.ylabel('Time (seconds)', fontsize=12)
plt.legend(title='Algorithm')
plt.grid(True)
plt.tight_layout()
plt.show()


# In[ ]:




