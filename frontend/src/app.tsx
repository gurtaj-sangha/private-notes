import { useEffect } from 'react';
import { useSocket } from './useSocket';
import React from 'react';

function App() {
  const socket = useSocket();

  useEffect(() => {
    socket.on('connect', () => 
      console.log('Connected to server', socket.id));
    }, [socket]);

  return <h1>Hello Secure Chat</h1>
}

export default App;