import re
import unittest


class RegEx():

    def use_reg_ex(self):
        # check whether string starts and ends with expected values
        txt = "The rain in Spain"
        x = re.search("^The.*Spain$", txt)
        y = re.search("^The.*Spain$", txt)
        print(x)
        print(y)

        # find all
        txt = "The rain in Spain"
        x = re.findall("ai", txt)
        print(len(x), x)

        txt = "The rain in Spain"
        x = re.findall("Portugal", txt)
        print(len(x), x)

        # search
        txt = "The rain in Spain"
        x = re.search("\s", txt)
        print("The first white-space character is located in position:", x.start())

        txt = "The rain in Spain"
        x = re.search("Portugal", txt)
        print(x)

        # split
        txt = "The rain in Spain"
        x = re.split("\s", txt)
        print(x)

        txt = "The rain in Spain"
        x = re.split("\s", txt, 1)
        print(x)

        # sub
        txt = "The rain in Spain"
        x = re.sub("\s", "9", txt)
        print(x)

        txt = "The rain in Spain"
        x = re.sub("\s", "9", txt, 2)
        print(x)

        # match properties
        """
        .span() returns a tuple containing the start-, and end positions of the match.
        .string returns the string passed into the function
        .group() returns the part of the string where there was a match
        """
        txt = "The rain in Spain"
        x = re.search(r"\bS\w+", txt)
        print(x.span())

        txt = "The rain in Spain"
        x = re.search(r"\bS\w+", txt)
        print(x.string)

        txt = "The rain in Spain"
        x = re.search(r"\bS\w+", txt)
        print(x.group())


if __name__ == "__main__":
    reg = RegEx()
    reg.use_reg_ex()