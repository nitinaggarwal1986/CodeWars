def get_start_time(schedules, duration):
  
  
  scht = [[[int(z[:2] + z[3:]) for z in y] for y in x] for x in schedules]
  dur = int(duration / 60) + float(duration % 60 / 100.0)
  
  def busy_time(scht):
    temp = []
    for x in scht:
      for y in x:
        temp.append(y)
    
    temp = sorted(temp, key = lambda x : x[0])
    busy = [temp[0]]
    max1 = temp[0][1]
    print(temp)
    for i in range(1, len(temp)):
      if temp[i][0] <= max1:
        busy[-1][1] = max(temp[i][1], busy[-1][1])
      else:
        busy.append(temp[i])
      max1 = max([temp[i][1], max1]) 
    return busy
  
  def free_time(busyTime):
    
    freeTime = []
    
    if busyTime[0][0] > 900:
      freeTime.append([900, busyTime[0][0]])
    
    i = 0
    
    if len(busyTime) > 1:
      for i in range(len(busyTime)-1):
        freeTime.append([busyTime[i][1], busyTime[i + 1][0]])
    
      if busyTime[-1][1] < 1900:
        freeTime.append([busyTime[-1][1], 1900])
    
    return freeTime
  
  bt = busy_time(scht)
  
  if bt == []:
    return '09:00'
  
  ft = free_time(bt)
  
  fg = [float(str("{0:.2f}".format((x[1] - x[0]) / 100.0)))  if (int(x[1] / 100) - int(x[0] / 100)) == int((x[1] - x[0]) / 100) else float(str("{0:.2f}".format((x[1] - x[0]) / 100.0))) + 0.60 - 1 for x in ft]
  
  meeting = None
  
  for i in range(len(fg)):
    if fg[i] >= dur:
      ch = i
      temp = str(ft[i][0]).zfill(4)
      return temp[:2] + ":" + temp[2:]
  
  return meeting