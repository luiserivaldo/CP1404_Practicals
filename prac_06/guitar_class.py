current_year = 2018


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Represent a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Returns the age of Guitar."""
        guitar_age = current_year - self.year  # replace current_year with the current year
        return guitar_age

    def is_vintage(self):
        """Check if Guitar is over 50 years."""
        return self.get_age() >= 50

    def __repr__(self):
        """Returns a string to represent Guitar."""
        return "My guitar: {0}, first made in {1}".format(self.name, self.year)

