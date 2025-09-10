def subtract_two_sets(list1,list2):
    return [x for x in list1 if x not in list2]
from myfunc2 import subtract_two_sets

def main():
    try:
        list1 = list(map(int, input("ใส่ตัวเลขชุดแรก (เว้นด้วย space): ").split()))
        list2 = list(map(int, input("ใส่ตัวเลขชุดที่สอง (เว้นด้วย space): ").split()))

        result = subtract_two_sets(list1, list2)
        print(f"\nผลลัพธ์หลังลบเลขชุดสอง: {result}")

    except ValueError:
        print("กรุณากรอกตัวเลขให้ถูกต้อง!")
if __name__ == "__main__":
    main()