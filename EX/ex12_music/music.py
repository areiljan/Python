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


if __name__ == '__main__':
    note_one = Note('a')  # yes, lowercase
    note_two = Note('C')
    note_three = Note('Eb')
    collection = NoteCollection()

    print(note_one)  # <Note: A>
    print(note_three)  # <Note: Eb>

    collection.add(note_one)
    collection.add(note_two)

    print(collection.get_content())
    # Notes:
    #   * A
    #   * C

    print(collection.extract())  # [<Note: A>,<Note: C>]
    print(collection.get_content())
    # Notes:
    #  Empty

    collection.add(note_one)
    collection.add(note_two)
    collection.add(note_three)

    print(collection.pop('a') == note_one)  # True
    print(collection.pop('Eb') == note_three)  # True

class Chord:
    """Chord class."""

    def __init__(self, note_one: Note, note_two: Note, chord_name: str, note_three: Note = None):
        """
        Initialize chord class.

        A chord consists of 2-3 notes and their chord product (string).
        If any of the parameters are the same, raise the 'DuplicateNoteNamesException' exception.
        """
        self.note_one = note_one
        self.note_two = note_two
        if note_three is not None:
            self.note_three = note_three
            self.notes = [self.note_one.normalize(), self.note_two.normalize(), self.note_three.normalize()]
        else:
            self.notes = [self.note_one.normalize(), self.note_two.normalize()]
        self.chord_name = chord_name
        set_of_notes = set(self.notes)
        self.notes.sort()
        if not len(list(set_of_notes)) == len(self.notes) or chord_name in self.notes:
            raise DuplicateNoteNamesException()

    def __repr__(self) -> str:
        """
        Chord representation.

        Return as: <Chord: [chord_name]> where [chord_name] is the name of the chord.
        """
        return f"<Chord: {self.chord_name}>"

    def __eq__(self, other):
        return (isinstance(other, Chord) and self.notes == other.notes and self.chord_name == other.chord_name)

    def __hash__(self):
        return hash((tuple(self.notes), self.chord_name))


class Chords:
    """Chords class."""

    def __init__(self):
        """
        Initialize the Chords class.

        Add whatever you need to make this class function.
        """
        self.chords = {}
    def add(self, chord: Chord) -> None:
        """
        Determine if chord is valid and then add it to chords.

        If there already exists a chord for the given pair of components, raise the 'ChordOverlapException' exception.

        :param chord: Chord to be added.
        """
        if tuple(chord.notes) in tuple(self.chords):
            raise ChordOverlapException()
        self.chords[tuple(chord.notes)] = chord

    def get(self, first_note: Note, second_note: Note, third_note: Note = None) -> Chord | None:
        """
        Return the chord for the 2-3 notes.

        The order of the first_note and second_note and third_note is interchangeable.

        If there are no combinations for the 2-3 notes, return None

        Example:
          chords = Chords()
          chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
          print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
          print(chords.get(Note('B'), Note('C'), Note('A')))  # ->  <Chord: Amaj>
          print(chords.get(Note('D'), Note('Z')))  # ->  None
          chords.add(Chord(Note('c#'), Note('d#'), 'c#5'))
          print(chords.get(Note('C#'), Note('d#')))  # ->  <Chord: c#5>

        :param first_note: The first note of the chord.
        :param second_note: The second note of the chord.
        :param third_note: The third note of the chord.
        :return: Chord or None.
        """
        chords_in_list = [first_note.normalize(), second_note.normalize()]
        try:
            if third_note:
                chords_in_list.append(third_note.normalize())
        except AttributeError:
            pass

        sorted_chord = tuple(sorted(chords_in_list))

        return self.chords.get(sorted_chord)


class DuplicateNoteNamesException(Exception):
    """Raised when attempting to add a chord that has same names for notes and product."""


class ChordOverlapException(Exception):
    """Raised when attempting to add a combination of notes that are already used for another existing chord."""


if __name__ == '__main__':
    chords = Chords()
    chords.add(Chord(Note('A'), Note('B'), 'Amaj', Note('C')))
    print(chords.get(Note('A'), Note('B'), Note('C')))  # ->  <Chord: Amaj>
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

