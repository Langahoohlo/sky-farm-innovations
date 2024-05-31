'use client'
import React, { useState, useRef } from 'react';

const MainContent = () => {
  const [isPlaying, setIsPlaying] = useState(false);
  const videoRef = useRef(null);

  const handlePlay = () => {
    const video = videoRef.current;
    if (video && !isPlaying) {
      video.play().then(() => {
        setIsPlaying(true);
      }).catch(error => {
        console.error('Error playing video:', error);
      });
    }
  };

  return (
    <div className="flex flex-col flex-grow p-4">
      <div className="flex justify-between items-center mb-4">
        <div className="text-lg font-bold">Live</div>
        <div className="flex space-x-2">
          <button className="px-2 py-1 bg-gray-300">Live</button>
          <button className="px-2 py-1 bg-gray-300">Map</button>
        </div>
      </div>
      <div className="bg-gray-200 h-96 mb-4 flex items-center justify-center">
        Map/ Live stream
        <div>
          <video ref={videoRef} controls>
            <source src="http://localhost:5000/video_feed" type="video/mp4 muted" />
          </video>
          {!isPlaying && (
            <button onClick={handlePlay}>Play</button>
          )}
        </div>
      </div>
      <div className="flex space-x-4">
        <div className="bg-purple-500 text-white p-4 flex-grow rounded-lg">
          <h3 className="font-bold">Missions</h3>
          <p>Missions taken: 2</p>
          <p>Review</p>
        </div>
        <div className="bg-purple-500 text-white p-4 flex-grow rounded-lg">
          <h3 className="font-bold">Drone info</h3>
          <p>Power: 75%</p>
          <p>Height: 20 M</p>
          <p>Time: 1:20 hrs</p>
          <p>Speed: 50 m/s</p>
          <p>Temperature: 29 C</p>
        </div>
        <div className="bg-purple-500 text-white p-4 flex-grow rounded-lg">
          <h3 className="font-bold">Objects detected</h3>
          <p>1. Names of objects here</p>
          <p>2. in the form of list</p>
        </div>
      </div>
    </div>
  );
};

export default MainContent;
