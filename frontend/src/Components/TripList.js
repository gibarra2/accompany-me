import React from 'react';
import TripCard from './TripCard';
import Grid from '@mui/material/Grid';

const TripList = ({ tripList }) => {
  // Make TripCards for each trip a user has
  const makeCards = (tripList) => {
    return tripList.map((trip) => {
      let location = `${trip.city}, ${trip.country}`;
      let dates = `${trip.start_date} - ${trip.end_date}`;
      return (
        <Grid item xs={4}>
          <TripCard location={location} dates={dates} />
        </Grid>
      );
    });
  };

  return (
    <Grid container spacing={3} justifyContent="space-between">
      {makeCards(tripList)}
    </Grid>
  );
};

export default TripList;
