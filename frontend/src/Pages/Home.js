import React, { useEffect } from 'react';
import TripList from '../Components/TripList';
import { useParams } from 'react-router-dom';
import Typography from '@mui/material/Typography';

const Home = ({ getTrips, tripList }) => {
  let { userID } = useParams();

  console.log(userID);

  useEffect(() => {
    getTrips(userID);
  }, []);

  return (
    <>
      <Typography variant="h4" margin={2}>
        Upcoming Trips
      </Typography>
      <TripList tripList={tripList} />
    </>
  );
};

export default Home;
