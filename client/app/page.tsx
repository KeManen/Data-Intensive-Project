'use client'

import {Box, Button, Card, Grid, InputBase, Typography, alpha, styled } from "@mui/material";
import Masonry from '@mui/lab/Masonry';
import SearchIcon from '@mui/icons-material/Search';
import { useEffect, useState } from "react";
import { get, post } from './api/restController';

const Search = styled('div')(({ theme }) => ({
  width: 300,
  backgroundColor: alpha(theme.palette.common.white, 0.15),
  '&:hover': {
    backgroundColor: alpha(theme.palette.common.white, 0.25),
  }
}));

const musicLibraryList = ["Rock", "Pop", "Hip-hop", "Rap", "Jazz", "Blues", "Country", "Electronic", "Classical", "Reggae", "Metal", "Indie"]

export default function Home() {
  const [musicLibraryList, setMusicLibraryList] = useState<string[]>([])

  const getMusicLibrarys = () => {
    get('/audio_collection/1')
      .then(response => {
        console.log('GET Response:', response.data);
      })
      .catch(error => {
        console.error('GET Error:', error);
      });
  }


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
        <Card sx={{height: 200}}>
          <Search>
            <SearchIcon/>
            <InputBase
              sx={{paddingLeft: 1}}
              placeholder="Search…"
              inputProps={{ 'aria-label': 'search' }}
            />
          </Search>
        </Card>
        <Card sx={{height: 700}}>
          <div className="p-2">
            <Grid container spacing={2}>
              {musicLibraryList.map((musicLibraryName, index) => (
                <Grid item xs={4} key={index}> 
                <Card sx={{height: 100, width: 100}}>
                  {musicLibraryName}
                </Card>
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
