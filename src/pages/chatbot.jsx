import React, { useEffect, useRef, useState } from 'react';
import { useHistory, Redirect } from '@docusaurus/router';
import Layout from '@theme/Layout';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import { useLanguage } from '@site/src/contexts/LanguageContext';
import '../components/Chatbot/ChatbotWidget.css'; // Using the same styles as the widget

const ChatbotPage = () => {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const messagesEndRef = useRef(null);
  const { siteConfig } = useDocusaurusContext();
  const history = useHistory();
  const { currentLanguage } = useLanguage(); // Get the current language from context

  // Check if user is authenticated
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      // Redirect to login if not authenticated
      history.push('/login');
      return;
    }
    setIsAuthenticated(true);
  }, [history]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = async () => {
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
        // If no token, redirect to login
        history.push('/login');
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
          history.push('/login');
          return;
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
    } catch (err) {
      setError('Sorry, I encountered an error. Please try again.');
      console.error('Chat error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleClear = () => {
    setMessages([]);
    setError(null);
  };

  // If not authenticated, redirect to login
  if (!isAuthenticated) {
    return <Redirect to="/login" />;
  }

  return (
    <Layout
      title={`AI Chatbot`}
      description="Ask questions about the Physical AI & Humanoid Robotics book">
      <main className="chatbot-page">
        <div className="container padding-vert--lg">
          <div className="row">
            <div className="col col--12">
              <div className="chatbot-interface-full">
                <div className="chatbot-header">
                  <div className="chatbot-header-content">
                    <h2>AI Assistant for Physical AI & Humanoid Robotics</h2>
                    <button onClick={handleClear} className="clear-button">
                      Clear Chat
                    </button>
                  </div>
                </div>
                <div className="chatbot-messages">
                  {error && (
                    <div className="chatbot-message system-message">
                      <div className="message-content">
                        {error}
                      </div>
                    </div>
                  )}
                  {messages.length === 0 ? (
                    <div className="chatbot-welcome">
                      Welcome! I'm your AI assistant for the Physical AI & Humanoid Robotics book. Ask me anything about the content.
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
                      <div className="message-content">
                        <div className="typing-indicator">
                          <span></span>
                          <span></span>
                          <span></span>
                        </div>
                      </div>
                    </div>
                  )}
                  <div ref={messagesEndRef} />
                </div>
                <div className="chatbot-input">
                  <input
                    type="text"
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder="Ask a question about the book..."
                    disabled={isLoading}
                  />
                  <button onClick={handleSend} disabled={isLoading}>
                    {isLoading ? 'Sending...' : 'Send'}
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    </Layout>
  );
};

export default ChatbotPage;