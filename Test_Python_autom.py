from selenium import webdriver
navegador = webdriver.Chrome()
navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a/p').click()

navegador.find_element_by_xpath('//*[@id="bWtQ7n6RcQdDDDCgCcH3yg=="]').click()
