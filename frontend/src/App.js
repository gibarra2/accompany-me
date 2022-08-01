import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Pages/Home';
import Trip from './Pages/Trip';
import TripProposal from './Pages/TripProposal';
import Header from './Components/Header';
import { useState, useEffect } from 'react';
import axios from 'axios';
import TripCard from './Components/TripCard';

function App() {
  const [tripList, setTripList] = useState({});

  const url = 'http://localhost:3000';

  const getTrips = (userID) => {
    axios
      .get(`${url}/users/${userID}/trips`)
      .then((response) => {
        console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <Router>
      {/* Components added within Router component will be display on every page */}
      <div className="main-page">
        <div className="main-container">
          <Header />
          <Routes>
            <Route path="/user/:id" element={<Home getTrips={getTrips} />} />
            <Route path="/trip/:id" element={<Trip />} />
            <Route path="/proposal/:id" element={<TripProposal />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
