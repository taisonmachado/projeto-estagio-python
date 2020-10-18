from selenium import webdriver

class Acess():
    
    def __init__(self, url):
        
        #Carrega o driver e acessa a url passada no construtor.
        try:
            driver = webdriver.Chrome()
            driver.get(url)
        except Exception as erro:
            print(str(erro) + 'Erro ao carregar o driver')


        #Localiza a matéria em destaque na página e executa uma ação de click nele.
        element = driver.find_element_by_class_name('destaque')
        element.click()

        driver.get(driver.current_url)

        #Localiza os elementos de título e conteúdo da matéria e recupera seus textos. 
        self.title = driver.find_element_by_class_name('titulo').text
        self.content = driver.find_element_by_id('tamanhotexto').text
        driver.close()
        