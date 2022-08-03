import React from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { LocalizationProvider, DatePicker } from '@mui/x-date-pickers';
import { useState, useEffect } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import format from 'date-fns/format';
import Chip from '@mui/material/Chip';
import '../styles/TripForm.css';

const TripForm = ({ userID, submitTrip, setOpenPopup }) => {
  let today = new Date();
  let tomorrow = new Date(today);
  tomorrow.setDate(tomorrow.getDate() + 1);

  const defaultState = {
    city: '',
    country: '',
    users: [],
    start_date: today,
    end_date: tomorrow,
  };

  const [users, setUsers] = useState([]);
  const [formFields, setFormFields] = useState(defaultState);

  const handleChange = (e) => {
    setFormFields({ ...formFields, [e.target.id]: e.target.value });
  };

  const getIDs = (values) => {
    /*
      Helper function to get user ID to submit in POST request. 
    */
    return values.map((value) => {
      return value.id;
    });
  };

  const submitTripData = (event) => {
    event.preventDefault();
    let formattedStartDate = format(formFields['start_date'], 'MM-dd-yyyy');
    let formattedEndDate = format(formFields['end_date'], 'MM-dd-yyyy');
    const userIDArray = getIDs(formFields.users);

    const requestBody = {
      ...formFields,
      start_date: formattedStartDate,
      end_date: formattedEndDate,
      users: userIDArray,
    };

    submitTrip(userID, requestBody);
    setFormFields(defaultState);
    setOpenPopup(false);
  };

  const url = process.env.REACT_APP_DEV_SERVER_URL;

  const getUsers = () => {
    /*
      Gets all users for drop down menu. 
    */
    axios
      .get(`${url}/users/`)
      .then((response) => {
        let allUsers = response.data
          .filter((user) => {
            return user.id !== parseInt(userID);
          })
          .map((user) => {
            return {
              label: `${user.first_name} ${user.last_name}`,
              id: user.id,
              value: `${user.first_name} ${user.last_name}`,
            };
          });
        setUsers(allUsers);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  useEffect(getUsers, []);

  return (
    <form className="newTripForm" onSubmit={submitTripData}>
      <TextField
        id="city"
        label="City"
        variant="filled"
        value={formFields.city}
        onChange={handleChange}
        required
      />
      <TextField
        id="country"
        label="Country"
        variant="filled"
        value={formFields.country}
        onChange={handleChange}
        required
      />
      <Autocomplete
        multiple
        id="users"
        options={users}
        renderInput={(params) => <TextField {...params} label="Users" />}
        value={formFields.users}
        onChange={(event, value) => {
          setFormFields({ ...formFields, users: value });
        }}
      />
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <DatePicker
          label="Start Date"
          value={formFields['start_date']}
          onChange={(newValue) => {
            setFormFields({ ...formFields, start_date: newValue });
          }}
          renderInput={(params) => <TextField {...params} />}
        />
        <DatePicker
          label="End Date"
          value={formFields['end_date']}
          onChange={(newValue) => {
            setFormFields({ ...formFields, end_date: newValue });
          }}
          renderInput={(params) => <TextField {...params} />}
        />
      </LocalizationProvider>
      <Button variant="contained" type="submit">
        Submit
      </Button>
    </form>
  );
};

export default TripForm;
