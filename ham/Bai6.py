import Bai4
import Bai5

def NhapX():
    x = int(input("Nhập x(1 or 2): "))
    while(x != 1 and x != 2):
        x = int(input("Nhập x(1 or 2): "))
    return x

def choicex(x):
    if(x == 1):
        a, b = Bai4.NhapHeSo()
        Bai4.GiaiPTBac1(a, b)
    else:
        a, b, c = Bai5.NhapHeSo()
        Bai5.GiaiPTBac2(a, b, c)

def main():
    x = NhapX()
    choicex(x)

if __name__== "__main__":
    main()

