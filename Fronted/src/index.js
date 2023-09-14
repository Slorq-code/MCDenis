import React from 'react';
import ReactDOM from 'react-dom/client';
import './styles/normalize.css';
import reportWebVitals from './reportWebVitals';
import AppRouter from './router/router'

import { Provider } from 'react-redux'
import store from './store/store';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={store}>
     <AppRouter />
    </Provider>
  </React.StrictMode>
);
reportWebVitals();
