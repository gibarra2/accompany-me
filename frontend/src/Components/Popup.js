import React from 'react';
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';

const Popup = ({ title, children, openPopup, setOpenPopup }) => {
  return (
    <Dialog open={openPopup} maxWidth="md">
      <DialogTitle>
        <div style={{ display: 'flex' }}>
          <Typography
            variant="h6"
            component="div"
            style={{ flexGrow: 1, justifyContent: 'center' }}
          >
            {title}
          </Typography>
          <IconButton onClick={() => setOpenPopup(false)}>
            <CloseIcon />
          </IconButton>
        </div>
      </DialogTitle>
      <DialogContent dividers>
        <div>{children}</div>
      </DialogContent>
    </Dialog>
  );
};

export default Popup;
