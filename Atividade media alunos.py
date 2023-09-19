nota_01 = float(input())
nota_02 = float(input())
nota_03 = float(input())
media = (nota_01 + nota_02 + nota_03)/3
if nota_03 > 8:
    media += 1
if media > 10:
    media = 10
print(f'{media:.2f}')










