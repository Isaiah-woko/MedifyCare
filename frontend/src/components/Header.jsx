import React from 'react'
import { Link } from 'react-router-dom'

export default function Header() {
  return (
    <header className="absolute w-full z-30">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="flex items-center justify-between h-16 md:h-20">
          <div className="shrink-0 mr-4 flex items-center ">
            <Link className="block" to="/" aria-label="Cruip">
              <img src='../assets/images/web-app-manifest-192x192.png' alt='logo' className='w-24'/>
            </Link>
            <div>MEDIFYCARE</div>
          </div>

          <nav className="flex grow">
            <ul className="flex grow justify-end flex-wrap items-center">
              <li>
                <Link className="font-medium text-gray-400 hover:text-secondary px-3 lg:px-5 py-2 flex items-center transition duration-150 ease-in-out" to="/signin">Sign in</Link>
              </li>
              <li>
                <Link className="font-medium text-gray-400 hover:text-secondary px-3 lg:px-5 py-2 flex items-center transition duration-150 ease-in-out" to="/signup">Sign Up</Link>
              </li>
              <li className="ml-3">
                <Link className="btn-sm text-white bg-gradient-to-t from-secondaryDark to-secondaryLight hover:to-secondary w-full shadow-lg group" to="#0">
                  Get Started <span className="tracking-normal text-blue-200 group-hover:translate-x-0.5 transition-transform duration-150 ease-in-out ml-1">-&gt;</span>
                </Link>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </header>
  );
}
