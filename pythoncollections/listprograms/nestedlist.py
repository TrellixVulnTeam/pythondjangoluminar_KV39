students=[
    [10,"ajay","bca",250],
    [11, "vijay", "bca", 240],
    [12, "sibin", "bca", 220],
    [13, "dino", "mca", 220],
    [14,"tom","mca",180],
    [15, "jain", "mca", 250],
]
#print only student name
for stud in students:
    print(stud[1])
#print students name whose mark>0
for stud in students:
    if stud[3]>240:
        print(stud[1])
#print total sum of mark
mark=0
for stud in students:
    mark+=mark+stud[3]
    print(mark)



#calculate total of bca and mca seperately
mtotal,btotal=0,0
for stud in students:
    if stud[2]=="bca":
        btotal+=stud[3]
    else:
        mtotal+=stud[3]
print("mca total=",mtotal)
print("bca total=",btotal)