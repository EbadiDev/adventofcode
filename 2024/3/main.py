#find mul then multiple it then sum it up all
#xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

import re

def find_mul(x: str):
    pattern = r'((?:don\'t|do)\(\))|(mul\((\d+),(\d+)\))'
    matches = re.findall(pattern, x)
    
    enabled = True  
    result = 0
    
    for match in matches:
        control, _, num1, num2 = match
        if control == "do()":
            enabled = True
        elif control == "don't()":
            enabled = False
        elif enabled and num1 and num2:
            result += int(num1) * int(num2)
    
    return result


# data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
with open(file='input.txt', mode='r') as file:
    context = file.read()
    print(find_mul(context))   

