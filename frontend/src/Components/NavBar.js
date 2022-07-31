import React from 'react';
import { Link } from 'react-router-dom';
import { useParams } from 'react-router-dom';
import '../styles/NavBar.css';
import Avatar from '@mui/material/Avatar';

const NavBar = () => {
  let { id } = useParams();
  return (
    <>
      <nav>
        <li>
          <Link to="/user/:id">Home</Link>
        </li>
        <li>
          <Avatar className="user-avatar">US</Avatar>
        </li>
      </nav>
    </>
  );
};

export default NavBar;
