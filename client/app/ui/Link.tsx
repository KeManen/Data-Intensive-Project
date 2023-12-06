'use client';


import NextLink from 'next/link'
import { simpleTheme } from '@/app/ui/theme';

type linkProps = {
    link: string,
    content: string
} 

export default function Link(props: linkProps) {

    return (
        <NextLink href={props.link}>
            <p style={{color: simpleTheme.primary.main, textDecoration: 'underline'}}>{props.content}</p>
        </NextLink>
    );
}