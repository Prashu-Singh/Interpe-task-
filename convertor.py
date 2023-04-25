dict={
    'Argentine Peso':2.687574,
   'Australian Dollar':0.018279,		
    'British Pound':0.009779,	
    'Canadian Dollar':0.016537,	
    'Euro':0.011043,
    'Hong Kong Dollar':0.095791,		
    'Indonesian Rupiah':182.389368,	
    'Japanese Yen':1.638748,	
   'Mexican Peso':0.219701,	
    'New Zealand Dollar':0.019784,	
    'Pakistani Rupee':3.409383,	
    'Philippine Peso':0.678539,	
    'Russian Ruble':0.991806,
    'Saudi Arabian Riyal':0.045763,	
    'Singapore Dollar':0.016287,	
    'South African Rand	':0.221882,	
    'South Korean Won':16.309478,	
    'Sri Lankan Rupee':3.916584,	
    'Swedish Krona':0.125139,
    'Taiwan New Dollar':0.374605,	
    'Trinidadian Dollar':0.082698,		
    'US Dollar':0.012204,
}
print("----------------------------------------------------------------------")
print()
amount = int(input("Enter amount to convertor:\t"))
print()
print("Choose the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in dict.keys()]
print()
currency = input("Please enter the choosen values here : \t")
print()
print(f"{amount} INR is equal to {amount *float(dict[currency])} {currency}")
print()
print("----------------------------------------------------------------------")
