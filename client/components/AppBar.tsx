import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { Avatar, Grid } from '@mui/material';
import { deepOrange } from '@mui/material/colors';

export default function MyAppBar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar sx={{padding: 2}}>
                <Grid container direction="row" justifyContent="flex-start">
                    <div className='pr-2'>
                        <Avatar sx={{ bgcolor: deepOrange[500] }}>N</Avatar>
                    </div>
                    <Typography variant="h5" sx={{paddingRight: 2}}>Music streaming service</Typography>
                    <Typography variant="h5" >Home</Typography>
                </Grid>
                <Grid container direction="row" justifyContent="flex-end">
                    <Button href="/register" sx={{padding: 2}}>Register</Button>
                    <Button href="/login" sx={{padding: 2}}>Login</Button>
                </Grid>
        </Toolbar>
      </AppBar>
    </Box>
  );
}