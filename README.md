# Automação de Testes com Selenium e PyTest

Este projeto implementa testes automatizados para um formulário de registro usando Selenium e PyTest.

## Requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes do Python)

## Instalação das Dependências

```bash
pip install selenium pytest webdriver-manager
```

## Estrutura do Projeto

```
├── CRUD/                  # Aplicação React
├── tests/
│   ├── conftest.py        # Configurações do PyTest
│   ├── test_register_form.py  # Testes do formulário de registro
│   └── utils.py           # Funções utilitárias para os testes
└── README.md              # Este arquivo
```

## Casos de Teste Implementados

O projeto implementa os seguintes casos de teste:

1. **Tamanho mínimo da senha**:
   - Teste com senha válida (8+ caracteres)
   - Teste com senha inválida (menos de 8 caracteres)

2. **Validação do Telefone**:
   - Teste com formato de telefone correto: (11) 91234-5678
   - Teste com formato de telefone incorreto: (11) 1234-5678

3. **Validação do CPF**:
   - Teste com CPF válido: 123.456.789-09
   - Teste com CPF inválido: 123.456.789-00

4. **Validação do Email**:
   - Teste com formato de email correto: teste@exemplo.com
   - Teste com formato de email incorreto: teste@exemplo@com

5. **Double Check do Email e Senha**:
   - Teste com email e senha que coincidem
   - Teste com email e senha que não coincidem

6. **Sucesso**:
   - Teste preenchendo todos os dados corretamente

## Executando os Testes

Antes de executar os testes, certifique-se de que a aplicação React esteja em execução:

```bash
# Na pasta CRUD
npm install
npm run dev
```

Em seguida, execute os testes com o comando:

```bash
pytest -v tests/test_register_form.py
```

Para gerar um relatório HTML dos testes:

```bash
pytest -v tests/test_register_form.py --html=report.html
```

## Observações

- Os testes utilizam o Chrome como navegador padrão. O WebDriver Manager se encarregará de baixar a versão compatível do ChromeDriver automaticamente.
- Os testes assumem que a aplicação está rodando em `http://localhost:5173/register`. Ajuste a URL no código caso seja diferente.

