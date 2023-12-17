/**
 * This is a very basic 'AuthProvider', we basically just store the username to localstorage for safe keeping. some inspiration from https://stackoverflow.com/questions/71550567/how-to-make-useeffect-in-authprovider-runs-first-then-call-usecontext
 */


'use client'
import { createContext, useContext, useEffect, useState } from 'react';

const getUser = () => {
    const user = localStorage.getItem('user')
    return user ? user : '';
}

const getToken = () => {
    const token = localStorage.getItem('token');
    return token ? token : '';
}

interface IUserContext {
    user: String | null | undefined,
    token: string,
    isLoggedIn: boolean,
    login(username: string, token: string): void,
    logout(): void
}

 const userContext = createContext<IUserContext>({
    user: "",
    token: "",
    isLoggedIn: false,
    login: (username: string) => {},
    logout: () => {},
  });

export const useUser = () => useContext(userContext);

const UserProvider = ({
    children,
  }: {
    children: React.ReactNode
  }) => {

    function login(username: string, token: string) {
        localStorage.setItem('user', username);
        localStorage.setItem('token', token);
        setLoggedIn(true);
    };

    function logout() {
        localStorage.removeItem('user');
        localStorage.removeItem('token');
        setLoggedIn(false);
    };

    const [user, setUser]= useState('');
    const [token, setToken]= useState('');
    const [isLoggedIn, setLoggedIn] = useState(false);

    useEffect(() => {
        const isUser = () => {
            let user = getUser();
            let token = getToken();
            setUser(user);
            setToken(token);
            if (user != '' && token != '') {
               setLoggedIn(true);
            }
        };

        isUser();
    }, [isLoggedIn]);

    return (
        <userContext.Provider value={{ isLoggedIn, login, logout, user, token }}>
        {children}
        </userContext.Provider>
    );
};

export default UserProvider;