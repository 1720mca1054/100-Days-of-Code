punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = input("Enter a string: ")

no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

# output:


# Enter a string: qwerty!asdfg
# qwertyasdfg
