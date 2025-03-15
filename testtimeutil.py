# statement coverage tester for timeutil
# 15 April 2022

'''
>>> import timeutil
>>> timeutil.validate(":23 p.m.")
False
>>> timeutil.validate("111:01 p.m.")
False
>>> timeutil.validate("01:1 a.m.")
False
>>> timeutil.validate("12:61 am")
False
>>> timeutil.validate("12:111 p.m.")
False
>>> timeutil.validate("12:59 a.m.")
True

'''

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)