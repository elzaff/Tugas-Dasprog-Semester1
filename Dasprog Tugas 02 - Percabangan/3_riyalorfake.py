userinput = input("Enter 'T' for true or 'F' for false: ").strip().upper()
if userinput == 'T':
    fun1 = 1
elif userinput == 'F':
    fun1 = 0
else:
    print("Input salah, ulang!")
    exit()

fun2 = 1  

print("Testing &&")
if fun1 and fun2:
    print("fun2 executed")
    print("Test of && complete")

print("Testing ||")
if fun1 or fun2:
    print("fun2 executed")
    print("Test of || complete")
