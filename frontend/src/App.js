import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Pages/Home';
import Trip from './Pages/Trip';
import TripProposal from './Pages/TripProposal';
import Header from './Components/Header';

function App() {
  return (
    <Router>
      {/* Components added within Router component will be display on every page */}
      <div className="main-page">
        <div className="main-container">
          <Header />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/trip/:id" element={<Trip />} />
            <Route path="/proposal/:id" element={<TripProposal />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
