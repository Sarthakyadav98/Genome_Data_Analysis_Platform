import React, { useState, useEffect } from 'react';

const Navbar = () => {
  const [currentTime, setCurrentTime] = useState(new Date().toLocaleTimeString('en-GB', { hour12: false }));

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentTime(new Date().toLocaleTimeString('en-GB', { hour12: false }));
    }, 1000);

    // Clean up interval on unmount
    return () => clearInterval(interval);
  }, []);

  return (
    <nav className="w-full flex justify-between items-center py-4 bg-gray-800 text-white px-10">
      {/* Home Button on the Left */}
      <div>
        <a href="/" className="text-xl font-bold">Home</a>
      </div>

      {/* Middle Content */}
      <div className="text-xl font-semibold">
        Welcome to Genome Platform
      </div>

      {/* Time on the Right */}
      <div className="text-xl">
        {currentTime}
      </div>
    </nav>
  );
};

export default Navbar;
