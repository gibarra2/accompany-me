import React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

const TripCard = () => {
  return (
    <>
      <Card sx={{ maxWidth: 400 }}>
        <CardActionArea>
          <CardMedia
            component="img"
            height="140"
            image="/pexels-oleksandr-pidvalnyi-1004584.jpg"
            alt="image of plane flying"
          />
          <CardContent>
            <Typography variant="h5">City Name</Typography>
            <Typography variant="h5" color="text.secondary">
              Dates of Travel
            </Typography>
          </CardContent>
        </CardActionArea>
      </Card>
    </>
  );
};

export default TripCard;
