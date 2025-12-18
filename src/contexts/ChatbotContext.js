import React, { createContext, useContext, useReducer } from 'react';
import apiService from '../utils/apiService';

// Create Chatbot Context
const ChatbotContext = createContext();

// Initial state for the chatbot
const initialState = {
  messages: [
    { id: 1, text: "Hello! I'm your AI assistant for the Physical AI & Humanoid Robotics book. Ask me anything about the content!", sender: 'bot' }
  ],
  isLoading: false,
  error: null,
  conversationId: null
};

// Reducer function to handle state updates
const chatbotReducer = (state, action) => {
  switch (action.type) {
    case 'SET_LOADING':
      return { ...state, isLoading: action.payload };
    
    case 'SET_ERROR':
      return { ...state, error: action.payload };
    
    case 'ADD_MESSAGE':
      return { 
        ...state, 
        messages: [...state.messages, action.payload],
        error: null
      };
    
    case 'SET_CONVERSATION_ID':
      return { ...state, conversationId: action.payload };
    
    case 'RESET_CHAT':
      return { 
        ...initialState,
        messages: [
          { id: 1, text: "Hello! I'm your AI assistant for the Physical AI & Humanoid Robotics book. Ask me anything about the content!", sender: 'bot' }
        ]
      };
    
    default:
      return state;
  }
};

// Chatbot Provider Component
export const ChatbotProvider = ({ children }) => {
  const [state, dispatch] = useReducer(chatbotReducer, initialState);

  // Function to send a message to the chatbot
  const sendMessage = async (text) => {
    if (!text.trim()) return;

    // Add user message to chat
    const userMessage = {
      id: Date.now(),
      text: text,
      sender: 'user'
    };
    
    dispatch({ type: 'ADD_MESSAGE', payload: userMessage });
    dispatch({ type: 'SET_LOADING', payload: true });
    dispatch({ type: 'SET_ERROR', payload: null });

    try {
      // Call the backend API
      const response = await apiService.chatbot.query({
        query: text,
        conversation_id: state.conversationId || null
      });

      // Add bot response to chat
      const botMessage = {
        id: Date.now() + 1,
        text: response.response,
        sender: 'bot'
      };

      dispatch({ type: 'ADD_MESSAGE', payload: botMessage });
      
      // Set conversation ID if not already set
      if (!state.conversationId && response.conversation_id) {
        dispatch({ type: 'SET_CONVERSATION_ID', payload: response.conversation_id });
      }
    } catch (error) {
      console.error('Error sending message:', error);
      dispatch({ 
        type: 'SET_ERROR', 
        payload: error.message || 'Failed to get response from chatbot' 
      });
      
      // Add error message to chat
      const errorMessage = {
        id: Date.now() + 1,
        text: "Sorry, I couldn't process your request at the moment. Please try again.",
        sender: 'bot'
      };
      dispatch({ type: 'ADD_MESSAGE', payload: errorMessage });
    } finally {
      dispatch({ type: 'SET_LOADING', payload: false });
    }
  };

  // Function to reset the chat
  const resetChat = () => {
    dispatch({ type: 'RESET_CHAT' });
  };

  // Value to be provided to consumers
  const value = {
    messages: state.messages,
    isLoading: state.isLoading,
    error: state.error,
    conversationId: state.conversationId,
    sendMessage,
    resetChat
  };

  return (
    <ChatbotContext.Provider value={value}>
      {children}
    </ChatbotContext.Provider>
  );
};

// Custom hook to use the chatbot context
export const useChatbot = () => {
  const context = useContext(ChatbotContext);
  if (!context) {
    throw new Error('useChatbot must be used within a ChatbotProvider');
  }
  return context;
};