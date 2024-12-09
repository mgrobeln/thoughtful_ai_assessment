import argparse

def get_volume(width, height, length):
    return width*height*length

def sort(width, height, length, mass):
    """
    params:
        width: assuming the value is a float in cm
        height: assuming the value is a float in cm
        length: assuming the value is a float in cm
        mass: assuming value is a float in kg
    """

    try:
        width = float(width)    # Ensure width is a float
        height = float(height)  # Ensure height is a float
        length = float(length)  # Ensure length is a float
        mass = float(mass)  # Ensure mass is a float

    except ValueError as e:
        raise ValueError(f"""Invalid input: 'width', 'height', 'length' and 'mass' must be numbers. 
                         Received: width={width}, height={height}, length={length}, mass={mass}""") from e

    is_bulky = False
    is_heavy = False
    volume = get_volume(width=width, height=height, length=length)
    # A package is bulky if 
    # its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or 
    # when one of its dimensions is greater or equal to 150 cm.
    if volume >= 1000000 or (height >= 150 or length >= 150 or width >= 150):
        is_bulky = True
    if mass >= 20:
        is_heavy = True
    if is_heavy and is_bulky:
        return "REJECTED"
    elif is_heavy or is_bulky:
        return "SPECIAL"
    elif not (is_heavy or is_bulky):
        return "STANDARD"
    
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Classify a package based on its dimensions and mass.")
    parser.add_argument("--w", type=float, required=True, help="Width of the package in cm")
    parser.add_argument("--h", type=float, required=True, help="Height of the package in cm")
    parser.add_argument("--l", type=float, required=True, help="Length of the package in cm")
    parser.add_argument("--m", type=float, required=True, help="Mass of the package in kg")

    args = parser.parse_args()

    package_stack = sort(width=args.w, height=args.h, length=args.l, mass=args.m)
    print(package_stack)