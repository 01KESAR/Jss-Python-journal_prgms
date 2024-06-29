# write python prgm to explore string functions

str1="jss college"
str2="python program"
print("first string is ",str1)
print("second string is",str2)
print("change ",str1,"to uppercase=",str1.upper())
print("change ",str2,"to title case=",str2.title())
print("no of occurences of string p in",str2,"=",str2.count('p'))
print("length  of ",str1,"=",len(str1))
print("string ",str1,"starts with jks",str1.startswith('jks'))
print("string",str2,"ends with m",str2.endswith('m'))
print("string  pr in ",str2,"is positioned at",str2.find('pr'))
print('after joining * in',str2, '*'.join (str2))