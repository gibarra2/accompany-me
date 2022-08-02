import React from 'react';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { DatePicker } from '@mui/x-date-pickers';
import { useState, useEffect } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import format from 'date-fns/format';
import Chip from '@mui/material/Chip';
import '../styles/TripForm.css';

const TripForm = ({ userID, submitTrip }) => {
  const defaultState = {
    city: '',
    country: '',
    users: [],
    start_date: new Date(),
    end_date: new Date(),
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
    let formattedStartDate = format(formFields['start_date'], 'yyyy-MM-dd');
    let formattedEndDate = format(formFields['end_date'], 'yyyy-MM-dd');

    const requestBody = {
      ...formFields,
      start_date: formattedStartDate,
      end_date: formattedEndDate,
    };

    console.log(requestBody);
    submitTrip(userID, requestBody);
    setFormFields(defaultState);
  };

  const url = process.env.REACT_APP_DEV_SERVER_URL;

  const getUsers = () => {
    /*
      Gets all users for drop down menu. 
    */
    axios
      .get(`${url}/users/`)
      .then((response) => {
        let allUsers = response.data.map((user) => {
          return {
            label: `${user.first_name} ${user.last_name}`,
            id: user.id,
            value: user.id,
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
        onChange={(event, value) => {
          setFormFields({ ...formFields, users: getIDs(value) });
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
