def chained(funcs):
  def fun(x):
    result = x
    
    for i in range(len(funcs)):
      result = funcs[i](result)

    return result
  return fun