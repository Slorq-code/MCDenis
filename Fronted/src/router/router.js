import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from '../modules/home/home';
import { AuthRoutes } from '../modules/auth/routes/AuthRoutes';


function AppRouter() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/auth/*" element={ <AuthRoutes /> } />
      </Routes>
    </Router>
  );
}

export default AppRouter;