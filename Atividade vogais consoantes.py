palavras = input()
vogais = 'aeiouAEIOU'
consoantes = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
numeros = '0123456789'
if palavras in vogais:
    print('vogal')
elif palavras in consoantes:
    print('consoante')
elif palavras in numeros:
    print('número')
else:
    print('símbolo')
    
