import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './Pages/Home';
import Trip from './Pages/Trip';
import TripProposal from './Pages/TripProposal';

function App() {
  return (
    <Router>
      {/* Components added within Router component will be display on every page */}
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/trip/:id" element={<Trip />} />
        <Route path="/proposal/:id" element={<TripProposal />} />
      </Routes>
    </Router>
  );
}

export default App;
