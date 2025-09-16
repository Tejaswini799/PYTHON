a = ["SITA", "RAVI", "GEETHA", "TEJA"]
CGPA = [79, 66, 47, 88]
ARREAR = [0, 1, 2, 1]

for i in range(4):
    if ARREAR[i] == 0 and CGPA[i] > 60:
        print(a[i])
