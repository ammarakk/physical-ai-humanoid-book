import React, { useState, useEffect } from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';
import { useLocation } from '@docusaurus/router';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { translate } from '@docusaurus/Translate';
import { useLanguage } from '@site/src/contexts/LanguageContext';
import './ChatbotWidget.css';

const ChatbotWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const location = useLocation();
  const { siteConfig } = useDocusaurusContext();
  const { currentLanguage } = useLanguage(); // Get the current language from context

  // Function to toggle chatbot window
  const toggleChatbot = () => {
    setIsOpen(!isOpen);
  };

  // Function to close chatbot
  const closeChatbot = () => {
    setIsOpen(false);
  };

  // Function to handle sending a message
  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!inputValue.trim() || isLoading) return;

    const userMessage = inputValue.trim();
    setInputValue('');

    // Add user message to chat
    const newMessages = [...messages, { id: Date.now(), text: userMessage, sender: 'user' }];
    setMessages(newMessages);
    setIsLoading(true);

    try {
      // Get JWT token from localStorage
      const token = localStorage.getItem('token');

      if (!token) {
        // If no token, inform user they need to log in
        const errorMsg = translate({
          id: 'chatbot.loginRequired',
          message: 'You need to log in to use the chatbot. Please go to the login page.'
        });
        setMessages(prev => [
          ...prev,
          { id: Date.now() + 1, text: errorMsg, sender: 'system' }
        ]);
        setIsLoading(false);
        return;
      }

      // Call the backend API with the current language
      const response = await fetch('/api/chat/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({
          query: userMessage,
          language: currentLanguage // Use the selected language from context
        })
      });

      if (!response.ok) {
        if (response.status === 401) {
          // Token might be expired, redirect to login
          localStorage.removeItem('token');
          const errorMsg = translate({
            id: 'chatbot.authExpired',
            message: 'Your session has expired. Please log in again.'
          });
          setMessages(prev => [
            ...prev,
            { id: Date.now() + 1, text: errorMsg, sender: 'system' }
          ]);
        } else {
          throw new Error(`API error: ${response.status}`);
        }
      } else {
        const data = await response.json();
        setMessages(prev => [
          ...prev,
          { id: Date.now() + 1, text: data.response, sender: 'bot' }
        ]);
      }
    } catch (error) {
      console.error('Chatbot error:', error);
      const errorMsg = translate({
        id: 'chatbot.errorMessage',
        message: 'Sorry, I encountered an error. Please try again.'
      });
      setMessages(prev => [
        ...prev,
        { id: Date.now() + 1, text: errorMsg, sender: 'system' }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  // Close chatbot when navigating to auth pages
  useEffect(() => {
    if (location.pathname.includes('/login') || location.pathname.includes('/signup')) {
      setIsOpen(false);
    }
  }, [location]);

  return (
    <BrowserOnly>
      {() => {
        // Only render if not on auth pages
        const shouldRender = !location.pathname.includes('/login') && !location.pathname.includes('/signup');

        return shouldRender ? (
          <>
            {/* Floating Chatbot Icon */}
            <div
              className={`floating-chatbot-icon ${isOpen ? 'hidden' : ''}`}
              onClick={toggleChatbot}
              title={translate({ id: 'chatbot.openTitle', message: 'Open AI Assistant' })}
            >
              🤖
            </div>

            {/* Chatbot Window */}
            {isOpen && (
              <div className="chatbot-container">
                <div className="chatbot-header">
                  <h3>{translate({ id: 'chatbot.title', message: 'AI Assistant' })}</h3>
                  <button
                    className="chatbot-close"
                    onClick={closeChatbot}
                    aria-label={translate({ id: 'chatbot.closeAria', message: 'Close chat' })}
                  >
                    ×
                  </button>
                </div>
                <div className="chatbot-messages">
                  {messages.length === 0 ? (
                    <div className="chatbot-welcome">
                      {translate({
                        id: 'chatbot.welcome',
                        message: 'Hello! I\'m your AI assistant. Ask me anything about the Physical AI & Humanoid Robotics book.'
                      })}
                    </div>
                  ) : (
                    messages.map((message) => (
                      <div
                        key={message.id}
                        className={`chatbot-message ${message.sender}-message`}
                      >
                        <div className="message-content">{message.text}</div>
                      </div>
                    ))
                  )}
                  {isLoading && (
                    <div className="chatbot-message bot-message">
                      <div className="message-content typing-indicator">
                        <span></span>
                        <span></span>
                        <span></span>
                      </div>
                    </div>
                  )}
                </div>
                <form className="chatbot-input" onSubmit={handleSendMessage}>
                  <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    placeholder={translate({
                      id: 'chatbot.inputPlaceholder',
                      message: 'Ask a question...'
                    })}
                    disabled={isLoading}
                  />
                  <button
                    type="submit"
                    disabled={!inputValue.trim() || isLoading}
                  >
                    {translate({ id: 'chatbot.sendButton', message: 'Send' })}
                  </button>
                </form>
              </div>
            )}
          </>
        ) : null;
      }}
    </BrowserOnly>
  );
};

export default ChatbotWidget;