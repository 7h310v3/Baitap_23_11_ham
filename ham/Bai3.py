import Bai2

def NhapN():
    x = int(input("Nhập N: "))
    while(x < 1):
        print("Nhập sai, xin nhập lại!")
        x = int(input("Nhập N: "))
    return x

def NhapThongDiep():
    stg = input("Nhập thông điệp muốn in ra: ")
    return stg

def main():
    n = NhapN()
    stg = NhapThongDiep()

    count = 0
    print("Thông điệp muốn in ra là: ")
    while(count < n):
        Bai2.In(stg)
        count += 1

if __name__== "__main__":
    main()
