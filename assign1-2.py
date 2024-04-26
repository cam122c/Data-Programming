def output_star(row):
    for i in range(1,row +1):
        print('*' *i)
row_number = int(input("enter the number of rows for the star triangle:"))

output_star(row_number)