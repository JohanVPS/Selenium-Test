"""
Funções utilitárias para os testes de automação.
"""

def validar_cpf(cpf):
    """
    Função para validar CPF - Remove caracteres especiais e verifica se o CPF é válido
    
    Args:
        cpf: String contendo o CPF com ou sem formatação
        
    Returns:
        True se o CPF for válido, False caso contrário
    """
    # Remove caracteres especiais
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    # Validação do primeiro dígito verificador
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    
    resto = soma % 11
    digito_verificador1 = 0 if resto < 2 else 11 - resto
    
    if int(cpf[9]) != digito_verificador1:
        return False
    
    # Validação do segundo dígito verificador
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    
    resto = soma % 11
    digito_verificador2 = 0 if resto < 2 else 11 - resto
    
    return int(cpf[10]) == digito_verificador2

def validar_telefone(telefone):
    """
    Função para validar formato de telefone - Deve estar no formato (XX) XXXXX-XXXX para celulares
    ou (XX) XXXX-XXXX para telefones fixos
    
    Args:
        telefone: String contendo o número de telefone
        
    Returns:
        True se o formato for válido, False caso contrário
    """
    # Remove caracteres especiais
    telefone_limpo = ''.join(filter(str.isdigit, telefone))
    
    # Verifica o comprimento (10 para fixo, 11 para celular)
    if len(telefone_limpo) == 11:  # Celular
        # Verifica o formato (XX) 9XXXX-XXXX
        return telefone_limpo[2] == '9'
    elif len(telefone_limpo) == 10:  # Fixo
        # Verifica o formato (XX) XXXX-XXXX
        return True
    
    return False

def validar_email(email):
    """
    Função para validar formato de email
    
    Args:
        email: String contendo o endereço de email
        
    Returns:
        True se o formato for válido, False caso contrário
    """
    import re
    # Padrão básico para validação de email
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    return bool(re.match(padrao, email))

