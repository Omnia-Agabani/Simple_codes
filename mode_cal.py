def mode_cal (numbers):
  """ The function calculate the mode of list of numbers

  Parameters:
      numbers (list): list of numbers that need to be calculate

  Returns:
      integer : The mode of the list
  """
  assert isinstance(numbers, list), "input should be a list"
  for num in numbers:
    assert isinstance (num, int),"The list should contain numbers only"
  if numbers == []:
    mode=0
  else:
    