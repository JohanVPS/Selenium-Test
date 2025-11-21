import React, { useState, useEffect } from 'react';

interface EmailInputFieldProps {
  label: string;
  placeholder: string;
  name: string;
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  error?: string;
  larger?: boolean;
  required?: boolean;
}

const EmailInputField: React.FC<EmailInputFieldProps> = ({
  label,
  placeholder,
  name,
  value = '',
  onChange,
  error,
  larger = false,
  required = false,
}) => {
  const [inputValue, setInputValue] = useState(value);
  const [emailError, setEmailError] = useState<string>('');

  useEffect(() => {
    setInputValue(value);
  }, [value]);

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const emailValue = e.target.value;
    setInputValue(emailValue);

    // Validação de formato de e-mail básica
    if (emailValue && !isValidEmail(emailValue)) {
      setEmailError('Formato de e-mail inválido');
    } else {
      setEmailError('');
    }

    // Passa o evento para o onChange original
    if (onChange) {
      onChange(e);
    }
  };

  // Função para validar o formato do e-mail
  const isValidEmail = (email: string): boolean => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  return (
    <div className="mb-3">
      <label htmlFor={name} className="form-label mb-1">
        {label}{required && <span className="text-danger">*</span>}
      </label>
      <input
        type="email"
        className={`form-control ${larger ? 'form-control-larger' : 'form-control-sm'} ${(error || emailError) ? 'is-invalid' : ''}`}
        id={name}
        name={name}
        placeholder={placeholder}
        value={inputValue}
        onChange={handleEmailChange}
      />
      {(error || emailError) && <div className="invalid-feedback">{error || emailError}</div>}
      {required && !error && !emailError && !inputValue.trim() && <div className="text-danger" style={{fontSize: '0.8rem'}}>Campo obrigatório</div>}
    </div>
  );
};

export default EmailInputField;
