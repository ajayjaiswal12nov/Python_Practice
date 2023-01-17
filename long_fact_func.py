def long_factorial(sorted_list):
    #factorial = 1
    for i in range(len(sorted_list)):
        if len(sorted_list) == 1:
            temp_fact = sorted_list[0]
        elif i < len(sorted_list) - 1:
            temp_fact = sorted_list[i]
            new_fact = sorted_list[i+1]
            loop_start = new_fact-temp_fact
            loop_end = new_fact
        else:
            temp_fact = sorted_list[i]
        #loop_start = new_fact-temp_fact
        #loop_end = new_fact
        element_list = sorted_list[i];
        #print("The list element is:",element_list)
        # check if the number is negative, positive or zero
        if element_list < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif element_list == 0:
            print("The factorial of 0 is 1")
        #elif element_list < 1 or element_list > 9:
            #print("Invalid scenario as per the range given in excercise. Range should be 1-9")
        else:
            temp_fact = 1
            if len(sorted_list) == 1:
                for j in range(1,sorted_list[0]+1):
                    temp_fact = temp_fact*j
            #print(temp_fact)
            else:
                temp_fact = 1
                for j in range(1,element_list+1):
                    temp_fact = temp_fact*j
                new_fact = 1
                for k in range(loop_start,loop_end+1):
                    new_fact = new_fact*k
                #print(new_fact)
            if sorted_list[0]:
                factorial = temp_fact
            else:
                factorial = temp_fact*new_fact
            print(factorial)