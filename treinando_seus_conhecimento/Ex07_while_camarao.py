cardapio = ['frango a kiev',
            'filet',
            'bolinho de bacalhau',
            'batata frita',
            'camarão',
            'costela ao molho barbecue']

item = cardapio.pop(0)

while item != 'camarão':
    print('Esse item não é camarão! cade meu camarão? ')
    item = cardapio.pop(0)

