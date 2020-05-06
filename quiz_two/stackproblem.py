new_stack = []
  
def apppend_digits(number): 
    while (number != 0):  
        new_stack.append(number % 10)
        number = int(number / 10)

 
def reverse(number): 
    apppend_digits(number)
    reverse_number = 0
    i = 1
   
    while (len(new_stack) > 0):  
        reverse_number = reverse_number + (new_stack[len(new_stack) - 1] * i)
        new_stack.pop()
        i = i * 10; 
      
    return reverse_number
  
number = 12345
  
print(reverse(number))
