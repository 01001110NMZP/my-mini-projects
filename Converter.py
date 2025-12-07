def remainder_finder(user_num: int):
    """converts base-10 to base-16 remainders"""
    remainders: list[int] = []

    while True:

        if user_num >= 16:

            num_remainder: int = user_num % 16
            remainders.append(num_remainder)

            user_num = user_num // 16

        else:
            remainders.append(user_num)
            break

    return remainders


def converter(remainders: list[int]):
    """Converts the remainders to actual hex"""

    letters: str = "abcdef"

    hex_display: str = "0x"

    reversed_remainders = remainders[::-1]

    for remainder in reversed_remainders:

        if remainder > 9:

            remainder = remainder - 10

            # given remainder == 10
            # 10 - 10 = 0
            # letters[0] = "a"
            # "a" -> hex_display
            hex_display += letters[remainder]

        else:

            hex_display += str(remainder)


    return hex_display


if __name__ == '__main__':
    while True:
        try:
            num = input("Input a base 10 to convert to hexadecimal (base 16) or e to exit: ")

            if num == "e":
                break
            else:
                num = int(num)
                print(converter(remainder_finder(num)))
                print(hex(num))  # just to check with the built-in hex func

        except ValueError as ve:
            print("Please only enter an integer")