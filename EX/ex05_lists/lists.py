"""Phone inventory."""


def list_of_phones(all_phones: str) -> list:
    """
    Return list of phones.

    The input string contains of phone brands and models, separated by comma.
    Both the brand and the model do not contain spaces (both are one word).

    "Google Pixel,Honor Magic5,Google Pixel" => ["Google Pixel', 'Honor Magic5', 'Google Pixel"]
    """
    if all_phones == "":
        phones_list = list("")
    else:
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
        if len(brand) > 1:
            if brand[0] not in brands_list:
                brands_list.append(brand[0])
        else:
            brands_list.append(brand)
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
        model = element.split(" ", 1)
        if len(model) > 1:
            if model[1] not in models_list:
                models_list.append(model[1])
        else:
            if model[0] not in models_list:
                models_list.append(model[0])
    return models_list


def search_by_brand(all_phones: str, keyword_brand:str) ->list:
    '''
    Parameetrid: telefonide nimekiri sõnena (nagu eelmises osas),
    otsitav tootja sõnena. Funktsioon tagastab listi telefonidest (tootja ja mudel).
    Telefonide nimekiri sõnena on täpselt samas vormingus nagu eelmistes osades.
    Funktsioon otsib tõstutundetult (case insensitive) täpseid vasteid.
    Kui sisend on "IPhone 14,iphone 7,IPHONE 11 Pro" ning otsitakse "IPhone" või "IPHONE",
    siis tulemus on: ['IPhone 14', 'iphone 7', 'IPHONE 11 Pro'].
    Tulemuses on telefonid originaalkujul.
    :param keyword_brand:
    :return:
    '''
    phones_list = list_of_phones(all_phones)
    matching_phones_list = []
    for phone in phones_list:
        if keyword_brand.lower() == phone.lower().split()[0]:
            matching_phones_list.append(phone)
    return matching_phones_list


def search_by_model(all_phones: str, keyword_model:str) ->list:
    '''
    Lisa funktsioon search_by_model.
    Parameetrid: telefonide nimekiri sõnena (nagu eelmises osas),
    otsitav mudel sõnena. Funktsioon tagastab listi telefonidest (tootja ja mudel).
    Otsing on tõstutundetu ning otsib täpset vastet mudelite sõnade seast.
    Kui sisend on "IPhone X,IPhone 12 Pro,IPhone 14 pro Max" ja otsitakse "Pro" või "pro",
    on tulemus ["IPhone 12 Pro", "IPhone 14 pro Max"]. "1" ei vasta täpselt otsingule.
    Kui otsida "Ma", siis ei tule ühtegi vastet (funktsioon tagastab tühja järjendi).
    Kuna mudel võib koosneda mitmest sõnast, siis tuleb igast sõnast otsida.

    Kui sisend on "IPhone X,IPhone 12 Pro,IPhone 14 pro Max" ja mudeli otsinguga
    otsitakse "12 Pro" (mitu sõna) või "1" (osaline sõna) või "IPhone" (tootja),
    siis ühtegi tulemust ei leita. Ehk siis tuleb leida sellised telefonid,
    kus otsitav sõne võrdub täpselt ühe mudeli sõnaga.
    Mudeli otsingut võib tõlgendada ka nii: Kas telefoni mudelite sõnades leidub
    täpselt selline otsitav sõna (case-insensitive).
    '''
    phones_list = list_of_phones(all_phones)
    model_list = []
    matching_phones_list = []
    for phone in phones_list:
        model_list = phone.split(" ")
        model_list.pop(0)
        for element in model_list:
            if keyword_model.lower() == element.lower():
                matching_phones_list.append(phone)
    return matching_phones_list

print(list_of_phones('Google Pixel,Honor Magic5,Google Pixel2,IPhone 12,IPhone XS,IPhone 11'))
print(phone_brands('Google Pixel,Honor Magic5,Google Pixel2,IPhone 12,IPhone XS,IPhone 11'))
print(phone_models('Google Pro Pixel2,Honor Magic5,Google Pixel2,IPhone 12,IPhone XS,IPhone 11'))
print(list_of_phones(""))
print(phone_models('one,one,one,one'))
print(search_by_model('Google Pro Pixel2,Honor Magic5,Google Pixel2,IPhone 12,IPhone XS,IPhone 11','Pixel2'))