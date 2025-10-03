from my_bet import*

def test_between():
    assert between(10,0,20) == True

if __name__ == "__main__":
  print( between(10, 0, 20) )
  print( between(25, 10, 20) )
  print( between(5.3, 6.7, 3.1) )
  print( between(5.3, 3.1, 6.7) )
  print(between("kookaburra", "aardvark", "tapir")) # cause error