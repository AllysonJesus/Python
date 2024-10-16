dist = float(input('Qual a diantância da viagem em KM? '))

if dist <= 200:
    v = dist * 0.50
    print('A viagem será R${:.2f}'.format(v))    
else: 
    v = dist * 0.45
    print('A viagem será R${:.2f}'.format(v))   