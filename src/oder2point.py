# import csv

# csvfile = open("order_.csv","w")
# writer = csv.writer(csvfile)

# writer.writerow(["lati"])
f = open("order_20161101.txt")
print("经纬度")
count = 0
for line in f:
    count += 1
    if count > 2:
        break
    line1 = "\"" + line[55:75] + "\""
    line2 = "\"" + line[76:-1] + "\""
    print(line1)
    print(line2)
