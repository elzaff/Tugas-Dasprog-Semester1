userinput1, userinput2 = input("Enter Two Inputs, separate it by a space, 'T' for true or 'F' for false: ").strip().upper().split()

if userinput1 == 'T':
    fun1 = 1
elif userinput1 == 'F':
    fun1 = 0
else:
    print("Input salah, ulang!")
    exit()

if userinput2 == 'T':
    fun2 = 1
elif userinput2 == 'F':
    fun2 = 0
else:    
    print("Input salah, ulang!")
    exit()

print("Testing &&")
if fun1 and fun2:
    print("fun2 executed")
    print("Test of && complete")

print("Testing ||")
if fun1 or fun2:
    print("fun2 executed")
    print("Test of || complete")