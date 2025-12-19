import React from 'react';
import './AnimatedRobot.css'; // We'll create this CSS file

const AnimatedRobot = () => {
  return (
    <div className="animated-robot-container">
      <div className="robot">
        <div className="robot-head">
          <div className="robot-eyes">
            <div className="robot-eye left-eye"></div>
            <div className="robot-eye right-eye"></div>
          </div>
        </div>
        <div className="robot-body">
          <div className="robot-chest">
            <div className="robot-heart"></div>
          </div>
        </div>
        <div className="robot-arms">
          <div className="robot-arm left-arm"></div>
          <div className="robot-arm right-arm"></div>
        </div>
        <div className="robot-legs">
          <div className="robot-leg left-leg"></div>
          <div className="robot-leg right-leg"></div>
        </div>
      </div>
    </div>
  );
};

export default AnimatedRobot;