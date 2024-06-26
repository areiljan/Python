"""Music."""


class Note:
    """
    Note class.

    Every note has a name and a sharpness or alteration (supported values: "", "#", "b").
    """

    def __init__(self, note: str):
        """Initialize the class.

        To make the logic a bit easier it is recommended to normalize the notes, that is, choose a sharpness
        either '#' or 'b' and use it as the main, that means the notes will be either A, A#, B, B#, C etc or
        A Bb, B, Cb, C.
        Note is a single alphabetical letter which is always uppercase.
        NB! Ab == Z#
        """
        self.note = note

    def normalize(self):
        """Normalize the notes.

        Making an easily reusable function that normalizes the notes making every note into one character notes
        and only using '#' to avoid confusion.
        """
        note = self.note.upper()
        if len(note) == 1:
            return note

        if note[0] == "Z":
            next_char = "A"
        else:
            next_unicode_value = ord(note[0]) + 1  # Increment the Unicode value to get the next character
            next_char = chr(next_unicode_value)

        if note[1] == 'B':
            normalized_note = note[0] + "b"
        elif note[1] == '#':
            normalized_note = next_char + "b"

        return normalized_note

    def __repr__(self) -> str:
        """
        Representation of the Note class.

        Return: <Note: [note]> where [note] is the note_name + sharpness if the sharpness is given, that is not "".
        Repr should display the original note and sharpness, before normalization.
        """
        return f"<Note: {self.note[0].upper()}{self.note[1:]}>"

    def __eq__(self, other):
        """
        Compare two Notes.

        Return True if equal otherwise False. Used to check A# == Bb or Ab == Z#
        """
        normalized_note = self.normalize()
        normalized_other = other.normalize()

        if normalized_other is None or normalized_note is None:
            return False
        else:
            return normalized_other == normalized_note


class NoteCollection:
    """NoteCollection class."""

    def __init__(self):
        """
        Initialize the NoteCollection class.

        You will likely need to add something here, maybe a dict or a list?
        """
        self.note_collection = []

    def add(self, note: Note) -> None:
        """
        Add note to the collection.

        Check that the note is an instance of Note, if it is not, raise the built-in TypeError exception.

        :param note: Input object to add to the collection
        """
        if not isinstance(note, Note):
            raise TypeError("Input 'note' must be an instance of the Note class")
        elif note not in self.note_collection:
            self.note_collection.append(note)

    def pop(self, note: str) -> Note | None:
        """
        Remove and return previously added note from the collection by its name.

        If there are no elements with the given name, do not remove anything and return None.

        :param note: Note to remove
        :return: The removed Note object or None.
        """
        note_to_search = Note(note)
        if note_to_search in self.note_collection:
            self.note_collection.remove(note_to_search)
            return note_to_search
        else:
            return None

    def extract(self) -> list[Note]:
        """
        Return a list of all the notes from the collection and empty the collection itself.

        Order of the list must be the same as the order in which the notes were added.

        Example:
          collection = NoteCollection()
          collection.add(Note('A'))
          collection.add(Note('C'))
          collection.extract() # -> [<Note: A>, <Note: C>]
          collection.extract() # -> []

        In this example, the second time we use .extract() the output list is empty
        because we already extracted everything.

        :return: A list of all the notes that were previously in the collection.
        """
        self.return_note_collection = self.note_collection
        self.note_collection = []
        return self.return_note_collection[::]

    def get_content(self) -> str:
        """
        Return a string that gives an overview of the contents of the collection.

        Example:
          collection = NoteCollection()
          collection.add(Note('C#'))
          collection.add(Note('Lb'))
          print(collection.get_content())

        Output in console:
           Notes:
            * C#
            * Lb

        The notes must be sorted alphabetically by name and then by sharpness, that is A, A#, B, Cb, C and so on.
        Recommendation: Use normalized note names, not just the __repr__()

        :return: Content as a string
        """
        sorted_notes = sorted(self.note_collection, key=lambda x: x.normalize())
        content = "Notes:\n"
        for note in sorted_notes:
            content += f"  * {note.normalize()}\n"
        if content == "Notes:\n":
            return "Notes:\n  Empty."
        return content.strip()

class Chord:
    def __init__(self, note_one, note_two, chord_name, note_three=None):
        self.notes = [note_one.note, note_two.note]
        if note_three:
            self.notes.append(note_three.note)

        if len(set(self.notes)) != len(self.notes):
            raise DuplicateNoteNamesException("Chord contains duplicate note names.")

        self.notes.sort()
        self.chord_name = chord_name

    def __repr__(self):
        return f"<Chord: {self.chord_name}>"

    def __eq__(self, other):
        return (isinstance(other, Chord) and
                self.notes == other.notes and
                self.chord_name == other.chord_name)

    def __hash__(self):
        return hash((tuple(self.notes), self.chord_name))


class Chords:
    def __init__(self):
        self.chords = {}

    def add(self, chord):
        if chord.notes in self.chords:
            raise ChordOverlapException("Chord combination already exists.")
        self.chords[chord.notes] = chord

    def get(self, first_note, second_note, third_note=None):
        notes = [first_note.name, second_note.name]
        if third_note:
            notes.append(third_note.name)

        notes.sort()
        for chord_notes, chord in self.chords.items():
            if sorted(notes) == sorted(chord_notes):
                return chord
        return None

if __name__ == '__main__':
    chords = Chords()
    chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
    chords.add(Chord(Note('G'), Note('F'), 'Amaj', Note('H')))
    print(chords.get(Note('A'), Note('C'), Note('B')))  # ->  <Chord: Amaj>
    print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
    print(chords.get(Note('D'), Note('Z')))  # ->  None
    chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
    print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>"""

    chords = Chords()

    chord1 = Chord(Note('A'), Note('C#'), 'Amaj', Note('E'))
    chord2 = Chord(Note('E'), Note('G'), 'Emin', note_three=Note('B'))
    chord3 = Chord(Note('E'), Note('B'), 'E5')

    chords.add(chord1)
    chords.add(chord2)
    chords.add(chord3)

    print(chords.get(Note('e'), Note('b')))  # -> <Chord: E5>

    try:
        wrong_chord = Chord(Note('E'), Note('A'), 'E')
        print('Did not raise, not working as intended.')
    except DuplicateNoteNamesException:
        print('Raised DuplicateNoteNamesException, working as intended!')

    try:
        chords.add(Chord(Note('E'), Note('B'), 'Emaj7add9'))
        print('Did not raise, not working as intended.')
    except ChordOverlapException:
        print('Raised ChordOverlapException, working as intended!')