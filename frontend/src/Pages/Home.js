import React, { useEffect } from 'react';
import TripList from '../Components/TripList';
import { useParams, Link as RouterLink } from 'react-router-dom';
import Link from '@mui/icons-material/Link';

const Home = ({ getTrips }) => {
  let { id } = useParams();
  return (
    <>
      <h2>Upcoming Trips</h2>
      {/* Trip List gets rendered here */}
      <TripList />
    </>
  );
};

export default Home;
