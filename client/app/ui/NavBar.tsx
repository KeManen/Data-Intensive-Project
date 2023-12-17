'use client'
import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import Container from '@mui/material/Container';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import HeadphonesIcon from '@mui/icons-material/Headphones';
import { useUser } from './UserProvider';
import Link from '@/app/ui/Link';

const actions = ['Logout'];

/*
This is a NavBar shown on top of the ui, design from https://mui.com/material-ui/react-app-bar/
*/

export default function NavBar() {

  const { user, logout, isLoggedIn } = useUser();
  
  const [anchorElUser, setAnchorElUser] = React.useState<null | HTMLElement>(null);

  const handleOpenUserMenu = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };
 
  const handleUserAction = (action: string) => {
    logout();
    handleCloseUserMenu();
  };

  return (
    <AppBar position="absolute">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
        <HeadphonesIcon color='primary' sx={{ml: 2}}></HeadphonesIcon>
        <Typography
            variant="h6"
            noWrap
            component="a"
            href="/"
            sx={{
              ml: 2,
              mr: 2,
              display: { xs: 'none', md: 'flex' },
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            Music streaming Service®
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
          </Box>
          <Typography
            variant="h5"
            noWrap
            component="a"
            href="/"
            sx={{
              mr: 2,
              display: { xs: 'flex', md: 'none' },
              flexGrow: 1,
              fontFamily: 'monospace',
              fontWeight: 700,
              letterSpacing: '.3rem',
              color: 'inherit',
              textDecoration: 'none',
            }}
          >
            Music streaming Service®
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
          </Box>

          {isLoggedIn 
          ? <Box sx={{ flexGrow: 0 }}>
           <Tooltip title="Open settings">
            <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
              {isLoggedIn ? user : ''}
            </IconButton>
          </Tooltip>
          <Menu
            sx={{ mt: '45px' }}
            id="menu-appbar"
            anchorEl={anchorElUser}
            anchorOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}
            keepMounted
            transformOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}
            open={Boolean(anchorElUser)}
            onClose={handleCloseUserMenu}
          >
            {actions.map((action) => (
              <MenuItem key={action} onClick={() => handleUserAction(action)}>
                <Typography textAlign="center">{action}</Typography>
              </MenuItem>
            ))}
          </Menu>

            
          </Box>
          : <Box sx={{ flexGrow: 0 }}>
            <Link link="/login" content='Login'/>
          </Box>
           }
        </Toolbar>
      </Container>
    </AppBar>
  );
}