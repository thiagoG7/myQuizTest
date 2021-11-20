from time import sleep

nome = input('Digite seu nome: ') 
if nome.lower():
    print ('Olá, ' + nome + ' tudo bem? ')

while True:
    pergunta = input('Deseja jogar um jogo? ')
    if pergunta.lower() == 'sim':
        print ('Vamos lá.')
        sleep (1)
    else:
        exit ()
    
    score = 0

    answer = input(nome + ', o que é CPU? ')
    if answer.lower() == 'processador':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    elif answer.lower() == 'central processing unit':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else:
        sleep (1)
        print ('Você errou.')
        
    answer = input(nome + ', o que é GPU? ')
    if answer.lower() == 'placa de vídeo':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    elif answer.lower() == 'graphics processing unit':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else:
        sleep (1)
        print ('Você errou.')

    answer = input(nome + ', o que é PSU? ')
    if answer.lower() == 'fonte':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    elif answer.lower() == 'power supply unit':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else:
        sleep (1)
        print ('Você errou')

    answer = input(nome + ', qual o tipo de leitura da memória ROM? ')
    if answer.lower() == 'texto':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else:
        sleep (1)
        print ('Você errou.')

    answer = input(nome + ', o que é HD? ')
    if answer.lower() == 'disco rígido':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    elif answer.lower() == 'hard disk':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    elif answer.lower() == 'hard disk driver':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else:
        sleep (1)
        print ('Você errou.')

    answer = input(nome + ', o que é MOBO? ')
    if answer.lower() == 'placa mãe':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    elif answer.lower() == 'motherboard':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else:
        sleep (1)
        print ('Você errou.')

    answer = input(nome + ', a memória RAM é temporária ou permanente? ')
    if answer.lower() == 'temporária':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else: 
        sleep (1)
        print ('Você errou.')

    answer = input(nome + ', o que é SSD? ')
    if answer.lower() == 'solid state drives':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    elif answer.lower() == 'unidade em estado sólido':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else:
        sleep (1)
        print ('VocÊ errou.')
    
    answer = input(nome + ', qual nome do chipset que faz o controle dos componentes rápidos? ')
    if answer.lower() == 'ponte norte':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    elif answer.lower() == 'northbridge':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else:
        sleep (1)
        print ('Você errou')

    answer = input(nome + ', qual nome do chipset que faz o controle dos componentes lentos? ')
    if answer.lower() == 'ponte sul':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    elif answer.lower() == 'southbridge':
        sleep (1)
        print ('Certa resposta! ')
        score += 1
    else:
        sleep (1)
        print ('Você errou.')
    print ('Você chegou no final, ' + nome + '. Vamos ver quantas questões você acertou.')
    sleep (1)
    print ('Você acertou ' + str(score) + ' questões.')
    sleep (1)
    print ('Uma porcentagem de acerto de ' + str((score/10) * 100) + '%.')


    if score <= 0:
        print ('Se esforçe mais, ' + nome + '.')
    elif score <= 2:
        print ('Não desanime, continue tentando, ' + nome + '.')
    elif score <= 3:
        print ('Você precisa estudar mais, ' + nome + '.')
    elif score <= 6:
        print ('Bom desempenho, ' + nome + '.')
    elif score <= 8:
        print ('Muito bem, ' + nome + '.')
    elif score <= 10:
        print ('UAU, belo desempenho, ' + nome + '.')
    exit()
