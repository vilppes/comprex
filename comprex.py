class ComprehensibleRegex:
    def __init__(self) -> None:
        pass
    def set_of_characters(self,set_of_characters: str) -> str:
        return "["+set_of_characters+"]"
    def special_sequence(self,special_sequence: str) -> str:
        return "\\"+special_sequence
    def any_character(self) -> str:
        return "."
    def n_any_characters(self,n) -> str:
        any_characters=""
        for x in range(x):
            any_characters+=self.any_character()
        return any_characters
    def starts_with(self) -> str:
        return "^"
    def ends_with(self) -> str:
        return "$"
    def zero_or_more_occurences(self) -> str:
        return "*"
    def one_or_more_occurences(self) -> str:
        return "+"
    def zero_or_one_occurences(self) -> str:
        return "?"
    def exactly_the_specified_number_of_occurences(self,n) -> str:
        return "{"+str(n)+"}"
    def either_or(self,a,b) -> str:
        return a+"|"+b
    def capture_and_group(self,group) -> str:
        return "("+group+")"
    def format_one(self,a) -> str:
        return "{}".format(a)
    def format_two(self,a,b) -> str:
        return "{}{}".format(a,b)
    def special_sequences(self,n):
        """
        0 = Returns a match if the specified characters are at the beginning of the string
        1 = Returns a match where the specified characters are at the beginning or at the end of a word
        (the "r" in the beginning is making sure that the string is being treated as a "raw string")
        2 = Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
        (the "r" in the beginning is making sure that the string is being treated as a "raw string")
        3 = Returns a match where the string contains digits (numbers from 0-9)
        4 = Returns a match where the string DOES NOT contain digits
        5 = Returns a match where the string contains a white space character
        6 = Returns a match where the string DOES NOT contain a white space character
        7 = Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
        8 = Returns a match where the string DOES NOT contain any word characters
        9 = Returns a match if the specified characters are at the end of the string
        """
        sequence_characters = ["A","b","B","d","D","s","S","w","W","Z"]
        if n > len(sequence_characters):
            raise Warning("out of index with the special sequences")
        return self.special_sequence(sequence_characters[n])