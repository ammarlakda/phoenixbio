import React, { useState } from 'react';
import HeaderBar from './headerBar';

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
      <HeaderBar></HeaderBar>
      <div style={{marginLeft:'30%', backgroundColor:'grey', marginRight:'45%', padding:20, width:'40%',marginTop:'15%',marginBottom:'15%',borderRadius:20}}>
        <h2>Enter Input Query:</h2>
        <form onSubmit={handleSubmit}>
          <input style={{width:'75%',height:35}}
            type="text"
            value={message}
            onChange={event => setMessage(event.target.value)}
          />
          <button type="submit" style={{height:40, marginLeft:10}}>Submit</button>
        </form>
        <div>
          <h2>Article Summary:</h2>
          <p style={{color:'lightgrey'}}>{response}</p>
        </div>
        </div>
    </div>
  );
};

export default App;
