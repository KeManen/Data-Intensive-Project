import { get } from "@/app/api/restController";
import { Typography } from "@mui/material";
import { Params } from "next/dist/shared/lib/router/utils/route-matcher";
import { useEffect, useState } from "react";

export default function Page({params}: {params: {songName: string}}) {
    const [songData, setSongData] = useState<string>('')

    const getSong = async () => {
        const response = await get(`/audio_data/${params.songName}`)
        console.log(response.data)
        return response.data
    }
    

    useEffect(() => {
        const onWindowLoad = async () => {
            const response = await getSong()
            const songData = setSongData(response)
        }
        onWindowLoad()
    }, [])

    return (
        <div>
            <Typography>{params.songName}</Typography>
            <Typography>{songData}</Typography>
        </div>
    )
}