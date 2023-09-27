"""Secret letter."""


def secret_letter(letter: str) -> bool:
    """
    Check if the given secret letter follows all the necessary rules. Return True if it does, else False.

    Rules:
    1. The letter has more uppercase letters than lowercase letters.
    2. The sum of digits in the letter has to be equal to or less than the amount of uppercase letters.
    3. The sum of digits in the letter has to be equal to or more than the amount of lowercase letters.

    :param letter: secret letter
    :return: validation
    """


    uppercaseletters = 0
    lowercaseletters = 0
    sumofdigits = 0

    for a in letter:
        if a.isupper():
            uppercaseletters += 1
        elif a.islower():
            lowercaseletters += 1
        else:
            sumofdigits += int(a)

    if uppercaseletters > lowercaseletters and sumofdigits <= uppercaseletters and sumofdigits >= lowercaseletters:
        return True
    else:
        return False



if __name__ == '__main__':
    print(secret_letter("sOMEteSTLETTer8"))  # True
    print(secret_letter("thisisNOTvaliD4"))  # False
    print(secret_letter("TOOMANYnumbers99"))  # False
    print(secret_letter("anotherVALIDLETTER17"))  # True
    print(secret_letter("CANBENOLOWERCASENODIGITS"))  # True