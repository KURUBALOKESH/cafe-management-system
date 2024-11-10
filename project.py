cafe management
veg={'pasta':40,'pizza':40,'burger':60,'coffee':80,'cooldrink':20}
non_veg={'chicken_roast':80,'mamaos':70,'briyani':200,'fish':120}
print('menu list\n', veg)
print(non_veg)
c=0
c1=0
a=input('what do u want sir (veg or non_veg):')
if a=='non_veg':
  choice=str(input('enter ur order:'))
  if choice in non_veg.keys():
     print('first order added:',choice)
     c+=non_veg[choice] 
  else:
    print('no this order not have yet now',choice)
elif a=='veg':
      choice1=str(input('enter ur veg items:'))
      if choice1 in veg.keys():
        print('ur order placed:',choice1)
        c1+=veg[choice1]     
      else:
        print('no this order not have',choice1)
while 'yes':
  x=input('do u want one more order (yes or no):')
  if x=="yes":
    y=input("Do u want one more Items:") 
    if y in non_veg.keys():
     print('ur order placed:',y)
     c+=non_veg[y]
    else:
      if y in veg.keys():
        print('ur order placed:',y)
        c1+=veg[y]  
      else:
        print('this order not have yet now',y)  
  elif x=='no':
      print('I do not want')  
      break
if a=='veg':
  print(f'total cost of {a} dishes:',c1,'\nplease visit again')
else:
  print(f'total cost of {a} dishes:',c,'\nplease visit again')
