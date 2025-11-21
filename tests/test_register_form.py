import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterForm:
    @pytest.fixture(scope="function")
    def setup(self):
        options = webdriver.ChromeOptions()
        
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--headless")
        
        print("Iniciando o Chrome diretamente (método que funcionou no teste)...")
        try:
            driver = webdriver.Chrome(options=options)
            print("Chrome iniciado com sucesso")
        except Exception as e:
            print(f"Erro ao iniciar o Chrome: {e}")
            pytest.fail(f"Não foi possível iniciar o ChromeDriver: {e}")
            
        driver.maximize_window()
        driver.get("http://localhost:5173/register")  
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "form"))
        )
        
        yield driver
        # Fecha o navegador após o teste
        driver.quit()
    
    def preencher_formulario(self, driver, nome="Teste", sobrenome="Usuário", 
                           telefone="(75) 55544-4444", cpf="210.830.180-19", 
                           email="teste@teste.com.br", confirmar_email="teste@teste.com.br",
                           senha="Teste123@", confirmar_senha="Teste123@"):
        """Função auxiliar para preencher o formulário"""
        driver.find_element(By.NAME, "nome").send_keys(nome)
        driver.find_element(By.NAME, "sobrenome").send_keys(sobrenome)
        driver.find_element(By.NAME, "telefone").send_keys(telefone)
        driver.find_element(By.NAME, "cpf").send_keys(cpf)
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "confirmarEmail").send_keys(confirmar_email)
        driver.find_element(By.NAME, "senha").send_keys(senha)
        driver.find_element(By.NAME, "confirmarSenha").send_keys(confirmar_senha)
    
    def verificar_botao_habilitado(self, driver):
        """Verifica se o botão de cadastro está habilitado"""
        botao = driver.find_element(By.XPATH, "//button[@type='submit']")
        return not botao.get_attribute("disabled")
    
    def verificar_mensagem_erro(self, driver, campo):
        """Verifica se há mensagem de erro para um campo específico"""
        try:
            error_element = driver.find_element(By.XPATH, f"//input[@name='{campo}']/following-sibling::div[contains(@class, 'invalid-feedback')]")
            return error_element.is_displayed()
        except:
            return False

    # Teste 0: Tamanho mínimo da senha
    def test_tamanho_minimo_senha_valido(self, setup):
        """Teste para validar que uma senha com 8 caracteres é válida"""
        driver = setup
        self.preencher_formulario(driver, senha="Teste123@", confirmar_senha="Teste123@")
        time.sleep(1)  
        assert self.verificar_botao_habilitado(driver)
    
    def test_tamanho_minimo_senha_invalido(self, setup):
        """Teste para validar que uma senha com menos de 8 caracteres é inválida"""
        driver = setup
        self.preencher_formulario(driver, senha="1a@", confirmar_senha="1a@")
        assert not self.verificar_botao_habilitado(driver)
    
    # Teste 1: Validação do Telefone
    def test_telefone_valido(self, setup):
        """Teste para validar formato de telefone correto"""
        driver = setup
        self.preencher_formulario(driver, telefone="(11) 91234-5678")
        time.sleep(1)  
        assert self.verificar_botao_habilitado(driver)
    
    def test_telefone_invalido(self, setup):
        """Teste para validar formato de telefone incorreto"""
        driver = setup
        self.preencher_formulario(driver, telefone="(11) 1234-5678")  
        time.sleep(1)  
        assert not self.verificar_botao_habilitado(driver)
    
    # Teste 2: Validação do CPF
    def test_cpf_valido(self, setup):
        """Teste para validar CPF válido"""
        driver = setup
        self.preencher_formulario(driver, cpf="123.456.789-09")  
        time.sleep(1)  
        assert self.verificar_botao_habilitado(driver)
    
    def test_cpf_invalido(self, setup):
        """Teste para validar CPF inválido"""
        driver = setup
        self.preencher_formulario(driver, cpf="123.456.789-00")  
        time.sleep(1)  
        assert not self.verificar_botao_habilitado(driver)
    
    # Teste 3: Validação do Email
    def test_email_valido(self, setup):
        """Teste para validar email com formato correto"""
        driver = setup
        self.preencher_formulario(driver, email="teste@exemplo.com", confirmar_email="teste@exemplo.com")
        time.sleep(1)  
        assert self.verificar_botao_habilitado(driver)
    
    def test_email_invalido(self, setup):
        """Teste para validar email com formato incorreto"""
        driver = setup
        self.preencher_formulario(driver, email="teste@exemplo@com", confirmar_email="teste@exemplo@com")
        assert not self.verificar_botao_habilitado(driver)
    
    # Teste 4: Double Check do Email e Senha
    def test_double_check_email_senha_valido(self, setup):
        """Teste para validar se o email e a senha coincidem"""
        driver = setup
        self.preencher_formulario(
            driver, 
            email="teste@exemplo.com", 
            confirmar_email="teste@exemplo.com", 
            senha="Senha123@", 
            confirmar_senha="Senha123@"
        )
        assert self.verificar_botao_habilitado(driver)
    
    def test_double_check_email_senha_invalido(self, setup):
        """Teste para validar se o email e a senha não coincidem"""
        driver = setup
        self.preencher_formulario(
            driver, 
            email="teste@exemplo.com", 
            confirmar_email="teste@exemplo.com", 
            senha="Senha123@", 
            confirmar_senha="Senha456@"
        )
        assert not self.verificar_botao_habilitado(driver)
    
    # Teste 5: Sucesso - Preenchimento completo com dados válidos
    def test_formulario_sucesso(self, setup):
        """Teste para validar o preenchimento correto de todos os campos"""
        driver = setup
        self.preencher_formulario(
            driver,
            nome="Teste",
            sobrenome="Completo",
            telefone="(75) 55544-4444",
            cpf="210.830.180-19",
            email="teste@teste.com.br",
            confirmar_email="teste@teste.com.br",
            senha="Teste123@",
            confirmar_senha="Teste123@"
        )
        time.sleep(1)  
        
        assert self.verificar_botao_habilitado(driver)
        botao = driver.find_element(By.XPATH, "//button[@type='submit']")
        botao.click()
        
        time.sleep(2)
        
