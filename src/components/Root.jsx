import React from 'react';
import ChatbotWidget from '@site/src/components/Chatbot/ChatbotWidget';
import { LanguageProvider } from '@site/src/contexts/LanguageContext';

export default function Root({ children }) {
  return (
    <LanguageProvider>
      {children}
      <ChatbotWidget />
    </LanguageProvider>
  );
}