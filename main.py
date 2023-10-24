import math
def get_ISBN():
    
    ISBN = str(input("please enter an ISBN wiht single missing digit as a ?: "))
    
    valid = True
    while valid:
        if ISBN == ""  or (len(ISBN)) != 10 or (ISBN.find("?")) == -1 or ( (ISBN.replace("?","")).replace("x","") ).isdigit() == False:
            ISBN = str(input("Please enter an ISBN with 10 numerical digits including question mark: "))
        else:
            valid = False

    return ISBN

def validation(ISBN):
    result = ""
    total = 0
    count= 10
    for x in ISBN:
        if x == "?":
            total = total
        elif x == "x":
            total = total + 10
        
        else:
            total = total + ((int(x))*count)
        count -= 1
    
    pos = 10 - (int((ISBN.find("?"))))
    find = math.ceil((total / 11))
    rest = (find * 11) - total
    finder = find +1
    state = True
    while state:
        if ((rest/pos).is_integer()) == False:
            rest = (finder * 11) - total
            finder += 1
        else:
            state = False

    
    left = rest/pos


    
    print(total)
    print(rest)
    print(pos)
    print(left)
    
    
    
    
    
    if  left == 10 and pos == 1:
        result = "x"
    
    elif left == 0:
        result = "0"
    elif left < 1 or left > 9 or (left.is_integer()) == False: 
        result = "not found"
    else:
        result = (str(left))
    
    return result 

def main():
    ISBN = get_ISBN()
    print("ISBN: " + ISBN)
    result = (validation(ISBN))
    print("The missing number is : " + result )

main()