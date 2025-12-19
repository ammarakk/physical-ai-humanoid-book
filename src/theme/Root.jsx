import React, { useState, useEffect } from 'react';
import { ChatbotProvider } from '@site/src/contexts/ChatbotContext';
import FloatingChatIcon from '@site/src/components/Chatbot/FloatingChatIcon';
import ChatbotInterface from '@site/src/components/Chatbot/ChatbotInterface';

// Global state provider component
const Root = ({ children }) => {
  const [showChatbot, setShowChatbot] = useState(false);
  const [isClient, setIsClient] = useState(false);

  useEffect(() => {
    // Set isClient to true after component mounts on client
    setIsClient(true);
  }, []);

  const toggleChatbot = () => {
    setShowChatbot(!showChatbot);
  };

  return (
    <ChatbotProvider>
      {children}
      {isClient && (
        <>
          <FloatingChatIcon onClick={toggleChatbot} isOpen={showChatbot} />
          <ChatbotInterface
            isVisible={showChatbot}
            onClose={() => setShowChatbot(false)}
          />
        </>
      )}
    </ChatbotProvider>
  );
};

export default Root;