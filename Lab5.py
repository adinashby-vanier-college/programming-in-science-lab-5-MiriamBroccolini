# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    square = ""
    for count in range(n):
        square += "*"

        for subcount in range(n-2):
            if count == 0 or count == n-1:
                square += "*"
            else:
                square += " "

        if n >1:
            square += "*"
        if count < n-1:
            square += "\n"

    return square

#print(hollow_square(5))

# 1
# 12
# 123
# 1234

def number_pattern(n):
    string = "" 
    count = 1

    while count <= n:
        subcount = 1

        while subcount <= count:
            string += str(subcount)

            if subcount == count and count < n:
                string += "\n"

            subcount += 1

        count +=1
        
    return string

#print(number_pattern(5))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    count = 0

    while count < n:
        total += count+1
        count += 1

    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    length = 2 * n - 1
    pyramid = ""

    for count in range(n):
        for subcount in range(length):
            if length // 2 - count <= subcount <= length // 2 + count :
                pyramid += "*"
            elif subcount <= length//2 + count:
                pyramid += " "
            elif subcount == length - 1  and subcount != count:
                    pyramid += "\n"

    return pyramid
