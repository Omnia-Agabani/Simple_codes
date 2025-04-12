def mean_cal(numbers: list)-> float:
  """ The function calculate the mean of list of numbers

  Parameters:
      numbers (list): list of numbers that need to be calculate

  Returns:
      float: The mean of the list
  """
  assert isinstance(numbers, list), "input should be a list"
  for num in numbers:
    assert isinstance (num, int),"The list should contain numbers only"
  if numbers == []:
    mean = 0
  else:
    summation = sum(numbers)
    length = len(numbers)
    mean = summation / length
  return mean  
