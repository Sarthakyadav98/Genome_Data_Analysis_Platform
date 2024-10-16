import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Pages/Home'
import AdminLogin from './Pages/adminname'
import AdminDashboard from './Pages/AdminDash';
const App = () => {
  return (
    <Routes>
      <Route path="/" element={<div class="text-3xl font-bold flex-1 text-center">    Project Started!  </div>} />
      <Route path ="/home" element = {<Home/>}></Route> 
      <Route path="/home/adminlogin" element={<AdminLogin />}></Route>
      <Route path="/home/adminlogin/admindash" element={<AdminDashboard />} />
    </Routes>
  )
}

export default App
