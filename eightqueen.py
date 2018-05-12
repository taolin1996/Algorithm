import  itertools

def is_valid_8_quene(col_index):
  for i in range(8):
    for j in range(8):
      if i != j and abs(i-j) == abs(col_index[i] - col_index[j]):
        return False
  return True

def count_8_quene_solutions():
  return sum([1 for p in itertools.permutations(range(8)) if is_valid_8_quene(p)])

if __name__ == '__main__':
  print (count_8_quene_solutions())
