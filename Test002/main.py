from myfunc import add
def main():
    try:
        A = float(input("A = "))
        B = float(input("B = "))
        result = add(A,B)
        print(f"\nผลลัพธ์ของ A + B คือ : {result}")
    except ValueError:
        print("กรุณากรอกตัวเลขให้ถูกต้อง!")
if __name__ == "__main__":
    main()