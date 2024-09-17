import itertools

def generate_passwords(first_name, last_name, favorite_food, birth_month, birth_day, birth_year, pets_name, spouse_name, partner_name, favorite_color):
    # List to store all possible password combinations
    password_combinations = []

    # Combinations using first name, last name, favorite food, birth date, pets, spouse, partner, favorite color
    base_info = [
        first_name, last_name, favorite_food, favorite_color, pets_name, spouse_name, partner_name,
        f"{birth_day}{birth_month}{birth_year}",  # Birthdate formats
        f"{birth_year}{birth_month}{birth_day}",
        f"{birth_month}{birth_day}{birth_year}",
        f"{birth_day}{birth_month}",
        f"{birth_month}{birth_year}"
    ]

    # Filter out any empty fields (like if no pets or partner is entered)
    base_info = [item for item in base_info if item]

    # Generate combinations of 2, 3, and 4 elements
    for n in range(2, 5):
        for combo in itertools.permutations(base_info, n):
            password_combinations.append(''.join(combo))
            password_combinations.append(''.join(combo).capitalize())
            password_combinations.append(''.join(combo).lower())
            password_combinations.append(''.join(combo).upper())

    return password_combinations

def main():
    # Input details
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    favorite_food = input("Favorite Food: ").strip()
    birth_month = input("Birth Month (in digits): ").strip()
    birth_day = input("Birth Day: ").strip()
    birth_year = input("Birth Year: ").strip()
    pets_name = input("Pets Name (if any): ").strip()
    spouse_name = input("Boyfriend or Husband (If any): ").strip()
    partner_name = input("Girlfriend or Wife (if any): ").strip()
    favorite_color = input("Favorite Color: ").strip()

    # Generate passwords
    passwords = generate_passwords(first_name, last_name, favorite_food, birth_month, birth_day, birth_year, pets_name, spouse_name, partner_name, favorite_color)

    # Save the generated passwords to output.txt
    with open("output.txt", "w") as f:
        f.write("\n".join(passwords))

    print(f"\nPasswords have been saved to output.txt")

if __name__ == "__main__":
    main()
