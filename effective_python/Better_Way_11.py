# zip


names = ['Jeon','Yu','Ri']
letters = [len(n) for n in names]

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print(longest_name)



#Use zip for easier code


for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
	max_letters = count

# In python2 zip doesn\'t mean generator

# if iterator\'s length is not same, use itertools.zip_longest, it reads longest iterator 
