'use client';

import NextLink from 'next/link'
import { Link as MUILink } from '@mui/material';

type linkProps = {
    link: string,
    content: string
} 

export default function Link(props: linkProps) {
    return (
        <NextLink href={props.link} passHref>
            <MUILink variant="body2">
                {props.content}
            </MUILink>
        </NextLink>
    );
}