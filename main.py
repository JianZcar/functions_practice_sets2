import math


def int_input(prompt: str) -> int:
    # input an integer
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter an integer.")


def calculate_area_of_triangle(a: int, b: int, c: int) -> float:
    # Heron's formula
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def is_it_leap_year(year: int) -> bool:
    # determine if a year is a leap year
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


def main():
    # main function
    selection = ["Calculate area of triangle", "Is it a leap year?"]
    [print(f"{i + 1}. {selection[i]}") for i in range(len(selection))]
    choice = int_input("Please select an option: ")
    match choice:
        case 1:
            a = int_input("Please enter the length of side a: ")
            b = int_input("Please enter the length of side b: ")
            c = int_input("Please enter the length of side c: ")
            area = calculate_area_of_triangle(a, b, c)
            print(f"The area of the triangle is {area}.")
        case 2:
            year = int_input("Please enter a year: ")
            if is_it_leap_year(year):
                print(f"{year} is a leap year.")
    pass


if __name__ == "__main__":
    main()
