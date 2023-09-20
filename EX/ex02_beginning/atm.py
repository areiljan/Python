"""
Create a machine that dispenses money using 1€, 5€, 10€, 20€, 50€ and 100€ banknotes.

Given the sum, one must print out how many banknotes does it take to cover the sum. Task is to cover the sum with as little
banknotes as possible.

Example
The sum is 72€
We use four banknotes to cover it. The banknotes are 20€, 50€, 1€ and 1€.
"""

amount = int(input("Enter a sum: "))
banknotes = 0
#
if amount % 100 > 0:
    sajalised = amount // 100
    amount -= sajalised * 100
    banknotes += sajalised
if amount % 50 > 0:
    viiekumnelised = amount // 50
    amount -= viiekumnelised * 50
    banknotes += viiekumnelised
if amount % 20 > 0:
    kahekumnelised = amount // 20
    amount -= kahekumnelised * 20
    banknotes += kahekumnelised
if amount % 10 > 0:
    kumnelised = amount // 10
    amount -= kumnelised * 10
    banknotes += kumnelised
if amount % 5 > 0:
    viielised = amount // 5
    amount -= viielised * 10
    banknotes += viielised
else:
    uhelised = amount
    banknotes += uhelised
#
print(f"Amount of banknotes needed: {banknotes}")