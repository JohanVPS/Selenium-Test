import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Layout from '../components/Layout';
import InputField from '../components/InputField';
import EmailInputField from '../components/EmailInputField';
import Button from '../components/Button';
import LinkText from '../components/LinkText';
import twitchLogo from '../assets/twitchtv logo.png';

const Register: React.FC = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    nome: '',
    sobrenome: '',
    telefone: '',
    cpf: '',
    email: '',
    confirmarEmail: '',
    senha: '',
    confirmarSenha: '',
  });

  const [formErrors, setFormErrors] = useState({
    email: '',
    confirmarEmail: '',
    senha: '',
    confirmarSenha: '',
  });

  const [isFormValid, setIsFormValid] = useState(false);
  
  // Estado para controlar a validação de requisitos da senha
  const [passwordRequirements, setPasswordRequirements] = useState({
    hasLowerCase: false,
    hasUpperCase: false,
    hasNumber: false,
    hasSpecialChar: false,
    hasMinLength: false,
  });

  // Verificar se os e-mails são iguais quando qualquer um dos campos mudar
  useEffect(() => {
    if (formData.confirmarEmail && formData.email !== formData.confirmarEmail) {
      setFormErrors(prev => ({ ...prev, confirmarEmail: 'Os e-mails não correspondem' }));
    } else {
      setFormErrors(prev => ({ ...prev, confirmarEmail: '' }));
    }
  }, [formData.email, formData.confirmarEmail]);

  // Verificar se todos os campos obrigatórios estão preenchidos
  useEffect(() => {
    const { nome, sobrenome, email, confirmarEmail, senha, confirmarSenha } = formData;
    const hasNoErrors = Object.values(formErrors).every(error => error === '');
    const requiredFieldsFilled = [
      nome.trim(),
      sobrenome.trim(),
      email.trim(),
      confirmarEmail.trim(),
      senha.trim(),
      confirmarSenha.trim()
    ].every(field => field !== '');
    
    // Verifica se todos os requisitos da senha foram atendidos
    const allPasswordRequirementsMet = Object.values(passwordRequirements).every(req => req);
    
    setIsFormValid(requiredFieldsFilled && hasNoErrors && allPasswordRequirementsMet);
  }, [
    formData.nome,
    formData.sobrenome,
    formData.email,
    formData.confirmarEmail,
    formData.senha,
    formData.confirmarSenha,
    formErrors,
    passwordRequirements
  ]);

  // Validar os requisitos da senha
  useEffect(() => {
    const password = formData.senha;
    
    // Verificar cada requisito
    const hasLowerCase = /[a-z]/.test(password);
    const hasUpperCase = /[A-Z]/.test(password);
    const hasNumber = /[0-9]/.test(password);
    const hasSpecialChar = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password);
    const hasMinLength = password.length >= 6;
    
    // Atualizar o estado de requisitos da senha
    setPasswordRequirements({
      hasLowerCase,
      hasUpperCase,
      hasNumber,
      hasSpecialChar,
      hasMinLength
    });
    
    // Verificar se todos os requisitos foram atendidos
    const allRequirementsMet = 
      hasLowerCase && 
      hasUpperCase && 
      hasNumber && 
      hasSpecialChar && 
      hasMinLength;
    
    // Atualizar o erro da senha com base nos requisitos
    if (password && !allRequirementsMet) {
      setFormErrors(prev => ({ ...prev, senha: 'A senha não atende aos requisitos de segurança' }));
    } else {
      setFormErrors(prev => ({ ...prev, senha: '' }));
    }
    
  }, [formData.senha]);

  // Verificar se as senhas são iguais quando qualquer uma das senhas mudar
  useEffect(() => {
    if (formData.confirmarSenha && formData.senha !== formData.confirmarSenha) {
      setFormErrors(prev => ({ ...prev, confirmarSenha: 'As senhas não correspondem' }));
    } else {
      setFormErrors(prev => ({ ...prev, confirmarSenha: '' }));
    }
  }, [formData.senha, formData.confirmarSenha]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    // Verificar se todos os requisitos de senha foram cumpridos
    const allPasswordRequirementsMet = Object.values(passwordRequirements).every(req => req);
    
    // Verificar se há erros antes de enviar
    const hasErrors = Object.values(formErrors).some(error => error !== '');
    
    if (hasErrors || !allPasswordRequirementsMet) {
      console.log('Por favor, corrija os erros no formulário.');
      return;
    }
    
    // Add form submission logic here
    console.log('Form submitted', formData);
  };

  const leftPanel = (
    <>
      <img src={twitchLogo} alt="Twitch Logo" className="img-fluid" style={{ height: 80, marginBottom: '1rem', objectFit: 'contain' }} />
      <h3>Twitch.tv</h3>
      <Button text="Entrar" className="btn btn-outline-light mt-3 px-4" onClick={() => navigate('/login')} />
    </>
  );

  const rightPanel = (
    <form onSubmit={handleSubmit}>
      <h2 className="mb-1">Crie sua conta</h2>
      <p className="text-muted mb-4">Preencha seus dados</p>

      <div className="input-group-container">
        <InputField
          label="Nome"
          placeholder="Insira o seu nome"
          name="nome"
          value={formData.nome}
          onChange={handleChange}
          larger={true}
          required={true}
        />
        <InputField
          label="Sobrenome"
          placeholder="Insira o seu sobrenome"
          name="sobrenome"
          value={formData.sobrenome}
          onChange={handleChange}
          larger={true}
          required={true}
        />
      </div>

      <div className="input-group-container">
        <InputField
          label="Telefone"
          placeholder="(99) 99999-9999"
          name="telefone"
          value={formData.telefone}
          onChange={handleChange}
          larger={true}
          // A máscara será aplicada automaticamente pelo nome do campo
        />
        <InputField
          label="CPF"
          placeholder="000.000.000-00"
          name="cpf"
          value={formData.cpf}
          onChange={handleChange}
          larger={true}
          // A máscara será aplicada automaticamente pelo nome do campo
        />
      </div>

      <div className="input-group-container">
        <EmailInputField
          label="E-mail"
          placeholder="Insira o seu e-mail"
          name="email"
          value={formData.email}
          onChange={handleChange}
          error={formErrors.email}
          larger={true}
          required={true}
        />
        <EmailInputField
          label="Confirmar E-mail"
          placeholder="Confirme o e-mail"
          name="confirmarEmail"
          value={formData.confirmarEmail}
          onChange={handleChange}
          error={formErrors.confirmarEmail}
          larger={true}
          required={true}
        />
      </div>

      <div className="input-group-container">
        <div>
          <InputField
            label="Senha"
            placeholder="Insira a sua senha"
            name="senha"
            type="password"
            value={formData.senha}
            onChange={handleChange}
            error={formErrors.senha}
            larger={true}
            required={true}
          />
          {formData.senha && (
            <div className="mt-1 password-requirements">
              <small className="d-block mb-1">Requisitos:</small>
              <div className="d-flex flex-wrap gap-1 small">
                <span className={`badge ${passwordRequirements.hasLowerCase ? 'bg-success' : 'bg-danger'}`}>a-z</span>
                <span className={`badge ${passwordRequirements.hasUpperCase ? 'bg-success' : 'bg-danger'}`}>A-Z</span>
                <span className={`badge ${passwordRequirements.hasNumber ? 'bg-success' : 'bg-danger'}`}>0-9</span>
                <span className={`badge ${passwordRequirements.hasSpecialChar ? 'bg-success' : 'bg-danger'}`}>@#$</span>
                <span className={`badge ${passwordRequirements.hasMinLength ? 'bg-success' : 'bg-danger'}`}>6+</span>
              </div>
            </div>
          )}
        </div>
        <div>
          <InputField
            label="Confirmar senha"
            placeholder="Confirme a senha"
            name="confirmarSenha"
            type="password"
            value={formData.confirmarSenha}
            onChange={handleChange}
            error={formErrors.confirmarSenha}
            larger={true}
            required={true}
          />
        </div>
      </div>

      <div className="mt-4 mb-2">
        <Button text="Cadastrar" type="submit" disabled={!isFormValid} />
      </div>

      <div className="mt-1">
        <LinkText text="Já tem uma conta?" linkText="Fazer login" href="/login" />
      </div>
    </form>
  );

  return <Layout leftPanel={leftPanel} rightPanel={rightPanel} />;
};

export default Register;
