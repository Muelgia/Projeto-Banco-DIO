nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

nota1 = nota1 / 100 * 20
nota2 = nota2 / 100 * 30
nota3 = nota3 / 100 * 50
total = nota1 + nota2 + nota3

if total < 30:
    print('Reprovado')
elif total < 70:
    print('Exame final')
else: 
    print('Aprovado')
