"""CP1404/CP5632 Practical - Programming Language."""


class ProgrammingLanguage:
    """List format for programming languages"""

    def __init__(self, name, typing, reflection, year):
        """Constructor that takes in parameters and creates objects"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determines Dynamic Typing"""
        return self.typing == "Dynamic"

    def reflection(self):
        """Determines reflection """
        if self.reflection is True:
            return "True"
        elif self.reflection is False:
            return "False"

    def __repr__(self):
        """Return details of object in string format"""
        return "{}, {} Typing, Reflection = {}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                             self.year)

