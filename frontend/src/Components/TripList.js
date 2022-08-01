import React from 'react';
import TripCard from './TripCard';

const TripList = ({ tripList }) => {
  // Make TripCards for each trip a user has
  const makeCards = (tripList) => {
    return tripList.map((trip) => {
      let location = `${trip.city}, ${trip.country}`;
      let dates = `${trip.start_date} - ${trip.end_date}`;
      return <TripCard location={location} dates={dates} />;
    });
  };

  return <>{makeCards(tripList)}</>;
};

export default TripList;
