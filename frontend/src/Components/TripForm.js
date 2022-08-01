import React from 'react';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { AdapterLuxon } from '@mui/x-date-pickers/AdapterLuxon';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { DatePicker } from '@mui/x-date-pickers';
import { useState, useEffect } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import Chip from '@mui/material/Chip';

const TripForm = () => {
  const [users, setUsers] = useState([]);
  const [date, setDate] = useState(new Date());
  const [formFields, setFormFields] = useState({
    city: '',
    country: '',
    users: [],
    start_date: new Date(),
    end_date: new Date(),
  });

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

  const url = process.env.REACT_APP_DEV_SERVER_URL;

  const getUsers = () => {
    axios
      .get(`${url}/users/`)
      .then((response) => {
        console.log(response.data);
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
    <Stack spacing={3} sx={{ width: 300 }} component="form">
      {/* <form> */}
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
        onChange={
          (event, value) => {
            setFormFields({ ...formFields, users: getIDs(value) });
          }
          // setFormFields({ ...formFields, users: [...formFields.users] })
        }
      />
      <LocalizationProvider dateAdapter={AdapterLuxon}>
        <DatePicker
          label="Start Date"
          value={formFields['start_date']}
          onChange={(newValue) => {
            setDate(newValue);
          }}
          renderInput={(params) => <TextField {...params} />}
        />
        <DatePicker
          label="End Date"
          value={formFields['end_date']}
          onChange={(newValue) => {
            setDate(newValue);
          }}
          renderInput={(params) => <TextField {...params} />}
        />
      </LocalizationProvider>
      <Button variant="contained" type="submit">
        Submit
      </Button>
      {/* </form> */}
    </Stack>
  );
};

export default TripForm;
