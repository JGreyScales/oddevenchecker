file = open('oddevenchecker.py', 'w')

file.write("x = input(' pick a number ')\n")
file.write('if x == 0:\n')
file.write('    print("idk")\n')

for x in range(1, (10**5) + 1):
    if x % 2 == 0:
        file.write(f"if x == '{x}':\n")
        file.write("    print('even')\n")
    else:
        file.write(f"if x == '{x}':\n")
        file.write("    print('odd')\n")

file.close()