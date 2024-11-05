import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from './Pages/Home'
import ClientDashboard from './Pages/ClientDashboard'
import ScientistDashboard from './Pages/ScientistDashboard'
import SearchSpecies from './components/SearchSpecies'; // Import your new component
import GenomicData from './Components/GenomicData';
import CompareGenomicData from './Components/GenomicComparison';
import Feedback from './Components/Feedback';


const App = () => {
  return (
    <Routes>
      <Route path ="/" element = {<Home/>}></Route> 
      <Route path="/home" element={<div class="text-3xl font-bold flex-1 text-center">    Project Started!  </div>} />
      <Route path="/clientDashboard" element={<ClientDashboard />} />
      <Route path="/scientistDashboard" element={<ScientistDashboard />} />
      <Route path="/clientDashboard/searcherSpecies" element={<SearchSpecies />} />
      <Route path="/clientDashboard/searcherGenomicData" element={<GenomicData />} />
      <Route path="/clientDashboard/compareGenomicData" element={<CompareGenomicData />} />
      <Route path="/clientDashboard/Feedback" element = {<Feedback/> }/>

    </Routes>
  )
}

export default App;