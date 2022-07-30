import React from 'react';
import { useParams } from 'react-router-dom';

const TripProposal = () => {
  let { id } = useParams();
  return (
    <>
      <p>This is the TripProposal page.</p>
    </>
  );
};

export default TripProposal;
