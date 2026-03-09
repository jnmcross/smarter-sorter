"""
Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.
"""

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    :param width: dimension in cm
    :param height: dimension in cm
    :param length: dimension in cm
    :param mass: kg
    :return: string: the name of the stack where the package should go.
        one of
        STANDARD: not bulky or heavy
        SPECIAL:
          bulky: volume >= 1,000,000 cm³ or one dimension >= 150 cm
          heavy: bulky mass >= 20kg
        REJECTED: both heavy and bulky
        INVALID: invalid input parameters
    """
    heavy = False
    bulky = False

    # reject invalid input up front
    #
    # test for zeroes
    if not width or not height or not length or not mass:
        return "INVALID"

    # test for negatives
    if width < 0 or height < 0 or length < 0 or mass < 0:
        return "INVALID"

    # check for bulky
    if width * height * length >= 1000000 or max(width, height, length) >= 150:
        bulky = True

    # check for heavy
    if mass >= 20:
        heavy = True

    if bulky and heavy:
        return "REJECTED"

    elif bulky or heavy:
        return "SPECIAL"

    else: # must be standard
        return "STANDARD"


# helper to write input and output
def help_sort(comment:str, width: float, height: float, length: float, mass: float):
    print(f"{comment} [w (cm) x h (cm) x l (cm), mass (kg)]:"
          f"\n input: {width} x {height} x {length}, {mass}" 
          f"\n output: {sort(width, height, length, mass)}\n")

# run sort with various input
# standard package
help_sort("within bounds", 140.5, 2.1, 3.001, 19.2)
help_sort("just within bounds", 149.999999999, 2.1, 3.001, 19.99999)

# invalid zero dimension
help_sort("out of bounds", 0, 20, 30, 40)
# invalid negative dimension
help_sort("out of bounds", 1, -2, 1, 2)
# invalid no mass
help_sort("out of bounds", 1, 2, 3, 0)

# bulky single dimension >= 151
help_sort("right on the bound", 150, 2, 3, 19)
help_sort("above the bound", 151, 2, 3, 19)
# bulky volume >= 1,000,000
help_sort("right on the bound",100,100, 100, 19)
help_sort("above the bound", 101,2000, 30000, 19)
# heavy mass >= 20
help_sort("right on the bound", 1, 2, 3, 20)
help_sort("above the bound", 1, 2, 3, 30)

# bulky and heavy
help_sort("right on the bound", 100,100, 100, 20)
help_sort("above the bound", 101,100, 100, 20)
help_sort("above the bound", 100,100, 100, 21)
