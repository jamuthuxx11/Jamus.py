#tuples
my_tuple = ("jamu,","jude","jose")
print(my_tuple)
#properties of turples
"""
1.turples are immutable ie.they cant be changed directly 
2.elemets in a tuple are indexed
3.tuples are usually in round brackets 
4.tuples are allow duplicates
5.tuples can have elements of different data types

"""
print(my_tuple[1])
my_tuple[1] ="jamu"   #this will give an error because we cannot change tuples directly
print(my_tuple[1])

#to modify/add/delete turples
"""
1.convert the tuple to a list
    mylist=list(the tuple name)
2.modify the value ypou wanted the same way we did in lists
    example on modification:
            student [0]="jamu"
    example on deleting:
            student.remove [0]="jude"
    example on adding:
            student.add=("jamu")
"""