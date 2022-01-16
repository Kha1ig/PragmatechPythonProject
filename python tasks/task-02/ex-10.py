### 9-cu tapşırıq:
# my_text = “Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.” 
# my_text stringindeki sozler elifba sirasi ile duzub string formatinda ekrana yazdirin.

my_text = "Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings."

text = [i.lower() for i in my_text.split()]
print(text)
text.sort()

for i in text:
    print(i)
