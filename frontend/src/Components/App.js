import './App.css';
import Login from "./Login";
import Navbar from './Navbar';
import ErrorPage from './ErrorPage';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import { Footer } from './Footer';

const router = createBrowserRouter([

  {
    path: '/',
    element: <Navbar />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: "/",
        element: <Login />,
      },
    ]
  }

])

function App() {
  return (
    <div className="App">
      <RouterProvider router={router} />
      {/* <Footer /> */}
    </div >
  );
}

export default App;
