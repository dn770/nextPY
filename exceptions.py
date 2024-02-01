import functools
import ctypes
import string


def dup(ch):
    return ch * 2


def double_letter(my_str):
    return ("".join(list(map(dup, my_str))))


# print(double_letter("python"))

def divisor(num):
    return num % 4 == 0


def four_dividers(number):
    return list(filter(divisor, range(number)))


# print(four_dividers(6))

def plus(dig1, dig2):
    return int(dig1) + int(dig2)


def sum_of_digits(number):
    return functools.reduce(plus, str(number))


# print(sum_of_digits(45000120))

def combine_coins(symbol, num):
    return ("".join([symbol + str(x) + " " for x in num]))


print(combine_coins('$', range(5)))


def read_file(file_name):
    str = "_content start_\n"
    try:
        f = open(file_name)
    except:
        str += "__NO_SUCH_FILE__\n"
    else:
        str += "This is the content from the file!\n"
    finally:
        str += "_content end_\n"
        return str


# print(read_file("file_does_not_exist.txt"))


class UnderAgeError(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Your age is ", self._arg, ". in", str(
            18 - self._arg), "years you will be able to come to Ido's birthday"


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAgeError(age)
    except:
        print("Your age is ", age, ". in", str(18 - age), "years you will be able to come to Ido's birthday")
    else:
        print("You should send an invite to " + name)


# send_invitation("koby", 15)
# send_invitation("boby", 22)

def UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The username contains an illegal character"


def UsernameTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Too short username . this username contaning", self._arg, "characters.\n The minimum length is 3."


def UsernameTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Too long username . this username contaning", self._arg, "characters.\n The maximum length is 16."


def PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "The password is missing a character."


def PasswordMissingUpper(PasswordMissingCharacter):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super(__str__(self)) + "missing upper letter"


def PasswordMissingLower(PasswordMissingCharacter):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super(__str__(self)) + "missing lower letter"


def PasswordMissingDigit(PasswordMissingCharacter):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super(__str__(self)) + "missing digit"


def PasswordMissingPunct(PasswordMissingCharacter):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super(__str__(self)) + "missing punct chracter"


def PasswordTooShort(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Too short username . this username contaning", self._arg, "characters.\n The minimum length is 8."


def PasswordTooLong(Exception):
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return "Too long username . this username contaning", self._arg, "characters.\n The maximum length is 40."


def check_input(username, password):
    try:
        for ch in username:
            if not ch.isdigit() and not ch.isalpha() and ch != "_":
                UsernameContainsIllegalCharacter()
    except:
        print("The username contains an illegal character \"", ch, "\" at index ", username.find(ch))

    try:
        if len(username) < 3:
            raise UsernameTooShort()
    except:
        print("The username length ", len(username), " is too short")

    try:
        if len(username) > 16:
            raise UsernameTooLong()
    except:
        print("The username length ", len(username), " is too long")
    try:
        if not any(ch.isupper() for ch in password):
            raise PasswordMissingUpper()
    except:
        print("password missing upcase char")
    try:
        if not any(ch.islower() for ch in password):
            raise PasswordMissingLower()
    except:
        print("password missing lower char")
    try:
        if not any(ch.isdigit() for ch in password):
            raise PasswordMissingDigit()
    except:
        print("password missing digit")
    try:
        if not any(ch in string.punctuation for ch in password ):
            raise PasswordMissingPunct()
    except:
        print("password missing punct char")

    try:
        if len(password) < 8:
            raise PasswordTooShort()
    except:
        print("The password length ", len(username), " is too short")

    try:
        if len(password) > 40:
            raise PasswordTooLong()
    except:
        print("The username length ", len(username), " is too long")


def main():
    print("Please insert user-name and password:")
    username = input("name:")
    password = input("paasword:")

    while True:
        try:
            check_input(username, password)
            print("ok")
            return
        except:
            print("Please insert user-name and password:")
            username = input("name:")
            password = input("paasword:")


main()
