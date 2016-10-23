def validBraces(string):
  pos = ['(', '{', '[']
  neg = [')', '}', ']']
  act = []
  for x in string:
      if x in pos:
          act.append(x)
      elif x in neg:
          if len(act) == 0:
              return False
          elif pos[neg.index(x)] == act[-1]:
              act = act[:-1]
          else:
              return False
  return True if len(act) == 0 else False