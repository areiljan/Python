def longest_substring(text: str) -> str:
    """
    Find the longest substring.

    #6

    Substring may not contain any character twice.
    CAPS and lower case chars are the same (a == A)
    In output, the case (whether lower- or uppercase) should remain.
    If multiple substrings have same length, choose first one.

    aaa -> a
    abc -> abc
    abccba -> abc
    babcdEFghij -> abcdEFghij
    abBcd => Bcd
    '' -> ''
    """
    longest = ""
    for j in range(len(text)):
        substring = ""
        for i in range(len(text[j:])):
            count_of_character = substring.lower().count(text[i].lower())
            if count_of_character < 1:
                substring += text[i]
                if len(substring) > len(longest):
                    longest = substring
            else:
                if len(substring) > len(longest):
                    longest = substring
                substring = ''
                if text[i - 1].lower() not in text[i:].lower():
                    substring = text[i - 1]
                substring += text[i]
    return longest

print(longest_substring('fgqwertyuiopa')) #wertyuiopa' == 'fgqwertyuiop
print(longest_substring('abc')) #abc
print(longest_substring('abccba')) #abc
print(longest_substring('babcdEFghij')) #abcdEFghij
print(longest_substring('abBcd')) #Bcd
print(longest_substring('')) #''