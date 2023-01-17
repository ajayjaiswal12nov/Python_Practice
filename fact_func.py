def list_factorial(list):
    for i in range(len(list)):
        factorial = 1
        element_list = list[i];
        #print("The list element is:",element_list)
        # check if the number is negative, positive or zero
        if element_list < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif element_list == 0:
            print("The factorial of 0 is 1")
        elif element_list < 1 or element_list > 9:
            print("Invalid scenario as per the range given in excercise. Range should be 1-9")
        else:
            for j in range(1,element_list+1):
                factorial = factorial*j
            print(factorial)