#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[4]:


import pandas as pd
import numpy as np


# In[5]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[6]:


black_friday.head()
exploracao = pd.DataFrame({'colunas': black_friday.columns, 
                           'tipos': black_friday.dtypes, 
                           'percentual_Faltante': black_friday.isna().sum()/black_friday.shape[0]})
exploracao


# In[7]:


black_friday.shape


# In[8]:


black_friday.info()


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[11]:


def q1():
    # Retorne aqui o resultado da questão 1.
    return black_friday.shape
    pass


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[13]:


def q2():
    # Retorne aqui o resultado da questão 2.
    return black_friday.groupby(['Gender','Age']).count().loc['F', '26-35']['User_ID']
    pass


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[14]:


def q3():
    # Retorne aqui o resultado da questão 3.
    return black_friday['User_ID'].nunique()
    pass


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[15]:


def q4():
    # Retorne aqui o resultado da questão 4.
    return black_friday.dtypes.nunique()
    pass


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[16]:


def q5():
    # Retorne aqui o resultado da questão 5.
    soma = 0
    for row in black_friday.isna().sum(axis=1):
        if row > 1:
            soma += 1
        else:
            soma += row

    return soma / black_friday.shape[0]   
    pass


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[17]:


def q6():
    # Retorne aqui o resultado da questão 6.
    return black_friday.isna().sum().max()
    pass


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[18]:


def q7():
    # Retorne aqui o resultado da questão 7.
    return black_friday['Product_Category_3'].mode()[0]
    pass


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[19]:


def q8():
    # Retorne aqui o resultado da questão 8.
    pMin = black_friday['Purchase'].min()
    pMax = black_friday['Purchase'].max()
    df_normalizado = pd.DataFrame([(i-pMin)/(pMax - pMin) for i in black_friday['Purchase']])
    return df_normalizado.mean()[0]
    pass


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[20]:


def q9():
    # Retorne aqui o resultado da questão 9.
    std = black_friday['Purchase'].std()
    mean = black_friday['Purchase'].mean()
    df_padronizado = pd.DataFrame([(i-mean)/std for i in black_friday['Purchase']])
    return pd.DataFrame([i for i in df_padronizado[0] if i<= 1 and i>= -1]).shape[0]
    pass


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[21]:


def q10():
    # Retorne aqui o resultado da questão 10.
    prodCat2 = black_friday['Product_Category_2'].isna()
    prodCat3 = black_friday['Product_Category_3'].isna()
    question = True
    for i,j in zip(prodCat2, prodCat3):
        if i:
            if not j:
                question = False
                break
    return question
    pass

