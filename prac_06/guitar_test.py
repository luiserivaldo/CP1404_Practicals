from prac_06.guitar_class import Guitar


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2012, 2152.65)

    print("{} - Expected {}. Got {}".format(guitar.name, 95, guitar.get_age()))
    print("{} - Expected {}. Got {}".format(another_guitar.name, 5, another_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, False, guitar.is_vintage()))

main()
