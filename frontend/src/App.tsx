import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import Home from './components/layouts/Home';
import Navbar from './components/shared/Navbar';

function App() {
  return (
    <BrowserRouter>
    <Navbar />
      <Switch>
        <Route component={Home} />
      </Switch>
    </BrowserRouter>
  );
}

export default App;
