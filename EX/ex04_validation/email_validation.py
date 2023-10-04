"""Email validation."""


def has_at_symbol(email):
    'kontrollib kas emailis on at sümbol'
    if "@" in email:
        return True
    else:
        return False


def is_valid_username(email):
    'kontrollib kas email vastab nõutele'
    at_count = 0
    for a in email:
        if "@" in email:
            at_count += 1
    name_list = email.rsplit("@", 1)
    for a in name_list[0]:
        if a == "." or a.isnumeric() or a.isalpha():
            continue
        else:
            return False
            break
    return True


def find_domain(email):
    'leiab domeeni'
    name_list = email.rsplit("@", 1)
    return(name_list[1])


def is_valid_domain(email):
    'kontrollib kas leitud domeen vastab nõuetele'
    name_list = email.rsplit("@", 1)
    name_list_dots = name_list[1].split(".")
    for a in name_list_dots:
        if a.isalpha():
            continue
        else:
            return False
            break

    if len(name_list_dots) >= 2:
        return False

    if 3 < len(name_list_dots[0]) or len(name_list_dots[0]) > 10 or len(name_list_dots[1]) < 2 or len(name_list_dots[1]) > 5:
        return False

    return True


def is_valid_email_address(email):
    'kontrollib kas emaili aadress vastab nõuetele'
    return has_at_symbol(email) and is_valid_username(email) and find_domain(email) and is_valid_domain(email)


def create_email_address(username, domain_name):
    'loob korrektse meiliaadressi'
    print("money")


if __name__ == '__main__':
    print("Email has the @ symbol:")
    print(has_at_symbol("joonas.kivi@gmail.com"))  # -> True
    print(has_at_symbol("joonas.kivigmail.com"))  # -> False

    print("\nUsername has no special symbols:")
    print(is_valid_username("martalumi@taltech.ee"))  # -> True
    print(is_valid_username("marta.lumi@taltech.ee"))  # -> True
    print(is_valid_username("marta lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta&lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta@lumi@taltech.ee"))  # -> False

    print("\nFind the email domain name:")
    print(find_domain("karla.karu@saku.ee"))  # -> saku.ee
    print(find_domain("karla.karu@taltech.ee"))  # -> taltech.ee
    print(find_domain("karla.karu@yahoo.com"))  # -> yahoo.com
    print(find_domain("karla@karu@yahoo.com"))  # -> yahoo.com

    print("\nCheck if the domain is correct:")
    print(is_valid_domain("pihkva.pihvid@ttu.ee"))  # -> True
    print(is_valid_domain("metsatoll@&gmail.com"))  # -> False
    print(is_valid_domain("ewewewew@i.u.i.u.ewww"))  # -> False
    print(is_valid_domain("pannkook@m.oos"))  # -> False

    print("\nIs the email valid:")
    print(is_valid_email_address("DARJA.darja@gmail.com"))  # -> True
    print(is_valid_email_address("DARJA=darjamail.com"))  # -> False

    print("\nCreate your own email address:")
    print(create_email_address("hot.ee", "vana.ema"))  # -> vana.ema@hot.ee
    print(create_email_address("jaani.org", "lennakuurma"))  # -> lennakuurma@jaani.org
    print(create_email_address("koobas.com",
                               "karu&pojad"))  # -> Cannot create a valid email address using the given parameters!
