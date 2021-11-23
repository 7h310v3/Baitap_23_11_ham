import Bai2

def NhapN():
    n = int(input("Nhập N: "))
    while(n < 1):
        print("Nhập sai, xin nhập lại!")
        n = int(input("Nhập N: "))
    return n

def NhapThongDiep():
    global stg
    stg = input("Nhập thông điệp muốn in ra: ")

def main():
    n = NhapN()
    NhapThongDiep()

    count = 0
    print("Thông điệp muốn in ra là: ")
    while(count < n):
        Bai2.In(stg)
        count += 1

if __name__== "__main__":
    main()