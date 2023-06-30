



''' assigning value to variables'''
priceLexusES = 200
priceLexusLS = 300
VAT = 23
Discount = 0.1
'''Putting all calculation into one variable'''
finalPrice = (1 + VAT/100) * (1 - Discount)
'''Using assigned variables to receive final output'''
costOfLexusES = priceLexusES * finalPrice
costOfLexusLS = priceLexusLS * finalPrice
