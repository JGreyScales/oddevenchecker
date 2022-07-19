file = open('oddevenchecker.py', 'w')

file.write("x = input(' pick a number ')\n")
file.write('if x == 0:\n')
file.write('    print("idk")\n')


for x in range(1, (10**5) + 1):
    y = 'odd'
    if x % 2 == 0:
        y = 'even'
    file.write(f"if x == '{x}':\n")
    file.write(f"    print('{y}')\n")

file.close()
