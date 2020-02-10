f = open("d.txt","r")  # open file, read-only
o = open("o.txt", "w") # open file, write
for line in f:
    data = line.strip().split("    ")
    print (data)
    #print (len(data))
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print ("{0}\t{1}".format(store, cost))
        o.write("{0}\t{1}\n".format(store, cost))
f.close()
o.close()