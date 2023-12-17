/**
 * This is a very basic 'AuthProvider', we basically just store the username to localstorage for safe keeping. some inspiration from https://stackoverflow.com/questions/71550567/how-to-make-useeffect-in-authprovider-runs-first-then-call-usecontext
 */


'use client'
import { Dispatch, SetStateAction, createContext, useContext, useEffect, useState } from 'react';

const getUser = () => {
    const user = localStorage.getItem('user')
    return user ? user : '';
}

interface IUserContext {
    user: String | null | undefined,
    isLoggedIn: boolean,
    login(username: string): void,
    logout(): void
}

 const userContext = createContext<IUserContext>({
    user: "",
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

    function login(username: string) {
        localStorage.setItem('user', username);
        setLoggedIn(true);
    };

    function logout() {
        localStorage.removeItem('user');
        setLoggedIn(false);
    };

    const [user, setUser]= useState('');
    const [isLoggedIn, setLoggedIn] = useState(false);

    useEffect(() => {
        const isUser = () => {
            let user = getUser();
            setUser(user);
            if (user != '') {
               setLoggedIn(true);
            }
        };

        isUser();
    }, [isLoggedIn]);

    return (
        <userContext.Provider value={{ isLoggedIn, login, logout, user }}>
        {children}
        </userContext.Provider>
    );
};

export default UserProvider;