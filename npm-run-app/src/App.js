import React, { useState } from 'react';

const App = () => {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async event => {
    event.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/send-data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message })
      });
      const json = await response.json();
      setResponse(json.message);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={message}
          onChange={event => setMessage(event.target.value)}
        />
        <button type="submit">Send Data</button>
      </form>
      <div>
        <p>Response from server:</p>
        <p>{response}</p>
      </div>
    </div>
  );
};

export default App;
