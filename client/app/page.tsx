'use client'

import {Box, Button, Card, Grid, InputBase, TextField, Typography, alpha, styled } from "@mui/material";
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
type Song = {
	name: string
	data: string
}
type searchedSong = {
	song_name: string
}

export default function Home() {
	const [musicLibraryList, setMusicLibraryList] = useState<musicLibrary[]>([])
	const [searchResults, setSearchResults] = useState<searchedSong[]>([]);

  	const { token } = useUser();

	const getMusicLibrarys = async () => {
		try {
			const response = await get('/audio_collection/1', token);
			console.log('GET Response:', response.data);
			return response.data;
		} catch (error) {
			console.error('GET Error:', error);
			throw error;
		}
	};

	const searchSong = async (searchParam: string) => {
		try {
			const response = await get(`/songs?name=${searchParam}`, token) as any
			console.log('GET Response: ', response)
			return response
		} catch (error) {
			console.error('GET Error:', error);
			throw error;
		}
	}

	const addSong = async (inputSong: Song) => {
		try {
			const response = await post('/audio_data', inputSong, token);
			console.log('GET Response:', response.data);
			return response.data;
		} catch (error) {
			console.error('GET Error:', error);
			throw error;
		}
	};

	const handleSearch = async (event: FormEvent<HTMLFormElement>) => {
		event.preventDefault()

		const formData = new FormData(event.currentTarget)
		const searchParam: string | null = formData.get("search-param") as string;

		const response = await searchSong(searchParam)
		setSearchResults(response)
	};

	const handleInput = async (event: FormEvent<HTMLFormElement>) => {
		event.preventDefault()

		const formData = new FormData(event.currentTarget)
		const songName: string = formData.get("inputSongName") as string;
		const songWords: string | null = formData.get("inputSongWords") as string;

		const inputSong: Song = {
			name: songName,
			data: songWords
		}

		addSong(inputSong)
	}

	useEffect(() => {
		const onWindowLoad = async () => {
			const response = await getMusicLibrarys()
			setMusicLibraryList(response) 
		}
		onWindowLoad()
	}, [])

	return (
		<main className="p-2 pt-20">
			<Masonry columns={2} spacing={2}>
				<Card sx={{ height: 250, padding: 2,  maxWidth: 800}}>
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
						<Button href={`/${result.song_name}`} key={index}>{result.song_name}</Button>
					))}
				</Card>
				<Card sx={{height: 700, padding: 2}}>
					<Box sx={{maxWidth: 1300}}>
						<Grid container spacing={2}>
							{musicLibraryList.map((library) => (
								<Grid item xs={3} key={library.id}> 
									<Button href={`/library/${library.id}`}>
										<Card sx={{height: 100, width: 100, bgcolor: 'gray', padding: 1}}>
											{library.name}
										</Card>
									</Button>
								</Grid>
							))}
						</Grid>
					</Box>
				</Card>

				<Card sx={{height: 434, padding: 2, maxWidth: 800}}>
					<Typography >Input Song</Typography>
					<Box component='form' onSubmit={handleInput} noValidate sx={{ mt: 1 }}>
						<TextField 
							required
							id="input-song-name"
							name="inputSongName"
							sx={{width: 200}}
						/>
						<TextField 
							required
							multiline
							sx={{paddingY: 2, width: 700}}
							id="input-song-words"
							name="inputSongWords"
						/>
						<Button
							type="submit"
							variant="contained"
							sx={{ mt: 3, mb: 2 }}
						>Submit</Button>
					</Box>
				</Card>
			</Masonry>
		</main>
	)
}
