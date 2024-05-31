const SignInForm = () => {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-100">
        <div className="bg-white p-8 rounded-lg shadow-lg w-80">
          <h2 className="text-2xl font-bold mb-6 text-center text-blue-700">Sign Up</h2>
          <form>
            <div className="mb-4">
              <label className="block mb-1">Username/ email</label>
              <input
                type="text"
                className="w-full px-3 py-2 border rounded text-black"
                placeholder="Username/ email"
              />
            </div>
            <div className="mb-4">
              <label className="block mb-1">Password</label>
              <input
                type="password"
                className="w-full px-3 py-2 border rounded text-black"
                placeholder="Password"
              />
            </div>
            <div className="text-right mb-4">
              <a href="#" className="text-blue-600 hover:underline">Forgot password?</a>
            </div>
            <button className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 transition">
              Sign Up
            </button>
            <div className="text-center mt-4">
              <p>
                Have an account?{' '}
                <a href="/signin" className="text-blue-600 hover:underline">Sign In</a>
              </p>
            </div>
          </form>
        </div>
      </div>
    );
  };
  
  export default SignInForm;
  