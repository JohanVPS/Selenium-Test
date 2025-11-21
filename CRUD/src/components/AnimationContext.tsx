import React, { createContext, useContext, ReactNode } from 'react';

interface AnimatePresenceProps {
  children: ReactNode;
}

const AnimationContext = createContext({});

export const useAnimation = () => useContext(AnimationContext);

export const AnimatePresence: React.FC<AnimatePresenceProps> = ({ children }) => {
  return (
    <AnimationContext.Provider value={{}}>
      {children}
    </AnimationContext.Provider>
  );
};
