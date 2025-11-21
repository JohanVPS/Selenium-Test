import os
import subprocess
import sys
import time
import webbrowser

def verificar_dependencias():
    try:
        import selenium
        import pytest
        from webdriver_manager.chrome import ChromeDriverManager
        return True
    except ImportError as e:
        subprocess.call([sys.executable, "-m", "pip", "install", "selenium", "pytest", "webdriver-manager", "pytest-html"])
        return False

def verificar_aplicacao_rodando():
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', 5173))
    sock.close()
    return result == 0

def main():
    if not verificar_dependencias():
        return
    
    if not verificar_aplicacao_rodando():
        print("A aplicação não está rodando em http://localhost:5173")
        print("Execute 'npm run dev' na pasta CRUD antes de executar os testes.")
        print("Deseja tentar iniciar a aplicação automaticamente? (s/n)")
        resposta = input().lower()
        
        if resposta == 's':
            print("Iniciando a aplicação...")
            try:
                os.chdir('CRUD')
                subprocess.Popen(["npm", "run", "dev"], 
                                stdout=subprocess.DEVNULL, 
                                stderr=subprocess.DEVNULL)
                os.chdir('..')
                
                print("Aguardando a aplicação iniciar...")
                for _ in range(10):
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
    
    print("Executando os testes...")
    report_file = "report.html"
    pytest_args = ["-v", "tests/test_register_form.py", f"--html={report_file}", "--self-contained-html"]
    
    result = subprocess.call(["pytest"] + pytest_args)
    
    if os.path.exists(report_file):
        print(f"Relatório gerado: {report_file}")
        print("Abrindo relatório no navegador...")
        webbrowser.open(f"file://{os.path.abspath(report_file)}")
    
    sys.exit(result)

if __name__ == "__main__":
    main()
