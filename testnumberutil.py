# creating a path coverage checker
# 14 April 2022

'''
>>> import numberutil
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(1)
'one'
>>> numberutil.aswords(30)
'thirty'
>>> numberutil.aswords(31)
'thirty one'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(120)
'one hundred and twenty'
>>> numberutil.aswords(130)
'one hundred and thirty'
>>> numberutil.aswords(131)
'one hundred and thirty one'


'''

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
