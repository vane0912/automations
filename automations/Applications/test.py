def test(test1):
    variables = {
        'Url' : ''
    }
    for x in test1:
        if x['type'] == 'Url':
            variables['Url'] = x['value']
    print(variables['Url'])
