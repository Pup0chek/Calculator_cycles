from operations import add, subtract, multiply, divide, remainder, sin, cos, power, square_root, floor, ceil
from memory import memory_add, memory_clear, memory_recall

def main():
    print("Welcome to the Calculator!")

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Remainder")
        print("6. Sin")
        print("7. Cos")
        print("8. Power")
        print("9. Square Root")
        print("10. Floor")
        print("11. Ceil")
        print("12. Memory +")
        print("13. Memory Clear")
        print("14. Memory Recall")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "0":
            break

        if choice in {"1", "2", "3", "4", "5", "8", "9", "10", "11"}:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: ")) if choice not in {"6", "7", "9"} else None

        elif choice in {"6", "7", "9"}:
            num1 = float(input("Enter number: "))
            num2 = None

        elif choice == "12":
            num1 = float(input("Enter number to add to memory: "))
            memory_add(num1)
            print(f"Added {num1} to memory.")

        elif choice == "13":
            memory_clear()
            print("Memory cleared.")

        elif choice == "14":
            print(f"Memory recall: {memory_recall()}")
            continue

        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {divide(num1, num2)}")
        elif choice == "5":
            print(f"Result: {remainder(num1, num2)}")
        elif choice == "6":
            print(f"Result: {sin(num1)}")
        elif choice == "7":
            print(f"Result: {cos(num1)}")
        elif choice == "8":
            print(f"Result: {power(num1, num2)}")
        elif choice == "9":
            print(f"Result: {square_root(num1)}")
        elif choice == "10":
            print(f"Result: {floor(num1)}")
        elif choice == "11":
            print(f"Result: {ceil(num1)}")

if __name__ == "__main__":
    main()