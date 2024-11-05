import React from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';

const Navbar = () => {
  const navigate = useNavigate();
  const location = useLocation();

  // Function to handle logout
  const handleLogout = () => {
    // Add any necessary logout logic here (like clearing local storage or tokens)
    navigate('/'); // Redirect to the home page
  };

  // Determine whether to show the Search link or the Dashboard link
  const isOnSearchPage = location.pathname === '/clientDashboard/searcherSpecies';

  return (
    <nav className="bg-gray-800 p-4 text-white flex justify-between items-center">
      {/* Left Side: Conditional Link */}
      <div>
        <Link 
          to={isOnSearchPage ? '/clientDashboard' : '/clientDashboard/searcherSpecies'} 
          className="hover:underline text-xl"
        >
          {isOnSearchPage ? 'Home Page' : 'Search For A Species'}
        </Link>
      </div>

      {/* Middle: Title */}
      <h1 className="text-2xl font-bold">Genome Data Analysis Platform</h1>

      {/* Right Side: Logout Button */}
      <div>
        <button 
          onClick={handleLogout} 
          className="bg-red-500 hover:bg-red-600 text-white py-2 px-4 rounded"
        >
          Logout
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
