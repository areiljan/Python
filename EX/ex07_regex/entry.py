"""Entry."""
import re


def parse(row: str) -> tuple:
    """
    Parse string row into a tuple.

    The row has a first name, last name, ID code, phone number, date of birth and address.
    Only ID code is mandatory, other values may not be included.

    They can be found by the following rules:
    - Both the first name and last name begin with a capital letter and are followed by a lowercase letter
    - ID code is an 11-digit number
    - Phone number has the same rules applied as in the previous task
    - Date of birth is in the form of dd-MM-YYYY
    - Address is everything else that's left

    :param row: given string to find values from
    :return: tuple of values found in given string
    """
    first_name_pattern = r'([A-Z][a-z]+)'
    first_name_match = re.match(first_name_pattern, row)
    if first_name_match:
        first_name = first_name_match.group(1)
        row = row.replace(first_name_match.group(0), '').strip()
    else:
        first_name = None


    family_name_match = re.match(first_name_pattern, row)
    if family_name_match:
        family_name = family_name_match.group(1)
        row = row.replace(family_name_match.group(0), '').strip()
    else:
        family_name = None

    id_pattern = r'(\d{11})'
    id_match = re.match(id_pattern, row)
    if id_match:
        id_number = id_match.group(1)
        row = row.replace(id_match.group(0), '').strip()
    else:
        id_number = None

    phone_pattern = r'((\+\d{3} ?)?\d{8})'
    phone_match = re.match(phone_pattern, row)
    if phone_match:
        phone = phone_match.group(1)
        row = row.replace(phone_match.group(0), '').strip()
    else:
        phone = None

    dob_pattern = r'(\d{2}[ -]?\d{2}[ -]?\d{4})'
    dob_match = re.match(dob_pattern, row)
    if dob_match:
        dob = dob_match.group(1)
        row = row.replace(dob_match.group(0), '').strip()
    else:
        dob = None

    address_pattern = r'(.*)'
    address_match = re.match(address_pattern, row)
    if address_match:
        address = address_match.group(1)
        row = row.replace(address_match.group(0), '').strip()
    else:
        address = None
    if address == '':
        address = None

    return (first_name, family_name, id_number, phone, dob, address)


if __name__ == '__main__':
    print(parse('PriitPann39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('39712047623+372 5688736402-12-1998Oja 18-2,Pärnumaa,Are'))
    # (None, None, '39712047623', '+372 56887364', '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('PriitPann3971204762302-12-1998Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', None, '02-12-1998', 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('PriitPann39712047623+372 56887364Oja 18-2,Pärnumaa,Are'))
    # ('Priit', 'Pann', '39712047623', '+372 56887364', None, 'Oja 18-2,Pärnumaa,Are')
    print()
    print(parse('39712047623'))
    # (None, None, '39712047623', None, None, None)
