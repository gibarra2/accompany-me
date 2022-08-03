import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import TripList from '../Components/TripList';
import Popup from '../Components/Popup';
import Typography from '@mui/material/Typography';
import TripForm from '../Components/TripForm';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import AddIcon from '@mui/icons-material/Add';

const Home = ({ getTrips, tripList, submitTrip }) => {
  let { userID } = useParams();
  const [toggleForm, setToggleForm] = useState(false);

  useEffect(() => {
    getTrips(userID);
  }, []);

  return (
    <>
      <Stack
        direction="row"
        justifyContent="space-between"
        alignItems="center"
        mt={2}
        mb={2}
      >
        <Typography variant="h4">Where I'm Going</Typography>
        <Button
          variant="contained"
          size="large"
          startIcon={<AddIcon />}
          onClick={() => setToggleForm(true)}
        >
          Add Trip
        </Button>
      </Stack>
      <TripList tripList={tripList} />
      <Popup
        title="Add Trip"
        openPopup={toggleForm}
        setOpenPopup={setToggleForm}
        children={
          <TripForm
            userID={userID}
            submitTrip={submitTrip}
            setOpenPopup={setToggleForm}
          />
        }
      />
    </>
  );
};

export default Home;
