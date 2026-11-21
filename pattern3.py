# for i in range(5,0,-1): #for i in range 5
#     for j in range(i): #column
#         print("*", end=" ")
#     print()

for i in range (5): #outer loop 
    for j in range(5-i): # inner loop reduce by i
        print("*",end="") # go to next line
    print() # just print reduced value