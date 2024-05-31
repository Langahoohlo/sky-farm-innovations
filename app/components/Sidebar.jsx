import Link from 'next/link';

const Sidebar = () => {

  return (
    <div className="bg-gray-800 text-white w-60 h-screen p-4">
      <div className="text-xl font-bold mb-4">SKYFARM INNOVATION</div>
      <nav className="flex flex-col space-y-4">
        <Link href="/" className="flex items-center space-x-2">
          <span>🏠</span><span>Dashboard</span>
        </Link>
        <Link href="/mapping" className="flex items-center space-x-2">
          <span>🗺️</span><span>Mapping</span>
        </Link>
        <Link href="/weather" className="flex items-center space-x-2">
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
      <div className="absolute bottom-4 left-4">
        <div>Name and username</div>
      </div>
    </div>
  );
};

export default Sidebar;
