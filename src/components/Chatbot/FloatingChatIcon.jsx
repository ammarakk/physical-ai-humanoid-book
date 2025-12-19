import React from 'react';
import './FloatingChatIcon.css';

const FloatingChatIcon = ({ onClick, isOpen }) => {
  return (
    <div 
      className={`floating-chatbot-icon ${isOpen ? 'open' : ''}`}
      onClick={onClick}
    >
      {isOpen ? '×' : '🤖'}
    </div>
  );
};

export default FloatingChatIcon;