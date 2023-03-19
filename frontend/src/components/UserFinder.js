import React, { useState, useEffect } from 'react';

import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';

// TODO: highligh selected username 
// TODO: add a textbox that filters displayed usernames by input
// TODO: add button for removing selection  
function UserFinder(props) {
    const USERS_API = 'http://localhost:8000/users/'
    const [users, setUsers] = useState([])

    // fetch all users data
    useEffect(() => {
        fetch(USERS_API)
            .then((res) => res.json())
            .then((json) => {
                setUsers(json)
            })
    }, [])

    return (
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
                Select a user
            </Typography>
            {/* TODO: add key to each list element */}
            <List>
                {users.map((user) => ( 
                    <ListItemButton 
                        onClick={() => props.setUsername(user.username)}
                    >
                        <Link href={user.html_url}>{user.username}</Link>
                    </ListItemButton>                        
                ))}
            </List>
        </Box>
    )

}
// class UserFinder extends React.Component {
//     // REACT_APP_BASE_URL = process.env
//     // USERS_API = this.REACT_APP_BASE_URL + 'users/'
//     USERS_API = 'http://localhost:8000/users/'
    
//     // Constructor 
//     constructor(props) {
//         super(props);

//         this.state = {
//             users: [],
//             DataisLoaded: false
//         };

//         this.setUsername = this.props.setUsername;
//     }


//     componentDidMount() {
//         fetch(this.USERS_API)
//             .then((res) => res.json())
//             .then((json) => {
//                 this.setState({
//                     users: json,
//                     DataisLoaded: true
//                 });
//             })
//     }

//     render() {
//         const { DataisLoaded, users } = this.state;

//         return (
//             <Box sx={{ 
//                 width: '50%', 
//                 height:'100%',
//                 maxWidth: 360, 
//                 bgcolor: 'background.paper', 
//                 boxShadow:1, 
//                 }}
//             >
//                 <Typography 
//                     color="text.secondary" 
//                     gutterBottom
//                     paddingLeft={2}
//                     paddingTop={2}
//                 >
//                     Select a user
//                 </Typography>
                    
//                 <List>
//                     {users.map((user) => ( 
//                         <ListItemButton 
//                             onClick={() => this.setUsername(user.username)}
//                         >
//                             <Link href={user.html_url}>{user.username}</Link>
//                         </ListItemButton>                        
//                     ))}
//                 </List>
//             </Box>
//         )
//     }
// }

export default UserFinder