import React from 'react';

interface ButtonProps {
  text: string;
  onClick?: () => void;
  type?: 'button' | 'submit' | 'reset';
  className?: string;
  disabled?: boolean;
}

const Button: React.FC<ButtonProps> = ({
  text,
  onClick,
  type = 'button',
  className = 'btn btn-dark w-100',
  disabled = false,
}) => {
  return (
    <button type={type} className={className} onClick={onClick} disabled={disabled}>
      {text}
    </button>
  );
};

export default Button;
