#Importações necessárias
import matplotlib.pyplot

#Dados que colocaremos no grafico
meses2020 = ['jan', 'fev', 'mar']
dados2020 = [999, 5000, 500 ]
meses2021 = ['jan', 'fev', 'mar']
dados2021 = [1000, 11006, 0 ]
meses2022 = ['jan', 'fev', 'mar']
dados2022 = [500, 1500, 500 ]

#Plotando os dados no grafico
#Linha normal
matplotlib.pyplot.plot(meses2020, dados2020, color='pink')
#k: Linha pontilhada
matplotlib.pyplot.plot(meses2021, dados2021,'k:', color='blue')
#k--: Linha tracejada
matplotlib.pyplot.plot(meses2022, dados2022,'k--', color='yellow')

#Lista que irá para a legenda
#Deve ser colocado na mesma ordem
anos = [2020, 2021, 2022]
#Criando a caixa de legenda externa(lista de nomes, titulo, localização)
matplotlib.pyplot.legend(anos, title="Anos", loc="center left")

#Definindo limites para a coluna y
#Ps: só valores positivos
matplotlib.pyplot.ylim(0, 12000)

#Titulo
matplotlib.pyplot.title('Graficos de teste')

#Nome da x
matplotlib.pyplot.xlabel('Meses')
#Nome da y
matplotlib.pyplot.ylabel('Número')

matplotlib.pyplot.show()
