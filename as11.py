def is_function(potential_function):
    """
    Determines whether the argument is a function
    given a domain and codomain of all integers [-10^6, 10^6]
    """
    data = dict()
    a = -10**3
    b = 10**3
    for i in range(a, b):
        if potential_function(i) in data.keys():
            return False
        data[i]=potential_function(i)
    return True

def is_partial(potential_partial_function):
    """
    Determines whether the argument is a partial function
    given a domain and codomain of all integers [-10^6, 10^6]
    """
    #if it's a function it must also be a partial function, right?
    if is_function(potential_partial_function):
        return True

    data = dict()
    a = -10**3
    b = 10**3
    for i in range(a, b):
        if potential_partial_function(i) in data.keys():
            return False
        data[i]=potential_partial_function(i)
    return True

def is_injective(potential_injective_function):
    """
    Determines whether the argument is an injective function
    given a domain and codomain of all integers [-10^6, 10^6]
    """
    data = dict()
    a = -10*3
    b = 10**3
    for i in range(a, b):
        data[i]=potential_injective_function(i)
    for item1 in data:
        for item2 in data:
            if data[item1] == data[item2] and item1 != item2:
                return False
    return True

def are_equivalent(potential_function_1, potential_function_2):
  """
  Determines whether the arguments are equivalent functions
  in the domain and codomain of all integers [-10^6, 10^6]
  """
  func1 = dict()
  func2 = dict()
  a = -10**6
  b = 10**6

  for i in range(a, b):
    func1[i]=potential_function_1(i)
    func2[i]=potential_function_2(i)

  for item in func1:
    if func1[item] != func2[item]:
      return False
  return True
