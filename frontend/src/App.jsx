import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from './Pages/Home'

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<div class="text-3xl font-bold flex-1 text-center">    Project Started!  </div>} />
      <Route path ="/home" element = {<Home/>}></Route> 
    </Routes>
  )
}

export default App
