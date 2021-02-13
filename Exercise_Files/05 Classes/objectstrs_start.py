# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "<Person fname:{}, lname:{}, age:{}>".format(
            self.fname, self.lname, self.age)

    # TODO: use str for a more human-readable string
    def __str__(self):
        return "Person ({}, {}, {})".format(
            self.fname, self.lname, self.age)


def main():
    # create a new Person object
    cls1 = Person()

    # use different Python functions to convert it to a string
    print(repr(cls1))
    print(str(cls1))
    print("Formatted: {0}".format(cls1))


if __name__ == "__main__":
    main()
