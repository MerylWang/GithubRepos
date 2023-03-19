import React, { useState, useEffect } from 'react';

import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

import RepoCard from './RepoCard';


function RepoBoard(props) {
    const [repos, setRepos] = useState([])
    const selectedUsername = props.selectedUsername;

    // fetch data of repos to be displayed 
    useEffect(() => {
        // TODO: update this api, use props.selectedUsername to construct api endpoint
        // const REPOS_API = 'http://localhost:8000/repos/'
        // TODO: display all or no repos if no username selected 
        if (selectedUsername) {
            const REPOS_API = `http://localhost:8000/users/${selectedUsername}/repos`
            fetch(REPOS_API)
                .then((res) => res.json())
                .then((json) => {
                    setRepos(json)
                })
        } else {
            // reset board if username selection removed 
            setRepos([])
        }
    }, [selectedUsername])

    return (
        // TODO implement scrolling
        <Box sx={{ 
            // width: '50%', 
            height:'100%',
            // maxWidth: 360, 
            bgcolor: 'background.paper', 
            boxShadow:1, 
            }}
        >
            <Typography 
                color="text.secondary" 
                gutterBottom
                paddingLeft={2}
                paddingTop={2}
            >
                Repos
            </Typography>  
            <Grid container spaing={2}>
                {/* TODO: reduce number of cards per row when window width decreases */}
                {repos.map((repo) => (
                    <Grid item xs={4} padding={2}>
                         <RepoCard repo={repo} />
                    </Grid>
                ))}
            </Grid>
            
        </Box>
    )

}

export default RepoBoard