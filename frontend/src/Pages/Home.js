import React, { useEffect } from 'react';
import TripList from '../Components/TripList';
import { useParams } from 'react-router-dom';
import Typography from '@mui/material/Typography';
import TripForm from '../Components/TripForm';

const Home = ({ getTrips, tripList }) => {
  let { userID } = useParams();

  useEffect(() => {
    getTrips(userID);
  }, []);

  return (
    <>
      <Typography variant="h4" margin={2}>
        Upcoming Trips
      </Typography>
      <TripList tripList={tripList} />
      <TripForm />
    </>
  );
};

export default Home;
