import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
// import HomePage from '../modules/home/home';
// import { AuthRoutes } from '../modules/auth/routes/AuthRoutes';
import  Home from '../modules/home/home';
import LoginPage from '../modules/auth/pages/LoginPage';


function AppRouter() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={ <LoginPage /> } />
        <Route path="/" element={ <Home /> } />
      </Routes>
    </Router>
  );
}

export default AppRouter;