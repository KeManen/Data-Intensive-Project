'use client';

import { ThemeOptions, createTheme } from '@mui/material/styles';

const colors: ThemeOptions = {
  palette: {
    mode: 'dark',
    primary: {
      main: '#3f51b5',
    },
    secondary: {
      main: '#f50057',
    },
    background: {
      default: '#121212',
    },
  }
};

const theme = createTheme(colors);

export const simpleTheme = {
  primary: {
    main: '#3f51b5',
  },
  secondary: {
    main: '#f50057',
  },
  background: {
    default: '#121212',
  },
}

export default theme;