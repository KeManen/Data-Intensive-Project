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
import { useUser } from '@/app/ui/UserProvider';
import { FormEvent } from 'react';
import { useRouter } from 'next/navigation';
import { put } from '../api/restController';

/**
 * 
 * Login page, layout inspiration from https://github.com/mui/material-ui/blob/v5.14.20/docs/data/material/getting-started/templates/sign-in/SignIn.tsx
 */

export default function Page() {
    const {login} = useUser();
    const {push} = useRouter();
    async function onSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()
 
        const formData = new FormData(event.currentTarget)
        
        const user = {
            user_name: formData.get("username"),
            password: formData.get("password")
        }

        
        await put('/login', user)
        .then(response => {
            console.log('GET Response:', response.data);
            const token = response.data
            login('' + user.user_name, token);
            push('/');
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
                        Sign in
                    </Typography>
                    <Box component="form" onSubmit={onSubmit} noValidate sx={{ mt: 1 }}>
                        <TextField
                        margin="normal"
                        required
                        fullWidth
                        id="username"
                        label="Username"
                        name="username"
                        autoComplete="username"
                        autoFocus
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
                        <Button
                        type="submit"
                        fullWidth
                        variant="contained"
                        sx={{ mt: 3, mb: 2 }}
                        >
                        Login
                        </Button>
                        <Grid container>
                        <Grid item>
                            <Link link='/register' content='No Account? Register here' />
                        </Grid>
                        </Grid>
                    </Box>
                    </Box>
                    <Copyright sx={{ mt: 8, mb: 4 }} />
                </Container>
            </Card>
            </Grid>            
        </Grid>  
    );
  }