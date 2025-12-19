import React from 'react';
import styles from './HumanoidDiagram.module.css';

const HumanoidDiagram = ({ parts, highlightedPart }) => {
  return (
    <div className={styles.diagramContainer}>
      <img src="/img/humanoid-base.svg" alt="Humanoid Base Diagram" className={styles.baseImage} />
      {parts.map(part => (
        <div
          key={part.id}
          className={`${styles.partOverlay} ${highlightedPart === part.id ? styles.highlighted : ''}`}
          style={{ top: part.y, left: part.x, width: part.width, height: part.height }}
          title={part.name}
        ></div>
      ))}
      <p className={styles.caption}>Interactive Humanoid Diagram</p>
    </div>
  );
};

export default HumanoidDiagram;