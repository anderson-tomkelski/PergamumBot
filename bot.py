from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass
import time

url = "http://consulta.uffs.edu.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php"
mat = input("Matricula: ")
pwd = getpass("Senha: ")

driver = webdriver.Firefox()
driver.get(url)
assert "UFFS" in driver.title
login = driver.find_element_by_name("login")
passwd = driver.find_element_by_name("password")
login.clear()
passwd.clear()

login.send_keys(mat)
passwd.send_keys(pwd)

driver.find_element_by_name("button").send_keys(Keys.RETURN)

time.sleep(2)

renovarBtns = driver.find_elements_by_class_name("btn_renovar");

#for btn in renovarBtns :
for i in range(len(renovarBtns)) :
    renovarBtns = driver.find_elements_by_class_name("btn_renovar");
    renovarBtns[i].send_keys(Keys.RETURN)
    #driver.find_element_by_name("botao_renovar"+str(i)).send_keys(Keys.RETURN)
    time.sleep(3)
    driver.execute_script("window.history.go(-1)")
    #driver.back()
    #driver.find_element_by_name("btn_gravar4").send_keys(Keys.RETURN)
    time.sleep(3)


#assert "No results found." not in driver.page_source
#driver.close()

