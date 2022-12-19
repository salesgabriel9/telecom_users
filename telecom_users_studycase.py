#!/usr/bin/env python
# coding: utf-8

# # Análise de dados com Python
# 
# ### Desafio: 
# 
# 
# Trabalhar em uma empresa de telecom que possui clientes com vários tipos de serviços diferentes, entre os principais: internet e telefone.
# 
# Ao analisar o histórico de clientes dos últimos anos, notou-se que a empresa tem uma taxa de cancelamento (Churn) de mais de 26% dos clientes.
# 
# Isso representa uma perda de bilhões para empresa.
# 
# O que a empresa pode fazer para resolver isso?

# In[1]:


# Passo 1: Importando a base de dados
import pandas as pd

telecom_users = pd.read_csv('telecom_users.csv')

# Passo 2: Visualizando a base de dados
# - Entender quais informações dos usuários encontram-se disponíveis
# - Corrigir erros da base de dado
display(telecom_users)


# In[2]:


telecom_users = telecom_users.drop('Unnamed: 0', axis=1)
display(telecom_users)
# remover coluna 'Unnamed: 0' do dataframe por serem informações sem utilidade, axis=0(linha), axis=1(coluna).


# In[3]:


# Passo 3: Tratando os dados
# - Valores que estão reconhecidos de forma errada
telecom_users.info()


# In[4]:


#corrigir valor reconhecido de forma errada da coluna 'TotalGasto' de 'object'(texto) para 'float64'(número decimal)
telecom_users['TotalGasto'] = pd.to_numeric(telecom_users['TotalGasto'], errors='coerce')
# pd.to_numeric é uma função do pacote pandas no Python que corrige o valor da coluna ['TotalGasto'] em um valor numérico
# errors='coerce' deleta os valores que não sejam numéricos e previne um possível erro de código

telecom_users.info()


# In[5]:


# - Valores vazios
# deletando as colunas vazias
telecom_users = telecom_users.dropna(how='all', axis=1)
# dropna deleta valores vazios (NaN) / how='all' apenas informações que tenham todos os valores vazios [Codigo] / axis=1 _> coluna

# deletando as linhas vazias
telecom_users = telecom_users.dropna(how='any', axis=0)
# dropna deleta valores vazios (NaN) / how='any' apenas informações que tenham pelo menos um valor vazio [TotalGasto] / axis=0 _> linha

telecom_users.info()
# 12 linhas e uma coluna com valores nulos(NaN) foram removidos


# In[6]:


# Passo 4: Análise Inicial
# Como estão nossos cancelamentos?

display(telecom_users['Churn'].value_counts())
#contar os valores da coluna de cancelamentos 'Churn'
display(telecom_users['Churn'].value_counts(normalize=True))
#contar os valores da coluna de cancelamentos 'Churn' e calcular o percentual


# In[29]:


# Passo 5: Análise mais completa
# comparar cada coluna da minha tabela com a coluna de cancelamento
import plotly.express as px

# etapa 1: criar o gráfico

coluna = 'MesesComoCliente'
# definindo a variavel das colunas
for coluna in telecom_users.columns:
# para cada coluna dentro das colunas do meu dataframe:
    grafico = px.histogram(telecom_users, x=coluna, color='Churn')
    # criar um gráfico histograma comparando cada coluna do dataframe 'telecom_users' com a coluna 'Churn' _> cancelamentos


# etapa 2: exibir o gráfico
    grafico.show()


# In[24]:


get_ipython().system('pip install plotly')
# instalação do pacote plotly para visualização dos gráficos


# ### Conclusões e Ações

# - Analisando os gráficos 'Casado' e 'Dependentes' é possivel notar que clientes que NÃO são casados e NÃO possuem dependentes  tem uma taxa de cancelamento bem maior em comparação a clientes casados ou que já possuam dependentes 
#     - Podemos fazer ações de marketing pra novos clientes que fizerem o plano junto de um amigo ou familiar
#     
#     
#     
# -  Analisando o gráfico  'MesesComoCliente' nota-se que os três primeiros meses de contrato são grandes responsáveis pela alta taxa de cancelamento dos clientes
#     - Podemos fazer promoções para clientes que assinarem o contrato anual, dar desconto em um telefone novo em troca da fidelidade ou  um desconto na mensalidade do plano em troca de 1 ou 2 anos de fidelidade. Por ultimo, priorizar o serviço de suporte a novos clientes.
#     
#     
# 
# - Analisando o gráfico 'ServicoInternet' pode-se notar que existe alguma coisa no serviço de Fibra que está  fazendo grande parte dos novos clientes clientes
#     - Entender por que os clientes estão cancelando o serviço de Fibra, agir em cima do problema e solucionar
# 
# 
# 
# - Analisando os gráficos de serviço ao cliente é possivel notar que clientes que quanto mais serviços o cliente tem, menor a taxa de cancelamento
#     - Podemos fazer promoções que incluam mais serviços ao cliente como bônus
#     
#     
#     
# - Analisando o gráfico 'TipoContrato' nota-se que clientes com contrato mensal tem MUITO mais chance de cancelar:
#     - Podemos fazer promoções para o cliente ir para o contrato anual
# 
# 
# 
# - Clientes no boleto tem MUITO mais chance de cancelar
#     - Temos que fazer alguma ação para eles irem para as outras formas de pagamento
