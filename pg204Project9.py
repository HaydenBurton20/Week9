file = input("Filename: ")
sum = 0 
count = 0
fopen = open(file, "r")
content = fopen.read().split()
for line in content:
	sum += int(line)
	count += 1
fopen.close()
average = float(sum)/count
print("Average: ",average)