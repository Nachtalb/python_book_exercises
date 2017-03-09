def bewege(n, von, nach, ueber):
    if (n == 1):
        print('Lege eine Scheibe von', von, 'nach', nach, '.')
    else:
        bewege(n - 1, von, ueber, nach)
        bewege(1, von, nach, ueber)
        bewege(n - 1, ueber, nach, von)


bewege(10, 1, 3, 2)
