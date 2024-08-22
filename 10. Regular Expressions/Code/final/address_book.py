import re #import the regular expression module

names_file = open("names.txt", encoding="utf-8")
data = names_file.read() #read the file into data
names_file.close() #close the file and free up file descriptor

# last_name = r'Love' #raw string
# first_name = r'Kenneth' #raw string
# print(re.match(last_name, data)) #match functions -- r tells that its a raw string-- no need for backslash character
# print(re.search(first_name, data)) #search function for the firstname -- match object
# print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data)) #search for phone number

#print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data)) #findall function for phone number

#print(re.findall(r'\w*, \w+', data)) #findall function for names e.g Love, Kenneth

#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
#print(re.findall(r'\b[trehous]{9}\b', data, re.I))
#print(re.findall(r'''
#    \b@[-\w\d.]*  # First a word boundary, an @, and then any number of characters
#    [^gov\t]+  # Ignore 1+ instances of the letters 'g', 'o', or 'v' and a tab.
#    \b  # Match another word boundary
#''', data, re.VERBOSE|re.I))
#print(re.findall(r"""
#    \b[-\w]+,  # Find a word boundary, 1+ hyphens or characters, and a comma
#    \s  # Find 1 whitespace
#    [-\w ]+  # 1+ hyphens and characters and explicit spaces
#    [^\t\n]  # Ignore tabs and newlines
#""", data, re.X))
line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
    (?P<twitter>@[\w\d]+)?$  # Twitter
''', re.X|re.M)

#print(line.search(data).groupdict())
for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))

#  Notes:
# \w - matches any letter & \W any non-letter
# \s - matches any whitespace & \S any non-whitespace
# \d - matches any digit & \D any non-digit
# \b - matches word boundary & \B any non-word boundary
# () - group things together
# {} - specifies the number of times to match. Counts. There is 
# *, ?, + - specifies the number of times to match. * is 0 or more, ? is 0 or 1, + is 1 or more
# Count. 
# re functions -- match, search, findall, compile, 
# sets - find a set of characters. e.g [trehous] finds any of the characters in the set
# [a-z] - finds any lowercase letter, [A-Z] finds any uppercase letter, [0-9] finds any digit
#re.INGORECASE or re.I - ignores case is used for case insensitive matching
#re.VERBOSE or re.X - used for multiline regular expressions
#finditer - finds all the matches in the data
# a set of characters - [trehous] finds any of the characters in the set
# A negative set - [^trehous] finds any character that is not in the set
