# as08.py

def is_reflexive(Set, Relation):
  """
  A relation 'Relation' on a set 'Set' is called reflexive when:
  ∀ a ∈ Set, (a,a) ∈ Relation
  https://en.wikipedia.org/wiki/Reflexive_relation

  Args:
      Set: A set of comparable values.
      Relation: A set of 2-tuples of comparable values.

  Returns:
      A boolean value indicating whether Relation is reflexive, with regard to Set.
  """
  R = list(Relation)
  result = set(ab for ab in R if ab[0] == ab[1])
  return True if len(Set) == len(result) else False

def is_symmetric(Relation):
  """
  A relation 'Relation' is called symmetric when:
  ∀ (a, b) ∈ Relation, (b, a) ∈ Relation
  https://en.wikipedia.org/wiki/Symmetric_relation

  Args:
      Relation: A set of 2-tuples of comparable values.

  Returns:
      A boolean value indicating whether Relation is symmetric.
  """
  counter = 0
  for thing in Relation:
      if (locate(Relation,thing) == True):
          if (locate(Relation,(thing[1],thing[0])) == True):
              counter +=1
  if (counter == len(Relation)):
      return True
  else:
      return False


def is_antisymmetric(Relation):
  """
  A relation 'Relation' is called antisymmetric when:
  ∀ (a, b) ∈ Relation, (b, a) ∈ Relation ==> a = b
  https://en.wikipedia.org/wiki/Antisymmetric_relation

  Args:
      Relation: A set of 2-tuples of comparable values.

  Returns:
      A boolean value indicating whether Relation is antisymmetric.
  """
  counter = 0
  for thing in Relation:
      if (locate(Relation,thing) == True and locate(Relation,(thing[1],thing[0])) == True and Relation != thing):
          counter +=1
  if (counter == len(Relation)):
      return False
  else:
      return True

def is_transitive(Relation):
    """
    A relation 'Relation' is called transitive when:
    ∀ (a, b) ∈ Relation, (b, c) ∈ Relation ==> (a, c) ∈ Relation
    https://en.wikipedia.org/wiki/Transitive_relation

    Args:
    Relation: A set of 2-tuples of comparable values.

    Returns:
    A boolean value indicating whether Relation is symmetric.
    """
    temp = set((a,b) for a, c in Relation for d, b in Relation if d == c)

    comparison = Relation | temp
    if comparison == Relation:
        return True
    else:
        return False

def composite(R1, R2):
  """
  The composite of relations 'R1' and 'R2' is the relation consisting
  of tuples (a,c), such that (a,b) ∈ R1 and (b,c) ∈ R2
  https://en.wikipedia.org/wiki/Composition_of_relations

  Args:
      R1: A set of 2-tuples of comparable values.
      R2: A set of 2-tuples of comparable values.

  Returns:
      A set of 2-tuples consisting of the composite of R1 and R2.
  """
  return set((a,c) for a, x in R1 for y, c in R2 if x == y)

def is_equivalence(Set, Relation):
  """
  A relation 'Relation' on a set 'Set' is called an equivalence relation
  if it is reflexive, symmetric, and transitive
  https://en.wikipedia.org/wiki/Equivalence_relation

  Args:
      Set: A set of comparable values.
      Relation: A set of 2-tuples of comparable values.

  Returns:
      A boolean value indicating whether Relation is an equivalence relation with regard to Set.
  """
  if(is_transitive(Relation) == True and is_reflexive(Set, Relation) == True and is_symmetric(Relation) == True):
      return True
  else:
      return False

  """
  Determines if something is in a list or not. If it is, returns true. Defaults to false.
  """
def locate(Relation, item):
    for thing in Relation:
        if item in Relation:
            return True
        else:
            return False
