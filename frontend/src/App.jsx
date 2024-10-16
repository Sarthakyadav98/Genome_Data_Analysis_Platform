import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from './Pages/Home'

const App = () => {
  return (
    <Routes>
      <Route path ="/" element = {<Home/>}></Route> 
      <Route path="/home" element={<div class="text-3xl font-bold flex-1 text-center">    Project Started!  </div>} />
    </Routes>
  )
}

export default App
