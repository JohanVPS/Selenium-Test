import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Layout from '../components/Layout';
import InputField from '../components/InputField';
import EmailInputField from '../components/EmailInputField';
import Button from '../components/Button';
import LinkText from '../components/LinkText';
import twitchLogo from '../assets/twitchtv logo.png';

const Login: React.FC = () => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    nomeCompleto: '',
    email: '',
    senha: '',
  });

  const [isFormValid, setIsFormValid] = useState(false);
  const [emailError, setEmailError] = useState('');

  // Função para validar o formato do e-mail
  const isValidEmail = (email: string): boolean => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  // Verifica se todos os campos obrigatórios estão preenchidos e válidos
  useEffect(() => {
    const { email, senha } = formData;
    const isEmailValid = email.trim() !== '' && isValidEmail(email);
    const isSenhaValid = senha.trim() !== '';
    const isValid = isEmailValid && isSenhaValid;
    setIsFormValid(isValid);
  }, [formData.email, formData.senha]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
    
    // Atualiza o estado de erro do email, se necessário
    if (name === 'email') {
      if (value.trim() !== '' && !isValidEmail(value)) {
        setEmailError('Formato de e-mail inválido');
      } else {
        setEmailError('');
      }
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Add login submission logic here
    console.log('Login submitted', formData);
  };

  const leftPanel = (
    <>
      <img src={twitchLogo} alt="Twitch Logo" className="img-fluid" style={{ height: 80, marginBottom: '1rem', objectFit: 'contain' }} />
      <h3>Twitch.tv</h3>
      <Button text="Cadastrar" className="btn btn-outline-light mt-3 px-4" onClick={() => navigate('/register')} />
    </>
  );

  const rightPanel = (
    <form onSubmit={handleSubmit}>
      <h2 className="mb-1">Fazer Login</h2>
      <p className="text-muted mb-4">Preencha seus dados</p>

      {/* <InputField
        label="Nome Completo"
        placeholder="Insira o seu nome"
        name="nomeCompleto"
        value={formData.nomeCompleto}
        onChange={handleChange}
        larger={true}
      /> */}

      <EmailInputField
        label="E-mail"
        placeholder="Insira o seu e-mail"
        name="email"
        value={formData.email}
        onChange={handleChange}
        error={emailError}
        larger={true}
        required={true}
      />

      <InputField
        label="Senha"
        placeholder="Insira a sua Senha"
        name="senha"
        type="password"
        value={formData.senha}
        onChange={handleChange}
        larger={true}
        required={true}
      />

      <div className="mt-4 mb-2">
        <Button text="Entrar" type="submit" disabled={!isFormValid} />
      </div>

      <div className="mt-1">
        <LinkText text="Não tem uma conta?" linkText="Cadastrar-se" href="/register" />
      </div>
      <div className="mt-1">
        <LinkText text="" linkText="Esqueci a senha" onClick={() => alert('Funcionalidade de recuperação de senha será implementada em breve!')} />
      </div>
    </form>
  );

  return <Layout leftPanel={leftPanel} rightPanel={rightPanel} />;
};

export default Login;
