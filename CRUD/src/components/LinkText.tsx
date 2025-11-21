import React from 'react';
import { Link } from 'react-router-dom';

interface LinkTextProps {
  text: string;
  linkText: string;
  href?: string;
  onClick?: () => void;
}

const LinkText: React.FC<LinkTextProps> = ({ text, linkText, href, onClick }) => {
  return (
    <p className="text-center mt-3 text-muted">
      {text} {
        href ? (
          <Link to={href} className="fw-bold text-decoration-none" style={{ color: '#0e1428' }}>
            {linkText}
          </Link>
        ) : (
          <a onClick={onClick} className="fw-bold text-decoration-none" style={{ cursor: 'pointer', color: '#0e1428' }}>
            {linkText}
          </a>
        )
      }
    </p>
  );
};

export default LinkText;
