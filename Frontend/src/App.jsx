import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from './components/Login'
import Dashboard from './components/Dashboard'
import Profile from './components/Profile'
import Leaderboard from './components/Leaderboard'
import Tips from './components/Tips'
import ForgotPassword from './components/ForgotPassword'
import React from 'react'
import SignUp from './components/Signup'
import DetailedReports from './components/DetailedReport'
function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/leaderboard" element={<Leaderboard />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/forgot" element={<ForgotPassword />} />
        <Route path="/tips" element={<Tips />} />
        <Route path="/detailed-report" element={<DetailedReports />} /> 
        
      </Routes>
    </Router>
  )
}

export default App
