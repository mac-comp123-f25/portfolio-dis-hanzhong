def sum3(input_list):
    assert isinstance(input_list,(list,tuple)) #make sure input is list/tuple
    assert len(input_list) >= 3 #make sure the length of list is greater than 3
    assert all(isinstance(input_list[i], (int, float)) for i in range(3))
    result = input_list[0] + input_list[1] + input_list[2]
    return result

if __name__ == "__main__":
  print( sum3([5, 2, 8, -2, 6, 15]) )
  print( sum3([5, 2]) )
  print( sum3(5) )
  print( sum3(["h", "i", 1, 2, 3]) )
  print( sum3([1, 2, 3, "h", "i"]) )
