# -*- coding: utf-8 -*-
# Universidade Federal do Acre
# Disciplina: Linguagem de Programação 1
# Gustavo Bezerra de Souza

# -*- coding: utf-8 -*-

def calcular_duracao_jogo(h_inicio, m_inicio, h_fim, m_fim):
    inicio_total_minutos = h_inicio * 60 + m_inicio
    fim_total_minutos = h_fim * 60 + m_fim
    
    if fim_total_minutos <= inicio_total_minutos:
        duracao_minutos = (24 * 60 - inicio_total_minutos) + fim_total_minutos
    else:
        duracao_minutos = fim_total_minutos - inicio_total_minutos
    
    duracao_horas = duracao_minutos // 60
    duracao_minutos = duracao_minutos % 60
    
    print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")

# Entrada de dados
h_inicio, m_inicio, h_fim, m_fim = map(int, input().split())

# Processamento e saída de dados
calcular_duracao_jogo(h_inicio, m_inicio, h_fim, m_fim)
