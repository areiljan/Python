"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    """
    phones_list = all_phones.split(",")
    return phones_list


def phone_brands(all_phones: str) -> list:
    """
    Return list of unique phone brands.

    The order of the elements should be the same as in the input string (first appearance).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google", "Honor"]
    """
    phones_list = list_of_phones(all_phones)
    brands_list = []
    for element in phones_list:
        brand = element.split(" ")
        if brand[0] not in brands_list:
            brands_list.append(brand[0])
    return brands_list


def phone_models(all_phones: str) -> list:
    """
    Return list of unique phone models.

    The order of the elements should be the same as in the input string (first appearance).

    "Honor Magic5,Google Pixel,Honor Magic4" => ['Magic5', 'Pixel', 'Magic4']
    """
    phones_list = list_of_phones(all_phones)
    models_list = []
    for element in phones_list:
        model = element.split(" ")
        if element not in models_list:
            models_list.append(model[1])
    return models_list

print(list_of_phones('Google Pixel,Honor Magic5,Google Pixel2,IPhone 12,IPhone XS,IPhone 11'))
print(phone_brands('Google Pixel,Honor Magic5,Google Pixel2,IPhone 12,IPhone XS,IPhone 11'))
print(phone_models('Google Pixel,Honor Magic5,Google Pixel2,IPhone 12,IPhone XS,IPhone 11'))
