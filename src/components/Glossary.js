import React from 'react';
import styles from './Glossary.module.css';

const Glossary = ({ terms }) => {
  return (
    <div className={styles.glossaryContainer}>
      <h2>Glossary</h2>
      <dl>
        {terms.map((term, index) => (
          <React.Fragment key={index}>
            <dt className={styles.term}>{term.title}</dt>
            <dd className={styles.description}>{term.description}</dd>
          </React.Fragment>
        ))}
      </dl>
    </div>
  );
};

export default Glossary;