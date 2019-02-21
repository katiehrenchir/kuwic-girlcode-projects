
# Open the CSV file and "read" the contents
with open("words.csv", "r") as f:
    # Try this part with both read() and readline()
    contents = f.readline()
    
print(contents)