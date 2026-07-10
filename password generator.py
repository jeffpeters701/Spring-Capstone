import itertools

def generate_passwords(length, filename):
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    with open(filename, 'w') as file:
        for password in itertools.product(characters, repeat=length):
            password_str = ''.join(password)
            file.write(password_str + '\n')
            print(password_str)  # Print the current combination

def main():
    password_length = 8
    filename = 'passAttempt.txt'
    generate_passwords(password_length, filename)
    print(f"Successfully generated passwords and saved them to {filename}")

if __name__ == "__main__":
    main()
