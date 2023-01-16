from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
import pandas as pd

print('Running module Scraping')
driver = webdriver.Chrome()
driver.get("https://casadosdados.com.br/solucao/cnpj/q4d-solucoes-em-ti-ltda-05933010000101%27%27%27")

h_cnpj = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[1]/p[1]').get_attribute('innerHTML')
v_cnpj = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[1]/p[2]').get_attribute('innerHTML')

h_razao_social = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[2]/p[1]').get_attribute('innerHTML')
v_razao_social = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[2]/p[2]').get_attribute('innerHTML')

h_nome_fantasia = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[3]/p[1]').get_attribute('innerHTML')
v_nome_fantasia = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[3]/p[2]').get_attribute('innerHTML') 

h_tipo = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[4]/p[1]').get_attribute('innerHTML') 
v_tipo = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[4]/p[2]').get_attribute('innerHTML') 

h_data_abertura = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[5]/p').get_attribute('innerHTML') 
v_data_abertura = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[5]/a').get_attribute('innerHTML') 

h_situacao_cadastral = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[6]/p[1]').get_attribute('innerHTML') 
v_situacao_cadastral = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[6]/p[2]').get_attribute('innerHTML') 

h_data_da_situacao_cadastral = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[7]/p[1]').get_attribute('innerHTML') 
v_data_da_situacao_cadastral = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[7]/p[2]').get_attribute('innerHTML') 

h_capital_social = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[8]/p[1]').get_attribute('innerHTML') 
v_capital_social = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[8]/p[2]').get_attribute('innerHTML') 

h_natureza_juridica = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[9]/p[1]').get_attribute('innerHTML') 
v_natureza_juridica = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[9]/p[2]').get_attribute('innerHTML') 

h_empresa_mei = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[10]/p[1]').get_attribute('innerHTML') 
v_empresa_mei = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[1]/div[10]/p[2]').get_attribute('innerHTML') 

h_logradouro = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[1]/p[1]').get_attribute('innerHTML') 
v_logradouro = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[1]/p[2]').get_attribute('innerHTML') 

h_numero = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[2]/p[1]').get_attribute('innerHTML') 
v_numero = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[2]/p[2]').get_attribute('innerHTML') 

h_complemento = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[3]/p[1]').get_attribute('innerHTML') 
v_complemento = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[3]/p[2]').get_attribute('innerHTML') 

h_cep = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[4]/p[1]').get_attribute('innerHTML') 
v_cep = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[4]/p[2]').get_attribute('innerHTML') 

h_bairro = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[5]/p[1]').get_attribute('innerHTML') 
v_bairro = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[2]/div[5]/p[2]').get_attribute('innerHTML') 

h_telefone = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[3]/div[1]/p[1]').get_attribute('innerHTML') 
v_telefone = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[3]/div[1]/p[2]/a').get_attribute('innerHTML') 

h_email = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[3]/div[2]/p[1]').get_attribute('innerHTML') 
v_email = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[4]/div[1]/div[3]/div[2]/p[2]/a').get_attribute('innerHTML') 

h_atividade_principal = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[5]/div[1]/p[1]').get_attribute('innerHTML') 
v_atividade_principal = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[5]/div[1]/p[2]').get_attribute('innerHTML') 

h_data_da_consulta = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[5]/div[3]/p[1]').get_attribute('innerHTML') 
v_data_da_consulta = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/section[1]/div/div/div[5]/div[3]/p[2]').get_attribute('innerHTML') 


info_q4d = [ 
    {
        h_cnpj: v_cnpj,
        h_razao_social: v_razao_social,
        h_nome_fantasia: v_nome_fantasia,
        h_tipo: v_tipo,
        h_data_abertura: v_data_abertura,
        h_situacao_cadastral: v_situacao_cadastral,
        h_data_da_situacao_cadastral: v_data_da_situacao_cadastral,
        h_capital_social: v_capital_social,
        h_natureza_juridica: v_natureza_juridica,
        h_empresa_mei: v_empresa_mei,
        h_logradouro: v_logradouro,
        h_numero: v_numero,
        h_complemento: v_complemento,
        h_cep: v_cep,
        h_bairro: v_bairro,
        h_telefone: v_telefone,
        h_email: v_email,
        h_atividade_principal: v_atividade_principal,
        h_data_da_consulta: v_data_da_consulta,
    }
]

# template
pd.DataFrame(data=info_q4d).to_excel(r'info_q4d.xlsx', index=False)