def NhapHeSo():
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    return a, b

def GiaiPTBac1(a, b):
    if(a == 0):
        if(b == 0):
            print("Vô số nghiệm!")
        else:
            print("Vô nghiệm!")
    else:
        print("Phương trình có nghiệm x =", -b/a)

def main():
    a, b = NhapHeSo()
    GiaiPTBac1(a, b)

if __name__== "__main__":
    main()