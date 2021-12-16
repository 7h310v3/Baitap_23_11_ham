import Bai4
import math

def NhapHeSo():
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    return a, b, c

def GiaiPTBac2(a, b, c):
    if (a == 0):
        Bai4.GiaiPTBac1(b, c)
    else:
        delta = b * b - 4 * a * c
        if (delta > 0):
            x1 = (float)((-b + math.sqrt(delta)) / (2 * a))
            x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
            print("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
        elif (delta == 0):
            x1 = (-b / (2 * a))
            print("Phương trình có nghiệm kép: x1 = x2 = ", x1)
        else:
            print("Phương trình vô nghiệm!")

def main():
    a, b, c = NhapHeSo()
    GiaiPTBac2(a, b, c)

if __name__== "__main__":
    main()