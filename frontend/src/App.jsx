import React from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import Doctors from './pages/Doctors'
import Login from './pages/Login'
import About from './pages/About'
import Appointments from './pages/Appointments'
import My_Profile from './pages/My_Profile'
import Navbar from './components/Navbar'
import Ai from './pages/Ai'
import Prediction from './pages/Prediction'

function App() {
  return (
    <div className='mx-4 sm:mx-[10%]'>
      <Navbar/>
      <Routes>
        <Route path ='/' element={<Home />}/>
        <Route path = '/doctors' element={<Doctors/>}/>
        <Route path = '/doctors/:speciality' element={<Doctors/>}/>
        <Route path = '/login' element={<Login/>}/>
        <Route path = '/about' element={<About/>}/>
        <Route path ='/appointments' element={<Appointments/>}/>
        <Route path ='/appointments:docId' element={<Appointments/>}/>
        <Route path='/ai' element={<Ai/>} />
        <Route path ='/profile' element = {<My_Profile/>}/>
        <Route path='/prediction' element={<Prediction/>} />
      </Routes>
    </div>
  )
}

export default App
