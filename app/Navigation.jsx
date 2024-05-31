import Link from 'next/link';

const Navigation = () => {
  return (
    <nav>
      <ul>
        <li>
          <Link href="/weather">
            <a>Weather</a>
          </Link>
        </li>
        {/* Add other navigation links here */}
      </ul>
    </nav>
  );
};

export default Navigation;