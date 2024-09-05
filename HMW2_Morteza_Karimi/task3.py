def itmo(number):
    if number>=10:
     while(number>=10):
         number=sum(int(x) for x in  str(number))
     return number
    return "not valid number"
number=int(input(f'enter the number:\t'))
print("result:\t",itmo(number))
    