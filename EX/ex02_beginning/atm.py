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
if amount / 100 > 1:
    banknotes += (amount // 100)
    amount -= ((amount // 100) * 100)
if amount / 50 > 1:
    banknotes += (amount // 50)
    amount -= ((amount // 50) * 50)
if amount / 20 > 1:
    banknotes += (amount // 20)
    amount -= ((amount // 20) * 20)
if amount / 10 > 1:
    banknotes += (amount // 10)
    amount -= ((amount // 10) * 10)
if amount / 5 > 1:
    banknotes += (amount // 5)
    amount -= ((amount // 5) * 5)
banknotes += amount

print(f"Amount of banknotes needed: {banknotes}")
