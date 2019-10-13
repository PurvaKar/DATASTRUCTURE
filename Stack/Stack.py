# -*- coding: utf-8 -*-
"""
@author: anishukla
"""

stack = []

while(True):
    print("\nChoose 1.Push a value in a stack.")
    print("2.Pop a value from stack.")
    print("3.Search an element in a stack.")
    print("4.View stack.")
    print("5.View stack and exit.")
    
    K = int(input("Choose an option between 1 to 5: "))
    if K==1:
        val = int(input("Enter value to be pushed: "))
        stack.append(val)
        
    elif K==2:
        if len(stack)==0:
            print("Nothing to pop. First add some elements!\n")
        else:
            stack.pop()
        
    elif K==3:
        val = 0
        L = []
        search = int(input("Enter the value of element you want to search: "))
        for i in range(len(stack)):
            if stack[i] == search:
                if val==0:
                    val = val+1 
                    print("The element searched is present at positions:")
                L.append(i+1)
        print(*L)
        if val == 0:
            print("Element you searched isn't present in the following stack.")
            
    elif K==4:
        print(*stack)
    
    elif K==5: 
        print(*stack)
        break
        
    else:
        print("Wrong input! Choose an input between 1 to 5.")
        