import pytest

# Hook para personalizar as informações de relatório
def pytest_html_report_title(report):
    report.title = "Relatório de Testes de Automação - Formulário de Registro"

# Hook para adicionar descrições detalhadas aos testes
def pytest_collection_modifyitems(items):
    for item in items:
        if "test_tamanho_minimo_senha_valido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de senha com tamanho mínimo válido"
        elif "test_tamanho_minimo_senha_invalido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de senha com tamanho mínimo inválido"
        elif "test_telefone_valido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de formato de telefone correto"
        elif "test_telefone_invalido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de formato de telefone incorreto"
        elif "test_cpf_valido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de CPF válido"
        elif "test_cpf_invalido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de CPF inválido"
        elif "test_email_valido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de email com formato correto"
        elif "test_email_invalido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de email com formato incorreto"
        elif "test_double_check_email_senha_valido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de correspondência de email e senha correta"
        elif "test_double_check_email_senha_invalido" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de correspondência de email e senha incorreta"
        elif "test_formulario_sucesso" in item.nodeid:
            item._nodeid = item.nodeid + ": Validação de preenchimento completo do formulário"

