salario = float(input('Digite seu salário: '))
if salario < 8500:
    print('Financiamento recusado, salário inferior ao valor mínimo!')
else:
    emprestimos = float(input('Digite seu total de emprestimos:'))
    minimo = salario / 100 * 20
    if emprestimos > minimo:
        print('Recusado pois o valor dos empréstimos ultrapassa 20% da renda')
    else:
        print('Financiamento aprovado')