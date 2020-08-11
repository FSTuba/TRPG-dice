def trpgdice(n):
  import random
  a = n.split('d')
  b = 0
  for i in range(eval(a[0])):
    b = b + random.randint(1,eval(a[1]))
  return(b)

def makecha():
  
  print(trpgdice('3d6'),trpgdice('3d6'),trpgdice('3d6'),trpgdice('3d6'),trpgdice('3d6'))
  print(trpgdice('2d6')+6,trpgdice('2d6')+6)
  print(trpgdice('3d6')+3)
  print(trpgdice('1d10'))

def main():
  print("+++++++++++TRPG DICE ROLLER!+++++++++++")
  print("(輸入範例:1d100,3d6 輸入ch創角  輸入 end 結束)")
  print("\n\n\n\n")
  print("偉大的骰子女神吶，請賜予我無上的力量!!!")
  print("=======================================")
  while(True):
    n = input("-->")
    if n == "end" or n == '':
      break
    elif n == 'ch':
      makecha()
    else:
      print(n,">>>>>>",(trpgdice(n)))
    

main()

  
