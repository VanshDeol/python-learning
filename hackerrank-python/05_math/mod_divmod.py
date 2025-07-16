integer_1 = int(input())
integer_2 = int(input())
divmod_op = divmod(integer_1 , integer_2) #returns tuple
integer_division , remainder = divmod_op  #unpacks tuple
print(integer_division)
print(remainder)
print(divmod_op)
