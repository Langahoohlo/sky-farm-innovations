
export default function Home() {
    return (
      <div className="flex flex-col items-center min-h-screen bg-blue-900 text-white p-4">
        <div className="w-full max-w-md">
          <header className="text-center mb-4">
            <h1 className="text-2xl font-bold">SkyFarm Drone</h1>
            <div className="mt-2 bg-gray-300 text-gray-700 rounded p-2">Drone connected</div>
          </header>
  
          <main className="bg-white text-black rounded p-4 mb-4">
            <div className="relative h-64 mb-4 bg-gray-200 flex items-center justify-center">
              <span className="absolute top-2 left-2">
                <button className="bg-gray-700 text-white p-2 rounded">📍</button>
              </span>
              <span className="absolute top-2 right-2">
                <button className="bg-gray-700 text-white p-2 rounded">🎥</button>
              </span>
              <span>MAP / VIDEO</span>
            </div>
  
            <div className="text-center font-bold mb-4">Readings from the drone</div>
  
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-blue-400 p-4 rounded">
                <div className="font-bold">Power</div>
                <div className="text-2xl">80%</div>
              </div>
              <div className="bg-purple-400 p-4 rounded">
                <div className="font-bold">Time Taken</div>
                <div className="text-2xl">1:30:03 sec</div>
              </div>
              <div className="bg-blue-400 p-4 rounded">
                <div className="font-bold">Objects Detected</div>
                <div className="text-2xl">5</div>
                <button className="mt-2 bg-gray-700 text-white p-2 rounded">View</button>
              </div>
              <div className="bg-blue-400 p-4 rounded">
                <div className="font-bold">Soil info</div>
                <div className="text-xl">Type: loam soil</div>
              </div>
            </div>
          </main>
        </div>
      </div>
    );
  }
  