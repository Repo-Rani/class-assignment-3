# full diamond shape pyramid pattern

rows = 5  

# Upper half
for i in range(1, rows + 1):
    print(' ' * (rows - i), end='') # print spaces
    print('*' * (2 * i - 1))        # print stars

# Lower half
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i), end='') # print spaces
    print('*' * (2 * i - 1))        # print stars
