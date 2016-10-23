def order(sentence):
  # code here
  list = sentence.split()
  order = []
  for word in list:
      for char in word:
          if char in [str(i) for i in range(1, len(list) + 2)]:
              order.append(int(char))
  result = ""
  orderR = []
  for i in range(len(order)):
      for j in range(len(order)):
          if order[j] == i + 1:
              orderR.append(j)
      
  for pos in orderR:
      if result != "":
          result = result + " " + list[pos ]
      else:
          result = list[pos]
  return(result)