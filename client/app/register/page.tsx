'use client';

import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import Link from '@/app/ui/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Card from '@mui/material/Card';
import Copyright from '@/app/ui/copyright';

import { FormEvent, useState } from 'react';
import { get, post } from '../api/restController';
import { FormControl, MenuItem, Select, SelectChangeEvent } from '@mui/material';
import { Password } from '@mui/icons-material';

/**
 * 
 * Register page, layout inspiration from https://github.com/mui/material-ui/blob/v5.14.20/docs/data/material/getting-started/templates/sign-in/SignIn.tsx
 */

export default function Page() {
    const [region, setRegion] = useState<string>('')
    
    async function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()
 
        const userData = {
            username: event.currentTarget.username.value,
            password: event.currentTarget.password.value,
            region_name: event.currentTarget.region.value 
        }

        post('/audio_collection/1', userData)
        .then(response => {
            console.log('GET Response:', response.data);
        })
        .catch(error => {
            console.error('GET Error:', error);
        });
        
    }

    return (
        <Grid container spacing={0} direction='column' alignItems='center' justifyContent='center' sx={{minHeight: '100vh'}}>
            <Grid item xs={3}>
            <Card sx={{ maxWidth: 760, display: 'flex', alignItems: 'center', justifyContent: 'center'}}>
                <Container component="main" maxWidth="xs">
                    <CssBaseline />
                    <Box
                    sx={{
                        marginTop: 8,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                    }}
                    >
                    <Typography component="h1" variant="h5">
                        Register
                    </Typography>
                    <Box>
                        <form onSubmit={handleSubmit}>
                            <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            autoComplete="email"
                            autoFocus
                            />
                            <TextField
                            margin="normal"
                            required
                            fullWidth
                            id="username"
                            label="Username"
                            name="username"
                            autoComplete="username"                        
                            />
                            <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="password"
                            label="Password"
                            type="password"
                            id="password"
                            autoComplete="current-password"
                            />
                            <TextField
                            margin="normal"
                            required
                            fullWidth
                            name="password-verify"
                            label="Password again"
                            type="password"
                            id="password-verify"
                            autoComplete="current-password"
                            />
                            <Select
                                value={region}
                                name='region'
                                onChange={(event: SelectChangeEvent<string>) => setRegion(event.target.value)}
                                label="Select Option"
                            >
                                <MenuItem value="eu">EU</MenuItem>
                                <MenuItem value="us">US</MenuItem>
                            </Select>
                            <Button
                                type="submit"
                                fullWidth
                                variant="contained"
                                sx={{ mt: 3, mb: 2 }}
                            >
                            Register
                            </Button>
                            <Grid container>
                            <Grid item>
                                <Link link="/login" content='Already Have an account? Login here'/>
                            </Grid>
                            </Grid>
                        </form>
                    </Box>
                    </Box>
                    <Copyright sx={{ mt: 8, mb: 4 }} />
                </Container>
            </Card>
            </Grid>            
        </Grid>  
    );
  }