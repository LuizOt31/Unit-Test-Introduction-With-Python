def Eh_primo(a):
    if a < 2:
        return False
    for i in range(2, int(a/2)):
        if a%i == 0:
            return False
    return True
