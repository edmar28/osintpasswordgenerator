# Password Generator for OSINT

Overview

This Python script generates a list of possible passwords based on a person's personal information. It collects inputs such as the person's name, birthdate, favorite food, and other details. The script then generates various combinations of these details and saves them into a file named output.txt. This can be useful in OSINT (Open Source Intelligence) activities, where you may need to generate potential passwords for further analysis.

## Features

- Collects personal information like first name, birthdate, favorite food, etc.
- Generates combinations of 2, 3, or 4 details to form possible passwords.
- Saves generated passwords to a text file (output.txt).
- Offers different case formats for password generation (lowercase, uppercase, capitalized).

## Requirements

- Python 3.x

## Installation

1. Clone the repository from GitHub:

```bash
  git clone https://github.com/edmar28/osintpasswordgenerator.git
```

2. Navigate to the project directory:
```bash
 cd osintpasswordgenerator
```

## Usage

1. Run the script:

Use the following command to run the script:

Example domains.txt:
```bash
python igp.py
```

2. Input Details:

When prompted, input the necessary personal details, such as:

- First Name
- Last Name
- Favorite Food
- Birthdate (Month, Day, Year)
- Pet’s Name (optional)
- Boyfriend or Husband (if any)
- Girlfriend or Wife (if any)

Example
```bash
First Name: John
Last Name: Doe
Favorite Food: Pizza
Birth Month (in digits): 12
Birth Day: 25
Birth Year: 1990
Pets Name (if any): Rover
Boyfriend or Husband (If any): 
Girlfriend or Wife (if any): Jane
Favorite Color: Blue
```


3. Password Generation:

The script will generate a list of possible password combinations using the entered details and store them in a file named output.txt.

4. Check Output:

After the script completes, open the output.txt file in the same directory to see the generated passwords.
```bash
cat output.txt
```
