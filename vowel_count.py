# Vokalräkning

VOWELS = ("a", "i", "e", "o", "u", "y", "ö", "å", "ä")


def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    user_input = input().lower()
    number_of_vowels = 0
    for i in VOWELS:
        number_of_vowels += user_input.count(i)

    print(number_of_vowels)


if __name__ == "__main__":
    main()
