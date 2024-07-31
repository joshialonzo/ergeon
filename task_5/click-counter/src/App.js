// src/App.js
import React from 'react';
import ClickCounter from './ClickCounter';
import './index.css';

const App = () => {
  return (
    <div className="App">
      <h1>Click Counter Example</h1>
      <ClickCounter initialCount={0} />
    </div>
  );
};

export default App;