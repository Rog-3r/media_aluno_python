aluno = input('Insira o nome do aluno: ')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
faltas = int(input('total de faltas do aluno: '))

media = (nota1 + nota2)/2
aulas = (20 - faltas)/20


if media > 6 and aulas >= 0.7:
    print ('Aluno,',aluno,'com média',media,'e com',aulas,'porcentagem de faltas está, aprovado')

elif media < 6 and aulas >= 0.7:
    print ('Aluno,',aluno,'com média',media,'e com',aulas,'porcentagem de faltas está, reprovado por média')

elif media > 6 and aulas < 0.7:
    print ('Aluno,',aluno,'com média',media,'e com',aulas,'porcentagem de faltas está reprovado por faltas')

elif media < 6 and aulas < 0.7:
    print ('Aluno,',aluno,'com média',media,'e com',aulas,'porcentagem de faltas está reprovado por faltas e por média')

else:
    print ('ERROR')

