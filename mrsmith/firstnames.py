
firstnames = []
with open('firstnames.data') as f:
    f.readline()
    for line in f:
        firstname = line.strip().split(',')
        firstnames.append((firstname[0], int(firstname[1]), float(firstname[2]), float(firstname[3]), float(firstname[4]), float(firstname[5]), float(firstname[6]), float(firstname[7])))

print(firstnames)