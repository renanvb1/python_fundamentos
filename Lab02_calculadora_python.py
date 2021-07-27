#!/usr/bin/env python
# coding: utf-8

# ## Tentativa de implementar a calculadora em Python

# In[6]:


# imprimindo as mensagens iniciais na tela
print('************************ Python Calculator ************************\n\n')
print('Select the adequate flag according to the desired operation: \n \n')
print(' + -> Sum \n - -> Subtraction \n * -> Multiplication \n / -> Division \n ** -> Power \n % -> Mod \n \n')

# lendo o flag da operacao
flag=input ('Type in your option (+, - , *, /, **, %): \n')

# enquanto o flag selecionado nao for uma opcao valida, informar ao usuario e perguntar novamente
while flag != '+' and flag != '-' and flag != '/' and flag != '*' and flag != '**' and flag != '%':
    print('\nInvalid operation! \n')
    flag=input ('Type in your option (+, - , *, /, **, %): \n')

# lendo o primeiro numero
n1=float(input ('\nType in the first number: \n'))
# lendo o segundo numero
n2=float(input ('Type in the second number: \n'))

# calculando o valor de ans de acordo com a opcao desejada
if flag == '+':
    ans = n1 + n2
elif flag == '-':
    ans = n1 - n2
elif flag == '*':
    ans = n1 * n2
elif flag == '/':
    ans = n1 / n2
elif flag == '**':
    ans = n1 ** n2
elif flag == '%':
    ans = n1 % n2

# imprimindo na tela a resposta
print('%r %s %r = %r' %(n1, flag, n2, ans) )


# In[ ]:




