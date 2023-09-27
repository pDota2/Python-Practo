def rectangle_area(width, height):
    return width * height

def is_even(number):
    try:
        number % 2 == 0 
        return True
    except:
        return False

def sum_digits(number):
    numS = 0
    while number:
        numS += number % 10
        number //= 10
    return numS