"""EX02 Poem."""

"""
Ask for user's inputs and print out a poem in one line using f string and newline (\n)

Example input:
color = "red"
objects = "violets"
activity = "code"

Example output:
Roses are red,
violets are blue,
I love to code
And so will you!
"""
color = input("Sisesta värv: ")
objects = input("Sisesta objekt: ")
activity = input("Sisesta tegusõna: ")
print(f'''Roses are {color},
{objects} are blue,
I love to {activity}
And so will you!''')
