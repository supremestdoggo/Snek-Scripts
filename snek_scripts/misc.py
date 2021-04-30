def organize(list):
  old_list = list
  new_list = []
  while len(old_list) != 0:
    new_list.append(max(old_list))
    old_list.remove(max(old_list))
  return new_list