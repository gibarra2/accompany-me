import React from 'react';
import { useParams, Link as RouterLink } from 'react-router-dom';
import Link from '@mui/icons-material/Link';

const Home = () => {
  let { id } = useParams();
  return (
    <>
      <p>This is the home page. down? </p>
    </>
  );
};

export default Home;
