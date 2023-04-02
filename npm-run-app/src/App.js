import React, { useState } from 'react';
import HeaderBar from './headerBar';
import './App.css';

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
  
  

    const [value, setValue] = useState(500);
  
    const handleSliderChange = (event) => {
      setValue(event.target.value);
  };


  return (
    
    <div class="app">
      <HeaderBar></HeaderBar>
      <div class="container">
      <div class="input-container">
        <div class="left" style={{ padding:20, width:'45%',marginTop:'15%',borderRadius:5}}>
          <h2 style={{color:'white'}}>Enter Input Query:</h2>
          <form onSubmit={handleSubmit}>
            <input style={{width:'75%',height:35}}
              type="text"
              value={message}
              onChange={event => setMessage(event.target.value)}
            />
            <button type="submit" style={{height:40, marginLeft:10}}>Submit</button>
          </form>
          </div>
          <div class="right" style={{ padding:20, width:'45%',marginTop:'15%',borderRadius:5}}>
          <h2 style={{color:'white'}}>Parameters:</h2>
          <form onSubmit={handleSubmit}>
          <input type="checkbox" id="checkbox1" name="checkbox1" value="option1"></input>
            <label style={{paddingRight:'5%'}}for="checkbox1">Don't store PDF Locally</label>
            <label for="slider">Summary Word Count:</label>
            <input type="range" id="slider" name="slider" min="100" max="1000" step="50" value={value} onChange={handleSliderChange}></input>
            <output id="output">{value}</output>

            <button style={{backgroundColor:'grey'}}type="submit" style={{height:40, marginLeft:10}}>Apply</button>
          </form>
          <div>

          </div>
          </div>
          </div>
          <div class="output">
            <h2>Article Summary:</h2>
            <p style={{color:'white'}}>{response}</p>
          
          </div>
      </div>
      
    </div>
  );
};

export default App;
