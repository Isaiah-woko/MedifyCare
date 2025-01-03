import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Header from './components/Header';
import { useEffect } from 'react'

import AOS from 'aos'
import 'aos/dist/aos.css'
import SignIn from './components/auth/SignIn';
import SignUp from './components/auth/SignUp';
import ResetPasword from './components/auth/ResetPasword';

function App() {
  useEffect(() => {
    AOS.init({
      once: true,
      disable: 'phone',
      duration: 500,
      easing: 'ease-out-cubic',
    })
  })
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path='*' element={<h1>Not Found</h1>} />
        <Route path='/signin' element={<SignIn />} />
        <Route path='/signup' element={<SignUp />} />
        <Route path='/reset-password' element={<ResetPasword />} />
      </Routes>
    </Router>
  );
}

export default App;