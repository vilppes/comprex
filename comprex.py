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