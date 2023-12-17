'use client'

import {Box, Button, Card, Grid, InputBase, Link, List, ListItem, ListItemText, Typography, alpha, styled } from "@mui/material";
import Masonry from '@mui/lab/Masonry';
import SearchIcon from '@mui/icons-material/Search';
import { FormEvent, useEffect, useState } from "react";
import { get, post } from './api/restController';
import { useUser } from "./ui/UserProvider";

const Search = styled('div')(({ theme }) => ({
  width: 300,
  backgroundColor: alpha(theme.palette.common.white, 0.15),
  '&:hover': {
    backgroundColor: alpha(theme.palette.common.white, 0.25),
  }
}));

type musicLibrary = {
  name: string
  id: number
}

export default function Home() {
  const [musicLibraryList, setMusicLibraryList] = useState<string[]>([])
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState<string[]>([]);

  const { token } = useUser();

  const testList: musicLibrary[] = [
    {name: "Rock", id: 1}, 
    {name: "Pop", id: 2},
    {name: "Hip-hop", id: 3},
    {name: "Rap", id: 4},
  ]

  const getMusicLibrarys = async () => {
    await get('/audio_collection/1', token)
      .then(response => {
        console.log('GET Response:', response.data);
      })
      .catch(error => {
        console.error('GET Error:', error);
      });
  }

  const handleSearch = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault()
 
    const formData = new FormData(event.currentTarget)
    const searchParam = formData.get("search-param")

    await get(`/songs?name=${searchParam}`, token)
      .then(response => {
        console.log('GET Response:', response.data);
        setSearchResults(response.data)
      })
      .catch(error => {
        console.error('GET Error:', error);
      });
    
    //Testing
    const fakeSearchResults = ['Song 1', 'Song 2', 'Song 3'];
    setSearchResults(fakeSearchResults);
  };

  useEffect(() => {
    const onWindowLoad = () => {
      //const response =  getMusicLibrarys()
      getMusicLibrarys()
      //setMusicLibraryList(response) 
    }
    onWindowLoad()
  }, [])

  return (
    <main className="p-2 pt-20">
      <Masonry columns={2} spacing={2}>
      <Card sx={{ height: 250 }}>
        <Box component='form' onSubmit={handleSearch} noValidate sx={{ mt: 1 }}>
          <Search>
            <SearchIcon />
            <InputBase
              sx={{ paddingLeft: 1 }}
              placeholder="Search…"
              inputProps={{ 'aria-label': 'search' }}
              name="search-param"
            />
          </Search>
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
            >
            Search
          </Button>
        </Box>

        {searchResults.map((result, index) => (
          <Typography key={index}>{result}</Typography>
        ))}
    </Card>
        <Card sx={{height: 700}}>
          <div className="p-2">
            <Grid container spacing={2}>
              {testList.map((library) => (
                <Grid item xs={3} key={library.id}> 
                <Button href={`/library/${library.id}`}>
                  <Card sx={{height: 100, width: 100, bgcolor: 'gray'}}>
                    {library.name}
                  </Card>
                </Button>
              </Grid>
              ))}
            </Grid>
          </div>
        </Card>
        <Card sx={{height: 484}}>
          <Typography >Placeholder</Typography>
        </Card>
      </Masonry>
    </main>
  )
}
