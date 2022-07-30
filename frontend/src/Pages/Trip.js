import React from 'react';
import { useParams } from 'react-router-dom';

const Trip = () => {
  let { id } = useParams();
  // Can use id variable to make api requests
  return (
    <>
      <p>This is the Trip page.</p>
    </>
  );
};

export default Trip;
