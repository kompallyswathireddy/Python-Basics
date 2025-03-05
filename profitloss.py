actualprice=float(input('Please enter actual price' ))
Salesprice=float(input('please enter selling price'))
if (Salesprice > actualprice):
 amount = Salesprice - actualprice
 print('total profit = {0}'.format(amount))
else:
 print('no profit')