# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import scipy.stats as stats
from sklearn.linear_model import LinearRegression

pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 200)
pd.set_option('max_info_columns', 300)
#############################################
# Importando e limpando o dataset de treino #
#############################################
table = pd.read_csv('train.csv')

# Eliminando as linhas das pessoas que não participaram ou foram eliminadas do enem
table.dropna(subset=['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT'], how='any',inplace=True)

# Salvando uma série com as notas de matematica que será usado para treinar o algoritmo
Y_MT = table['NU_NOTA_MT']

X = table.drop(['NU_NOTA_MT', 'TX_RESPOSTAS_CN', 'TX_RESPOSTAS_CH', 'TX_RESPOSTAS_LC', 'TX_RESPOSTAS_MT',
                'TX_GABARITO_CN', 'TX_GABARITO_CH', 'TX_GABARITO_LC', 'TX_GABARITO_MT'], axis=1)

mapper = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10,  'K':11,  'L':12,  'M':13,  'N':14,
          'O':15,  'P':16, 'Q':17}

# For para converter as colunas do tipo object em números e convertendo elas para o tipo númérico
for i in range(50):
    if X[X.columns[108+i]].dtype == 'object':
        X[X.columns[108 + i]] = X[X.columns[108 + i]].map(mapper)
        pd.to_numeric(X[X.columns[108+i]], errors='coerce')

X['TP_SEXO'] = X['TP_SEXO'].map({'M': 1, 'F': 2})
pd.to_numeric(X['TP_SEXO'], errors='coerce')

X.fillna(0, inplace=True)
X.reset_index()

X = X.drop(['Unnamed: 0', 'NU_INSCRICAO', 'NU_ANO', 'SG_UF_RESIDENCIA', 'NO_MUNICIPIO_NASCIMENTO', 'SG_UF_NASCIMENTO',
        'NO_MUNICIPIO_ESC', 'SG_UF_ESC', 'NO_ENTIDADE_CERTIFICACAO', 'SG_UF_ENTIDADE_CERTIFICACAO', 'SG_UF_PROVA',
        'NO_MUNICIPIO_RESIDENCIA', 'NO_MUNICIPIO_PROVA', 'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC', 'CO_PROVA_MT'], axis=1)

# Instanciando a classe LinearRegression
lm = LinearRegression()

'''
#lm.fit(X, Y_MT)
#mt = lm.predict(X)

#print(pd.DataFrame(zip(X.columns, lm.coef_), columns=['features', 'estimatedCoefficients']))

#mseFull = np.mean((Y_MT - mt) ** 2)
#print(mseFull)

#pred = pd.DataFrame(zip(lm.predict(X), Y_MT))
#print(pred)
'''

############################################
# Importando e limpando o dataset de teste #
############################################
table_test = pd.read_csv('test.csv')

X_test = table_test.drop(['NU_INSCRICAO','SG_UF_RESIDENCIA', 'CO_PROVA_CN', 'CO_PROVA_CH', 'CO_PROVA_LC',
                          'CO_PROVA_MT', 'TP_PRESENCA_CN', 'TP_PRESENCA_CH', 'TP_PRESENCA_LC'], axis=1)
X_test['TP_SEXO'] = X_test['TP_SEXO'].map({'M': 1, 'F': 2})
pd.to_numeric(X_test['TP_SEXO'], errors='coerce')

for i in ['Q001', 'Q002', 'Q006', 'Q024', 'Q025', 'Q026', 'Q027', 'Q047']:
    if X_test[i].dtype == 'object':
        X_test[i] = X_test[i].map(mapper)
        pd.to_numeric(X_test[i], errors='coerce')
X_test.fillna(0, inplace=True)

X_test = X_test.drop(['TP_ENSINO'], axis=1)
print(X_test.columns)
print(X_test.info())

# Selecionando as mesmas colunas que o dataset de teste possuo
X = X[X_test.columns]

lm.fit(X, Y_MT)

mt = lm.predict(X)
print(pd.DataFrame(zip(X.columns, lm.coef_), columns=['features', 'estimatedCoefficients']))
mseFull = np.mean((Y_MT - mt) ** 2)
print()
print(mseFull)
#pred = pd.DataFrame(zip(lm.predict(X), Y_MT))
#print(pred)



#lm.fit(X, Y_MT)
#mt = lm.predict(X_test)

#answer = pd.DataFrame(zip(table_test['NU_INSCRICAO'], mt), columns=['NU_INSCRICAO', 'NU_NOTA_MT'])
#print(answer)
#answer.to_csv('answer.csv', index=False)
