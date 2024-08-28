# Medelvärde

def main():
    # Skriv din lösning här nedan. Byt ut "pass" mot din kod.
    values = [float(value)
              for value in input().replace(" ", "").split(",")]
    mean_val = 0
    x = 0
    for value in values:
        mean_val += value
        x += 1
    print(mean_val/x)


if __name__ == "__main__":
    main()
