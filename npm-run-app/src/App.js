import React, { useState } from "react";

const TextInputOutput = () => {
  const [inputText, setInputText] = useState("");
  const [outputText, setOutputText] = useState("");

  const handleSubmit = () => {
    setOutputText(inputText);
  };

  return (
    <div style={styles.container}>
      <input
        type="text"
        placeholder="Enter text here"
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        style={styles.input}
      />
      <button onClick={handleSubmit} style={styles.button}>
        Submit
      </button>
      <p style={styles.outputText}>{outputText}</p>
    </div>
  );
};

const styles = {
  container: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    height: "100vh",
  },
  input: {
    padding: "1rem",
    fontSize: "1.2rem",
    width: "50%",
    margin: "1rem 0",
    borderRadius: "5px",
    border: "1px solid gray",
  },
  button: {
    padding: "1rem",
    fontSize: "1.2rem",
    backgroundColor: "lightgray",
    borderRadius: "5px",
    marginTop: "1rem",
    border: "1px solid gray",
    cursor: "pointer",
  },
  outputText: {
    fontSize: "1.5rem",
    padding: "1rem",
    backgroundColor: "lightgray",
    borderRadius: "5px",
    marginTop: "1rem",
  },
};

export default TextInputOutput;
