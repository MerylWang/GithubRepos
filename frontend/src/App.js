import './App.css';
import React, { useState } from 'react';

import UserFinder from './components/UserFinder';
import RepoBoard from './components/RepoBoard';

import Box from '@mui/material/Box';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import Grid from '@mui/material/Grid';


import { blueGrey, red } from '@mui/material/colors';
import { createTheme } from '@mui/material/styles';

// TODO: include option to view all repos 
// button View All Repos -> pass flag to use repos/ endpoint 
function App() {

  const theme = createTheme({
    palette: {
      primary: {
        light: blueGrey.A100,
        main: blueGrey.A400,
        dark: blueGrey.A700,
        contrastText: '#fff',
      },
      secondary: {
        light: red[50],
        main: red[100],
        dark: red[900],
        contrastText: '#000',
      },
    },
  });

  const [selectedUsername, setSelectedUsername] = useState("");

  const setUsername = (username) => {
    console.log('calling setUsername')
    setSelectedUsername(username)
  }

  return (
    // TODO center box 
    <Box sx={{ 
      width: '100%', 
      height: '100%',
      bgcolor: 'background.paper', 
      flexGrow:1
      }}>

      <AppBar position="static" color='primary'>
      <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Github Repo Explorer
          </Typography>
        </Toolbar>
      </AppBar>

      <Grid container spaing={2} padding={5}>
        <Grid item xs={4} padding={2}>
          <UserFinder 
            setUsername={setUsername}
          />
        </Grid>

        <Grid item xs={8} padding={2}>
          {/* TODO: make this separate column */}
          <RepoBoard 
            selectedUsername={selectedUsername}
          />
        </Grid>
      </Grid>
    </Box>

  );
}

export default App;
