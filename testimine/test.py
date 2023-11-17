food = {"apple": 2, "pizza": 4, "cucumber": 1}
food = ["cucumber"]

cats = {"Saf", "Sofi"}
cats.add("Nala")
cats.update(["Mochi", "Peanut"])
cats.add("Saf")
print(cats)

def remove_incorrect_names(names: set[str]):
    """Remove all names from a given set that contain number in it."""
    for name in names:
        for letter in name:
            if letter.isnumeric():
                names.remove(name)
    return names

print(remove_incorrect_names({"Albert", "Tom", "245"}))

