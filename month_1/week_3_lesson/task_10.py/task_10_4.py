#Nigerian Currency Converter 

try:
    #Collect user input
    currency = input('Which currency do you want to convert: Choose 1 for dollars and 2 for GBP: ')
    

    #Set exchange rates
    exchange_rate_usd = 1500
    exchange_rate_gbp = 1900



    #Display
    if currency == '1':
        amount = float(input('Enter amount in NGN: '))
        title = 'Nigerian Currency Converter(Naira - USD)'
        amount_usd = (amount/exchange_rate_usd)
        print(f'\n{title:^50}')
        print(f'amount($): {amount_usd:>40.2f}')
    elif currency == '2':
        amount = float(input('Enter amount in NGN: '))
        title = 'Nigerian Currency Converter(Naira - GBP)'
        amount_gbp = amount/exchange_rate_gbp
        print(f'{title:^50}')
        print(f'amount(£): {amount_gbp:>40.2f}')
    else:
        raise ValueError('Choose from available options')

except ValueError as e:
    print('Error: ', e)
except TypeError as e:
    print('Error', e)
finally:
    print('Thanks for using our app')