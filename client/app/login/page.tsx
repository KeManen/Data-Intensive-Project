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
import { FormEvent, useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { post } from '../api/restController';

/**
 * 
 * Login page, layout inspiration from https://github.com/mui/material-ui/blob/v5.14.20/docs/data/material/getting-started/templates/sign-in/SignIn.tsx
 */

type User = {
    user_name: string | null,
    password: string | null
}

export default function Page() {
    const [token, setToken] = useState<string>()
    const {login} = useUser();
    const {push} = useRouter();

    const tryToLogin = async (user: User) => {
        try {
            const response = await post('/login', user) as any
            console.log('POST Response:', response["auth_token"]);
            const token = response["auth_token"]; // Use optional chaining to handle undefined
            setToken(token)
            return token
        } catch (error) {
            console.error('GET Error:', error);
            throw error;
        }
    };
    
    async function onSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault()
 
        const formData = new FormData(event.currentTarget)
        
        const user = {
            user_name: formData.get("username") as string,
            password: formData.get("password") as string
        }

        const token = await tryToLogin(user)
        console.log(token);
        if (token) {
            console.log(token);
            login('' + user.user_name, token);
            // Redirect or perform any necessary action after successful login
            // push('/');
        } else {
            console.error('Auth token not found in the response.');
        }

        /*await post('/login', user)
        .then(response => {
            console.log('POST Response:', response);
            const token = response.data?.auth_token || ''; // Use optional chaining to handle undefined
            console.log(token);
            if (token) {
                login('' + user.user_name, token);
                console.log(token);
                // Redirect or perform any necessary action after successful login
                // push('/');
            } else {
                console.error('Auth token not found in the response.');
            }
        })
        .catch(error => {
            console.error('POST Error:', error);
        });*/

    }

    useEffect(() => {
        console.log('Token', token)
    }, [token])

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