'use client'

import { get } from "@/app/api/restController";
import { Card, Typography } from "@mui/material";
import { useEffect, useState } from "react";
import { useUser } from "../ui/UserProvider";

export default function Page({params}: {params: {songName: string}}) {
    const [songData, setSongData] = useState<string>('Tribute')
    const [songName, setSongName] = useState<string>(`
        This is the greatest and best song in the world...
        Tribute.
        Long time ago me and my brother Kyle here,
        We was hitchhiking down a long and lonesome road.
        All of a sudden,
        There shined a shiny demon,
        In the middle of the road,
        And he said!
        Play the best song in the world, or I'll eat your souls...
        Well me and Kyle,
        We looked at each other,
        And we each said,
        Okay.
        And we played the first thing that came to our heads,
        Just so happened to be
        The best song in the world,
        It was the best song in the world.
        Look into my eyes and it's easy to see
        One and one makes two, two and one makes three,
        It was destiny.
        Once every hundred thousand years or so
        When the sun doth shine
        And the moon doth glow and the grass doth grow.
        Needless to say,
        The beast was stunned.
        Whip-crack went his whippy tail,
        And the beast was done.
        He asked us,
        Be you angels?
        And we said nay,
        We are but men,
        Rock!
        Ah, ah, ah, oh, wo, a-yo!
        This is not the greatest song in the world, no.
        This is just a tribute!
        Couldn't remember the greatest song in the world, yeah - no!
        This is a tribute!
        To the greatest song in the world,
        Alright!
        It was the greatest song in the world,
        Alright!
        This is the greatest motherfuckin' song, the greatest song in the world oh!
        And the peculiar thing is this my friends,
        The song we sang on that fateful night,
        It didn't actually sound anything like this song!
        This is just a tribute!
        You gotta believe me,
        And I wish you were there,
        Just a matter of opinion.
        Ah, ah, oh!
        Good God,
        Gotta love him,
        I'm so surprised to find ya can't stop him!
        Alright!
        Alright!
    `)

    const { token } = useUser();

    const getSong = async () => {
        const response = await get(`/audio_data/${params.songName}`, token) as any
        console.log(response.data)
        return response
    }
    

    useEffect(() => {
        const onWindowLoad = async () => {
            const response = await getSong()
            setSongName(response.name)
            setSongData(response.data)
        }
        onWindowLoad()
    }, [])

    return (
        <div className="p-20">
            <Card sx={{minHeight: 300, padding: 2}}>
                <Typography sx={{paddingBottom: 2}}>{songName}</Typography>
                <Typography>{songData}</Typography>
            </Card>
        </div>
    )
}