values = []

def initalize_list(n):
    global values
    for x in range(n):
        values.append('P')
    values[0] = 'N'
    values[1] = 'N'

def find_prime():
    global values
    l = int((len(values) / 2) + 1)                      # Get halfway index+1 for end of range to examine
    for x in range(2, l):                               # Loop from index to to l
        if values[x] == 'P':                            # Index is prime...loop through list marking multiples as 'N'
            for y in range (x, len(values), x):         # Find every multiple of x and mark as 'N'
                if y == x: continue                     # Skip the first which IS prime
                elif values[y] != 'N':                  # Only do if its not already equal to 'N'
                    values[y] = 'N'                     # Set multiples

def print_prime():
    global values
    last = str(len(values))                             # Get last value
    length = len(last) + 1                              # Add one onto length for space inbetween
    counter = 1                                         # Count 10 columns
    for x in range(len(values)):
        if values[x] == 'P':
            output = str(x)                             # Build an output string
            if counter % 10 == 0:                       # Determine if column is 10 wide
                output += '\n'
            else:
                while len(output) != length:            # Add spacing to maintain columns
                    output += ' '
            counter += 1
            print(output, end='')

def main():
    n = int(input('Enter a positive integer: '))
    initalize_list(n)
    #print(values)
    find_prime()
    #print(values)
    print_prime()

main()
