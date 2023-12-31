import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import { ThemeProvider } from '@mui/material'
import theme from '@/app/ui/theme'
import NavBar from './ui/NavBar'
import UserProvider from '@/app/ui/UserProvider'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Music streaming service',
  description: 'Music streming with passion since 2023',
}



export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <ThemeProvider theme={theme}>
          <UserProvider>
            <NavBar></NavBar>
            {children}
          
          </UserProvider>
        </ThemeProvider>       
      </body>
    </html>
  )
}
