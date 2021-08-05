


import re

txt = "RegEx can be used to check if a string contains the specified search pattern."
x = re.search("RegEx", txt)
print(x)

#findall()
#The findall() function returns a list containing all matches.

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "RegEx can be used to check if a string contains the specified search pattern."
x = re.findall("RegEx", txt)
print(x)


#search() function
'''The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned'''

txt = "RegEx can be used to check if a string contains the specified search pattern."
x = re.search("check", txt)
print(x)


txt = "RegEx can be used to check if a string contains the specified search pattern."
x = re.search("checks", txt) #returns None if no match is found
print(x)



#split() function
#The split() function returns a list where the string has been split at each match

txt = "The rain in Spain"
x = re.split("\t", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\n", txt, 1)
print(x)

#sub() function
#The sub() function replaces the matches with the text of your choice

txt = "RegEx can be used to check if a string contains the specified search pattern."
x = re.sub("\s","meena", txt)
print(x)

txt = "RegEx can be used to check if a string contains the specified search pattern."
x = re.sub("\s","meena", txt,4)#we can control the number of replacements by specifying the count parameter
print(x)


