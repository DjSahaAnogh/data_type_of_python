def get_strings_methods():
  i: int = 0
  for method in dir(str):
    if "_" not in method:
      i += 1