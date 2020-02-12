s = open("pur_out_map.txt","r")
r = open("pur_red_out.txt", "w")

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  time, cost = data

  if time != thisKey:

    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = time
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(cost)


# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()