import re #import the regular expression module

names_file = open("names.txt", encoding="utf-8")
data = names_file.read() #read the file into data
names_file.close() #close the file and free up file descriptor

last_name = r'Love' #raw string
first_name = r'Kenneth' #raw string
print(re.match(last_name, data)) #match functions -- r tells that its a raw string-- no need for backslash character
print(re.search(first_name, data)) #search function for the firstname -- match object
print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data)) #search for phone number

# \w - matches any letter & \W any non-letter
# \s - matches any whitespace & \S any non-whitespace
# \d - matches any digit & \D any non-digit
# \b - matches word boundary & \B any non-word boundary
#() - group things together