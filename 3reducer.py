s = open("s.txt","r")
r = open("r.txt", "w")

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function

  #finds the sum
  #thisValue += float(amount)

  #finds the max
  #if float(amount) > thisValue:
    #thisValue = float(amount)

  #finds the min
  #if thisValue==0:
    #thisValue = float(amount)
  #elif float(amount) < thisValue:
    #thisValue = float(amount)

  #finds the count
  #thisValue +=1

  #finds the average

  count +=1
  thisValue += float(amount)
thisValue = thisValue/count



# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+' ' +str(count)+'\n')

s.close()
r.close()