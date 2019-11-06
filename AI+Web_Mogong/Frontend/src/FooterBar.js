import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

const useStyles = makeStyles(theme => ({
  root: {
    position : 'fixed',
    bottom : 0,
    width: '100%',
    height : '2.5rem',
    textAlign :'center',
  },
}));

export default function FooterBar() {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar variant="dense">
          <Typography variant="h6" color="inherit">
             
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}