import re

def regfind(sentence):

 
    pattern = r'\b\d{5}_\d{5}\b'
    correct_code=re.findall(pattern,sentence)
    if correct_code:
        return correct_code
    else:
        return "There Is No Valid Postal Code!!"
    

#  main function


print("please Write Your Text:")
text1=input()
my_codes=regfind(text1)
print("the codes are : ",my_codes)