import  re

my_string = 'f456.89ts'
str_list = my_string.split()
print(str_list)

pattern="\d+"
str_list=re.findall(pattern,my_string)
print("List of numbers in string format is:")
print(str_list)
num_list=[int(i) for i in str_list]
print("Output List of numbers is:")
print(num_list)