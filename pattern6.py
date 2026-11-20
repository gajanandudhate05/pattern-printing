# for i in range(1,6):
#     for j in range(6,1,):
#         print(i,end="")
for i in range(1, 6):
    for j in range(5 - i):
        print("  ", end="")
    for j in range(i):
        print("* ", end="")
    print()