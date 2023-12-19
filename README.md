1. Write function folding, which calculates the index for given string in hash table using the folding method. The strings only contain numbers.

The method takes three parameters: the string to be indexed (pn), the length of substring (n) and hash table size (size). 

For example, when the string is "123456" and n = 2, the string is split into substrings "12", "34" and "56". If n is 3, then the substrings are "123" and "456". 

The function prototype should be:
def folding(pn,n,size):
   # your answer code here
For example:
Test	Result
pn = "0401234567"
n=2
size = 11
print(folding(pn,n,size))	8
pn = "987654321"
n = 3
size = 20
print(folding(pn,n,size))	2


2. Question text 1
In a list of strings, find and print out the strings containing the given substring. Printing should be done in an alphabetical order.

The function prototype is shown below. The parameter string_list is the list containing the strings and and find_string is the substring to be found:
def sort_subs(string_list, find_string):
    // your answer code here

Hint: It might be good idea to first look into the documentation python strings, most likely you'll find operations that do lot of things for you already..

For example:
Test	Result
string_list = ["Ball", "Keys", "Fall", "Urge", "All", "Dorm", "Wall", "Tell", "Jive", "Fizz" ]
find_string = "ll"
sort_subs(string_list,find_string)	['All', 'Ball', 'Fall', 'Tell', 'Wall']

string_list = ["Ball", "Keys", "Fall", "Urge", "All", "Dorm", "Wall", "Tell", "Jive", "Fizz" ]
find_string = "zz"
sort_subs(string_list,find_string)	



Q2
Find missing numbers in a list of integers from 0 to 9 and print out a list of those.

For example: a list [ 0, 1, 3, 4, 5, 7, 8, 9 ] is missing numbers 2 and 6. List [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ] is missing number 9.

The function prototype is shown below. The parameter num_list is the list containing the numbers:
def missing_number(num_list):
    // your answer code here

For example:
Test	Result
num_list = [ 0, 1, 3, 4, 5, 7, 8, 9]
missing_number(num_list)	[2, 6]


num_list = []
missing_number(num_list)	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


Q3
Sort a list of integers using selection sort (the general unoptimized version) and then print out the sorted list, the number of comparisons and swaps that occurred during the sorting process.

The function prototype is, where the parameter data is the list of integers to be sorted:
def selection_sort(data):
    // your answer code here

For example:
Test	Result
data = [6, 5, 4, 3, 2, 1 ]
selection_sort(data)	[1, 2, 3, 4, 5, 6]
comparisons: 15
swaps: 5



import random

data = list(range(0, 20))
random.seed(5)
random.shuffle(data)
selection_sort(data)
	[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
comparisons: 190
swaps: 19


3. Q1 
Write function list_factorial, which takes a list of integers as parameter.  
The function then calculates the factorial of each of the number in the list and prints it out. The list can only contain numbers between 1-9. No  need to check this in your code.
The function prototype should be: 
def list_factorial(list):
    # your code her
Hint: Don't forget the import statement from your answer. 
Test	Result
from collections import deque
list = deque()
list.append(5)
list.append(3)
list.append(7)
list_factorial(list)	120
6
5040
from collections import deque
list = deque()
list.append(1)
list_factorial(list)	1

Q2 Create a function copy_stack that takes two stacks as parameters, from_stack and to_stack that contain strings. The method then copies the contents of from_stack to to_stack, using some data structure as the temporal storage. Lastly, the function prints out the contents of both stacks for visual comparison. 
The function prototype should be: 
def copy_stack(from_stack, to_stack):
    # answer code here
Hint: Don't forget to add any imports if, needed. Please do not use straightforward copy-operations as we are practising programming here..


For example:
Test	Result
from_stack = []
from_stack.append('fourth');
from_stack.append('third');
from_stack.append('second');
from_stack.append('first');
to_stack = []
copy_stack(from_stack, to_stack)	['fourth', 'third', 'second', 'first']
['fourth', 'third', 'second', 'first']
from_stack = []
from_stack.append('cat');
to_stack = []
copy_stack(from_stack, to_stack)	['cat']
['cat']

Q3 Write function long_factorial, which takes a sorted list of long integers as parameter. 
Modify your existing function list_factorial code so that it does not recalculate each factorial starting from 1, but from the previous result, sort of incrementally. 
For example: When sorted queue is [7,15,19], first calculate the factorial of 7 and store it as intermediate result, then calculate the factorial of 15 starting from the intermediate result 7. Lastly, calculate the factorial of 19 starting from the factorial of 15.  
The function prototype should be:
def long_factorial(sorted_list):
# your answer code here


For example:
Test	Result
sorted_list = [ 1, 6, 13, 17, 19 ]
long_factorial(sorted_list)	1
720
6227020800
355687428096000
121645100408832000
sorted_list = [ 1 ]
long_factorial(sorted_list)	1

Q3 Lets write a parser for common operations presented in Reverse Polish Notation (RPN). The best data structure for such parser is the stack, right? See the link..
In RPN, the operator follows the two operands (always only two operands). For example, statement (2+3)*5 is presented as 23+5* in RPN and ((6*7)+2)*5 as 67*2+5*. 
Now, 23+ -> 2+3 = 5 and when we replace the operation with its result, we get for the next iteration 55* -> 5*5 = 25, which is the final result as our RPN string contains no more operands and operators. 
The function prototype is shown below, where it takes a RPN string as its input and prints out the final result:
def rpn(rpn_string):
    # your answer here
Hint. Lets use only single digit numbers (1-9) in our RPN input strings.
Hint. Here only addition, subtraction and multiplication are needed. 
For example:
Test	Result
rpn_string = '32+5*'
rpn(rpn_string)	25

rpn_string = '56-3*5+'
rpn(rpn_string)	2


Chapter 1:
All right, this exercise might be a bit harder. Lets write a recursive function that finds out the maximum value in a linked list of integers and prints it out. 
Again, we need to think of the three laws of recursion:
1. Define a base case: Well.. again our list needs to have items?
2. Move towards the base case: So.. when we added integers, we recursively went through the list until we reached the final item and then added the value to the value of the previous item. Maybe here we need to do the same, except that we compare last item with the previous one and return the maximum value? For comparison, see the hint below.
3. Must call itself: Maybe I should call myself again?
The function prototype is shown below:
def recursive_max(list):
    # your code here
Hint. Use built-in python function max()-method to compare two integers.

from collections import deque
list = deque()
list.append(1)
list.append(8)
list.append(11)
list.append(4)
print(recursive_max(list))	11
from collections import deque
list = deque()
list.append(1)
print(recursive_max(list))	


Lets write a function that reverses the elements in a linked list of integers. 
As described in the lecture material, you need to follow the three laws of recursion to write a recursive function:
1. Define a base case: I guess it is needed that our list needs to have at least one item?
2. Move towards the base case: Maybe remove an item from the list, after its added to the reversed list?
3. Must call itself: Maybe I should call myself with the updated list and reverselist?
The function prototype is shown below:
def recursive_reverse(list, reverse_list):
    # your code here
from collections import deque
list = deque()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
reverse_list = deque()
print(list)
recursive_reverse(list,reverse_list)
print(reverse_list)	deque([1, 2, 3, 4])
deque([4, 3, 2, 1])
from collections import deque
list = deque()
list.append(1)
reverse_list = deque()
print(list)
recursive_reverse(list,reverse_list)
print(reverse_list)	



