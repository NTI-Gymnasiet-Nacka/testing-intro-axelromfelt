# Största skillnad

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    numbers = [int(number)
               for number in input().replace(" ", "").split(",")]
    numbers.sort()
    print(abs(numbers[-1]-numbers[0]))


if __name__ == "__main__":
    main()
