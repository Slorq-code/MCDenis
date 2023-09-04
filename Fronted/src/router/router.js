import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { AuthRoutes } from '../modules/auth/routes/AuthRoutes';


function AppRouter() {
  return (
    <Router>
      <Routes>
        {/* Login y Registro */}
        <Route path="/auth/*" element={ <AuthRoutes /> } />
      </Routes>
    </Router>
  );
}

export default AppRouter;