num = []
pn = [int(line.strip()) for line in open(r'C:\Users\camca\Downloads\primenumbers.txt')]
ln = [int(line.strip()) for line in open(r'C:\Users\camca\Downloads\luckynumbers.txt')]

overlappingnumbers = list(set(pn) & set(ln))

if overlappingnumbers:
    print("The overlapping numbers in both files are:")
    for number in sorted(overlappingnumbers):
        print(number)
    num = list(overlappingnumbers)
print(num)