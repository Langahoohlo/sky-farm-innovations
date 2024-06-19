import Sidebar from '../../components/Sidebar';

const Weather = () => {
  return (
    <div className="flex">
      <Sidebar />
      <div className="p-4 flex-1">
        <h1 className="text-2xl font-bold mb-4">Weather</h1>
        <p>This is the weather page.</p>
      </div>
    </div>
  );
};

export default Weather;
