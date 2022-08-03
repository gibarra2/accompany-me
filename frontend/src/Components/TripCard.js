import React from 'react';
import { useNavigate } from 'react-router-dom';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

const TripCard = ({ location, dates, tripID }) => {
  const navigate = useNavigate();
  return (
    <>
      <Card sx={{ maxWidth: 400 }} onClick={() => navigate(`trip/${tripID}`)}>
        <CardActionArea>
          <CardMedia
            component="img"
            height="140"
            image="/pexels-oleksandr-pidvalnyi-1004584.jpg"
            alt="image of plane flying"
          />
          <CardContent>
            <Typography variant="h5">{location}</Typography>
            <Typography variant="h6" color="text.secondary">
              {dates}
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </>
  );
};

export default TripCard;
