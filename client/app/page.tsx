'use client'
import { useUser } from '@/app/ui/UserProvider';

export default function Home() {

  const  { isLoggedIn, user } = useUser();


  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>This is dashboard</div>
    </main>
  )
}
