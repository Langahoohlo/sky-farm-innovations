import Link from 'next/link';
import { SignedIn, SignOutButton, UserButton, UserProfile } from '@clerk/nextjs';
import { auth, currentUser } from '@clerk/nextjs/server';

function Sidebar () {
  // const user = await currentUser();

  // if(!user){
    // return new Response("Unauthorized", { status: 401 });
  // }

  return (
    <div className="bg-gray-800 text-white w-60 h-screen p-4">
      <div className="text-xl font-bold mb-4">SKYFARM INNOVATION</div>
      <nav className="flex flex-col space-y-4">
        <Link href="/dashboard" className="flex items-center space-x-2">
          <span>🏠</span><span>Dashboard</span>
        </Link>
        <Link href="/dashboard/mapping" className="flex items-center space-x-2">
          <span>🗺️</span><span>Mapping</span>
        </Link>
        <Link href="/dashboard/weather" className="flex items-center space-x-2">
          <span>☁️</span><span>Weather</span>
        </Link>
        <Link href="#" className="flex items-center space-x-2">
          <span>🛫</span><span>Control/ take a fly</span>
        </Link>
        <Link href="#" className="flex items-center space-x-2">
          <span>📅</span><span>Plan a Mission</span>
        </Link>
        <Link href="#" className="flex items-center space-x-2">
          <span>📊</span><span>Analysis</span>
        </Link>
        <Link href="#" className="flex items-center space-x-2">
          <span>🔍</span><span>Search</span>
        </Link>
      </nav>
      <div className='absolute bottom-4 left-4 border bg-white'>
        <SignedIn>
          <UserButton showName />
        </SignedIn>
      </div>
      
    </div>
  );
};

export default Sidebar;
