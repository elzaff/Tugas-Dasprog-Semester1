M,N,T = map(int,input().split())

red = int(20)
yellow = int(5)
green =int(60)
total = red + yellow + green

passed_green = green // 5
cars_passed = (T//total)*(passed_green)
time_left = T // cars_passed

if time_left > red + yellow:
    cars_passed += (time_left - red - yellow) // 5
    
cars_total = M + N + 1
cars_left = cars_total - cars_passed

if cars_passed <= 0:
    print('YES! 0')
elif cars_passed > M:
    print('YES!'+ str(cars_left))
else:
    print('NO!' + str(cars_left))