def maior_primo(n):
    aux = n
    while aux > 2:
        if eh_primo(aux):
            return aux
        aux -= 1
    return 2

def eh_primo(k):
    i = 2
    while i * i <= k:
        if k % i == 0:
            return False
        i += 1
    return True

print('Maior primo ate 8: ' + str(maior_primo(8)))
print('Maior primo ate 7: ' + str(maior_primo(7)))
print('Maior primo ate 100: ' + str(maior_primo(100)))
print('Maior primo ate 60: ' + str(maior_primo(60)))
print('Maior primo ate 61: ' + str(maior_primo(61)))
print('Maior primo ate 3: ' + str(maior_primo(3)))
print('Maior primo ate 2: ' + str(maior_primo(2)))
print('Maior primo ate 1: ' + str(maior_primo(1)))
print('Maior primo ate 0: ' + str(maior_primo(0)))