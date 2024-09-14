print()
rno = int(input("{:_<25}: ".format("Enter Roll Number")))
name = input("{:_<25}: ".format("Enter Name"))

print()
print("Enter All Subjects' Marks")
print("-------------------------------")

hin = -1
while hin<0 or hin>100:
    hin = int(input("{:_<25}: ".format("Hindi Marks")))

    if hin<0 or hin>100:
        print()
        print("Marks must be between 0 and 100.")
        print()

eng = -1
while eng<0 or eng>100:
    eng = int(input("{:_<25}: ".format("English Marks")))

    if eng<0 or eng>100:
        print()
        print("Marks must be between 0 and 100.")
        print()

mat = -1
while mat<0 or mat>100:
    mat = int(input("{:_<25}: ".format("Mathematics Marks")))

    if mat<0 or mat>100:
        print()
        print("Marks must be between 0 and 100.")
        print()

sci = -1
while sci<0 or sci>100:
    sci = int(input("{:_<25}: ".format("Science Marks")))

    if  sci<0 or sci>100:
        print()
        print("Marks must be between 0 and 100.")
        print()

soc = -1
while soc<0 or soc>100:
    soc = int(input("{:_<25}: ".format("Social Marks")))

    if soc<0 or soc>100:
        print()
        print("Marks must be between 0 and 100.")
        print()

tel = -1
while tel<0 or tel>100:
    tel = int(input("{:_<25}: ".format("Telugu Marks")))

    if tel<0 or tel>100:
        print()
        print("Marks must be between 0 and 100.")
        print()

total = hin + eng + mat + sci + soc + tel
per = total * 100 / 600

isPassed = hin>=35 and eng>=35 and mat>=35 and sci>=35 and soc>=35 and tel>=35

if isPassed:
    if per>=75:
        grd = 'A'
    elif per<75 and per>=60:
        grd = 'B'
    elif per<60 and per>=45:
        grd = 'C'
    else:
        grd = 'D'
else:
    grd = 'F'

rno = f"{rno:08}"
hin = f"{hin:>2}F" if hin<35 else f"{hin:>3}"
eng = f"{eng:>2}F" if eng<35 else f"{eng:>3}"
mat = f"{mat:>2}F" if mat<35 else f"{mat:>3}"
sci = f"{sci:>2}F" if sci<35 else f"{sci:>3}"
soc = f"{soc:>2}F" if soc<35 else f"{soc:>3}"
tel = f"{tel:>2}F" if tel<35 else f"{tel:>3}"

if isPassed:
    print()
    print("+-----------------------------------------------+")
    print("| {:<18}: {:<25} |".format("Roll Number", rno))
    print("| {:<18}: {:<25} |".format("Name", name))
    print("+-------+-------+-------+-------+-------+-------+")
    print("|  HIN  |  ENG  |  MAT  |  SCI  |  SOC  |  TEL  |")
    print("+-------+-------+-------+-------+-------+-------+")
    print("|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |".format(hin, eng, mat, sci, soc, tel))
    print("+-------+-------+-------+-------+-------+-------+")
    print("|                                               |")
    print("|{:^47}|".format("CONGRATULATIONS"))
    print("|{:^47}|".format("You Passed!"))
    print("|                                               |")
    print("+-------------------------------+---------------+")
    print("| TOTAL MARKS OBTAINED          | {:>13} |".format(total))
    print("| PERCENTAGE                    | {:>12.2f}% |".format(per))
    print("| GRADE                         | {:>13} |".format(grd))
    print("+-------------------------------+---------------+")
else:
    print()
    print("+-----------------------------------------------+")
    print("| {:<18}: {:<25} |".format("Roll Number", rno))
    print("| {:<18}: {:<25} |".format("Name", name))
    print("+-------+-------+-------+-------+-------+-------+")
    print("|  HIN  |  ENG  |  MAT  |  SCI  |  SOC  |  TEL  |")
    print("+-------+-------+-------+-------+-------+-------+")
    print("|  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |".format(hin, eng, mat, sci, soc, tel))
    print("+-------+-------+-------+-------+-------+-------+")
    print("|                                               |")
    print("|{:^47}|".format("SORRY"))
    print("|{:^47}|".format("You Failed!"))
    print("|                                               |")
    print("+-------------------------------+---------------+")
    print("| TOTAL MARKS OBTAINED          | {:>13} |".format(total))
    # print("| PERCENTAGE                    | {:>12.2f}% |".format(per))
    print("| GRADE                         | {:>13} |".format(grd))
    print("+-------------------------------+---------------+")

print()

