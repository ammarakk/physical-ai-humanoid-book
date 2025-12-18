import React from 'react';
import Layout from '@theme/Layout';
import ChatbotWidget from '@site/src/components/Chatbot/ChatbotWidget';

export default function LayoutWrapper(props) {
  return (
    <>
      <Layout {...props} />
      <ChatbotWidget />
    </>
  );
}