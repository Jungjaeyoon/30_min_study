#day 1, effective python better way 5
#slicing sequence
#basic slicing
#somelist[start:end] >> [somelist[start],...somelist[end-1]]
a = [1,2,3,4,5,6,7]
#skip first or last index  when slice result starts from first or last index
assert a[:5] == a[0:5]
assert a[5:] == a[5:len(a)]

#replace list values 
a[2:] = [0,0]
print(a)

#copy list
b = a[:]
assert b ==a and b is not a

#tip
#do not set 0 as start index or len(sequence) as end index
# slicing allow over range start or end index
# assign list slice replace original sequnce range to assign list   
