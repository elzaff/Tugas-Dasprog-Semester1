Uhp = int(input())
K = int(input())
M = int(input())

ApM = M // 2  * 2
HpM = M * 100
SerangM = 100/100
ApK = K // 2 * 5
HpK = K * 500
SerangK = 500/100
ApR = 100
HpR = 1000 
SerangR = 1000/100

if Uhp > ApM:
    Uhp -= ApM * SerangM
    if Uhp > ApK:
        Uhp -= ApK * SerangK
        if Uhp > ApR:
            Uhp -= ApR * SerangR
            if Uhp > 0:
                print(f"Yey! Ucup Menang! HP tersisa: {round(Uhp)}")
            else:
                print('Yah! Ucup Meninggoy.')
        else:
            print('Yah! Ucup Meninggoy.')
    else:
        print('Yah! Ucup Meninggoy.')
else:
    print('Yah! Ucup Meninggoy.')