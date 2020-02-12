input = open("purchases.txt", "r")
output = open("pur_out_map.txt", "w")

for line in input:
    datalist = line.strip().split("    ")
    date, time, city, item, cost, paymentType = datalist
    output.write(time + "\t" + cost + "\n")

input.close()
output.close()