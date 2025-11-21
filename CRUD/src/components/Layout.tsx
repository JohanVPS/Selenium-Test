import React, { type ReactNode } from 'react';
import '../custom.scss';

interface LayoutProps {
  leftPanel: ReactNode;
  rightPanel: ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ leftPanel, rightPanel }) => {
  return (
    <div className="layout-container d-flex shadow-sm rounded">
      <div className="left-panel d-flex flex-column align-items-center justify-content-center text-white">
        {leftPanel}
      </div>
      <div className="right-panel flex-grow-1 bg-white">
        {rightPanel}
      </div>
    </div>
  );
};

export default Layout;
