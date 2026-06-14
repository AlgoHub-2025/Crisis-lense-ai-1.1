import React, { useEffect, useState } from 'react';
import './ConfidenceMeter.css';

export default function ConfidenceMeter({ confidence }) {
  const [offset, setOffset] = useState(100);
  const radius = 28;
  const circumference = 2 * Math.PI * radius;
  
  useEffect(() => {
    // Ensure confidence is between 0 and 1
    const safeConfidence = Math.max(0, Math.min(1, confidence || 0));
    // Calculate the SVG stroke offset
    const progressOffset = circumference - (safeConfidence * circumference);
    
    // Slight delay for animation effect
    const timeout = setTimeout(() => {
      setOffset(progressOffset);
    }, 100);
    
    return () => clearTimeout(timeout);
  }, [confidence, circumference]);

  const percentage = Math.round((confidence || 0) * 100);
  
  let colorClass = "meter-green";
  if (percentage < 50) colorClass = "meter-red";
  else if (percentage < 80) colorClass = "meter-amber";

  return (
    <div className={`confidence-meter ${colorClass}`}>
      <div className="meter-svg-wrapper">
        <svg className="meter-svg" width="70" height="70">
          <circle 
            className="meter-bg"
            stroke="rgba(255, 255, 255, 0.1)"
            strokeWidth="5"
            fill="transparent"
            r={radius}
            cx="35"
            cy="35"
          />
          <circle 
            className="meter-progress"
            stroke="currentColor"
            strokeWidth="5"
            strokeLinecap="round"
            fill="transparent"
            r={radius}
            cx="35"
            cy="35"
            style={{
              strokeDasharray: circumference,
              strokeDashoffset: offset
            }}
          />
        </svg>
        <div className="meter-text">
          <span className="meter-value">{percentage}%</span>
        </div>
      </div>
      <div className="meter-label">
        <strong>XGBoost</strong>
        <span>AI Confidence</span>
      </div>
    </div>
  );
}
