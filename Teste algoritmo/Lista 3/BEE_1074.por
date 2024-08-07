algoritmo verificacao
    escreva 'entre com o n'
    leia n

    para i = 1 ate n:
        escreva 'entre com o número'
        leia num
        se num == 0:
            escreva("NULL")
        senao:
            se num % 2 != 0:
                tipo = "odd"
            senao:
                tipo = "even"
            fim_se
            se num < 0:
                sinal = "negative"
            senao:
                sinal = "positive"
        fim_se
    fim_para

    escreva ' {tipo}, {sinal} '
fim_algoritmo