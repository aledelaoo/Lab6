# Alessandro De-La-O

def main():
    print('Menu')
    print('-----------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    user_input = input("Enter an 8-digit password in string format: ")


    encoded_password = encode_password(user_input)
    print(f"Encoded password: {encoded_password}")

    decoded_password = decode_password(encoded_password)
    print(f"Decoded password: {decoded_password}")
def encode_password(password):
    if not password.isdigit() or len(password) != 8:
        return "Invalid password format"

    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit

    return encoded_password


if __name__ == '__main__':
    main()
