def is_list(lists=None):
  if lists is not None:
    if isinstance(lists, list):
      return True
    else:
      return False

def find_max_min(lists):

  is_list(lists)
  min_max = []
  new_list = []
  while True:

    sorted_list = sorted(lists)
    min_num = sorted_list[0]
    max_num = sorted_list[len(sorted_list)-1]
    if min_num < max_num:
      min_max.append(min_num)
      min_max.append(max_num)
      return min_max
    elif min_num == max_num:
      elements = len(lists)
      new_list.append(elements)
      return new_list

    
