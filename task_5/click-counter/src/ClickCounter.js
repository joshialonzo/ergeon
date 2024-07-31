import React, { useState } from 'react';

const ClickCounter = ({ initialCount }) => {
  const [count, setCount] = useState(initialCount);

  const handleClick = () => {
    setCount(count + 1);
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <button className="custom-button" onClick={handleClick}>
        Click Count: {count}
      </button>
    </div>
  );
};

export default ClickCounter;