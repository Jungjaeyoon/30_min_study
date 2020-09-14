# try/finally
# finally runs allways after try

try:
    print(data)
except:
    pass
finally:
    print('data closed')


