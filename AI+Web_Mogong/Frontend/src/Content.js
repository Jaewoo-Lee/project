import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';
import MainImage from './MainImage.js';

const useStyles = makeStyles(theme => ({
  root: {
    padding: theme.spacing(3, 2),
    textAlign : 'center',
  },
}));
export default function Content() {
  const classes = useStyles();
  return (
    <div>
      <Paper className={classes.root}>
        <Typography variant="h5" component="h3">
          사진 화질 높이기.
        </Typography>
        <Typography component="p">
          저화질의 사진을 고화질의 사진으로 바꿔보세요.
          하나의 사진만 가능합니다.
        </Typography>
        <br/>
        <br/>
        <MainImage></MainImage>
        <br/>
        <br/>
        <br/>
        <br/>
      </Paper>
    </div>
  );
}