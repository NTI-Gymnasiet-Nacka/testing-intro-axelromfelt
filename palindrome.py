# Palindrome

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    user_input = input().lower()
    text_reversed = user_input[::-1]
    if user_input == text_reversed:
        print(True)
    else:
        print(False)


if __name__ == "__main__":
    main()
