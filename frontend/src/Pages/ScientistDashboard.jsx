import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../Components/ClientNav'; // Assuming you want a different navbar for scientists

const ScientistDashboard = () => {
  return (
    <div className="bg-gray-800 min-h-screen text-white">
      <Navbar />
      <div className="hero bg-gray-700 text-center py-20">
        <h1 className="text-5xl font-bold mb-4">Scientist Dashboard</h1>
        <p className="text-xl mb-8">Manage species data and genomic analysis.</p>
        <button className="bg-green-500 text-white py-3 px-6 rounded-full shadow-lg hover:bg-green-600 transition">
          Get Started
        </button>
      </div>
      <div className="p-10 space-y-6">
        <h2 className="text-3xl font-semibold mb-6">What would you like to do?</h2>

        {/* Functionality buttons */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Link to="/scientistDashboard/addSpecies" className="w-full">
            <button className="w-full bg-blue-600 text-white py-4 rounded-lg shadow-lg hover:bg-blue-700 transition">
              Add a New Species
            </button>
          </Link>

          <Link to="/scientistDashboard/updateGenomicData" className="w-full">
            <button className="w-full bg-green-600 text-white py-4 rounded-lg shadow-lg hover:bg-green-700 transition">
              Update Genomic Data
            </button>
          </Link>

          {/* Additional buttons for Scientist-specific functionalities */}
          <Link to="/scientistDashboard/addGenomicData" className="w-full">
            <button className="w-full bg-red-600 text-white py-4 rounded-lg shadow-lg hover:bg-red-700 transition">
              Add Genomic Data for a Species
            </button>
          </Link>
          <Link to="/scientistDashboard/compareGenomicData" className="w-full">
            <button className="w-full bg-purple-600 text-white py-4 rounded-lg shadow-lg hover:bg-purple-700 transition">
              Compare Genomic Data
            </button>
          </Link>

          <Link to="/scientistDashboard/evolutionaryHistory" className="w-full">
            <button className="w-full bg-yellow-600 text-white py-4 rounded-lg shadow-lg hover:bg-yellow-700 transition">
              Check Evolutionary History
            </button>
          </Link>

        </div>
      </div>
    </div>
  );
};

export default ScientistDashboard;
