#!/usr/bin/env python
"""
Script para executar os testes de automação com Selenium e PyTest.
"""
import os
import subprocess
import sys
import time
import webbrowser

def verificar_dependencias():
    """Verifica se as dependências estão instaladas."""
    try:
        import selenium
        import pytest
        from webdriver_manager.chrome import ChromeDriverManager
        print("Todas as dependências estão instaladas.")
        return True
    except ImportError as e:
        print(f"Dependência faltando: {e}")
        print("Instalando dependências...")
        subprocess.call([sys.executable, "-m", "pip", "install", "selenium", "pytest", "webdriver-manager", "pytest-html"])
        print("Dependências instaladas. Execute o script novamente.")
        return False

def verificar_aplicacao_rodando():
    """Verifica se a aplicação React está rodando."""
    import time
    
    # Priorizar o método HTTP, que é mais confiável para este caso específico
    print("Verificando se a aplicação está rodando via HTTP...")
    try:
        import urllib.request
        response = urllib.request.urlopen('http://localhost:5173', timeout=3)
        if response.getcode() == 200:
            print("✅ Aplicação detectada via HTTP")
            return True
    except Exception as e:
        print(f"Falha na verificação HTTP: {e}")
    
    # Se HTTP falhar, tenta verificar via socket como fallback
    print("Tentando verificar via socket...")
    import socket
    for _ in range(2):  # Tenta 2 vezes
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)  # Timeout de 2 segundos
            result = sock.connect_ex(('localhost', 5173))
            sock.close()
            
            if result == 0:
                print("✅ Aplicação detectada via socket")
                return True
                
            print(f"Tentativa de conexão socket falhou com código {result}")
            time.sleep(1)
        except Exception as e:
            print(f"Erro ao verificar aplicação via socket: {e}")
            time.sleep(1)
    
    return False

def main():
    """Função principal que executa os testes."""
    if not verificar_dependencias():
        return
    
    # Obtém o caminho base do projeto (onde está este script)
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    if not verificar_aplicacao_rodando():
        print("A aplicação não está rodando em http://localhost:5173")
        print("Execute 'npm run dev' na pasta CRUD antes de executar os testes.")
        print("Deseja tentar iniciar a aplicação automaticamente? (s/n)")
        resposta = input().lower()
        
        if resposta == 's':
            print("Iniciando a aplicação...")
            # Tenta iniciar a aplicação em segundo plano
            try:
                crud_path = os.path.join(base_path, 'CRUD')
                print(f"Tentando acessar o diretório: {crud_path}")
                
                if not os.path.exists(crud_path):
                    print(f"Erro: O diretório {crud_path} não existe!")
                    return
                    
                os.chdir(crud_path)
                subprocess.Popen(["npm", "run", "dev"], 
                                stdout=subprocess.DEVNULL, 
                                stderr=subprocess.DEVNULL)
                
                # Volta para o diretório base do projeto
                os.chdir(base_path)
                
                # Espera a aplicação iniciar
                print("Aguardando a aplicação iniciar...")
                for _ in range(20):  # Aumentado o tempo de espera
                    if verificar_aplicacao_rodando():
                        print("Aplicação iniciada com sucesso!")
                        break
                    time.sleep(1)
                else:
                    print("Falha ao iniciar a aplicação. Por favor, inicie manualmente.")
                    return
            except Exception as e:
                print(f"Erro ao iniciar a aplicação: {e}")
                print("Por favor, inicie a aplicação manualmente.")
                return
        else:
            return
    
    # Executa os testes
    print("Executando os testes...")
    report_file = os.path.join(base_path, "report.html")
    
    # Verifica vários possíveis locais para o arquivo de teste
    possíveis_caminhos = [
        os.path.join(base_path, "tests", "test_register_form.py"),
        os.path.join(base_path, "test_register_form.py"),
        os.path.join(base_path, "tests", "tests", "test_register_form.py")
    ]
    
    test_file_path = None
    for caminho in possíveis_caminhos:
        if os.path.exists(caminho):
            test_file_path = caminho
            print(f"Arquivo de teste encontrado em: {caminho}")
            break
    
    if not test_file_path:
        print("ERRO: Arquivo de teste não encontrado!")
        print("Caminhos verificados:")
        for caminho in possíveis_caminhos:
            print(f"  - {caminho}")
        return
    
    pytest_args = ["-v", test_file_path, f"--html={report_file}", "--self-contained-html"]
    
    result = subprocess.call(["pytest"] + pytest_args)
    
    if os.path.exists(report_file):
        print(f"Relatório gerado: {report_file}")
        print("Abrindo relatório no navegador...")
        webbrowser.open(f"file://{os.path.abspath(report_file)}")
    
    sys.exit(result)

if __name__ == "__main__":
    main()