import {Link} from 'react-router-dom'
export default function Footer() {
  return (
    <footer>
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="grid sm:grid-cols-12 gap-8 py-8 md:py-12">
          <div className="sm:col-span-12 lg:col-span-4 lg:max-w-xs">
            <div className="mb-2">
              <Link href="/" className="inline-flex text-secondaryDark transition duration-150 ease-in-out" aria-label="Cruip">
                <img src='../assets/images/favicon-96x96.png' alt='logo'/>
              </Link>
            </div>
            <div className="text-lg font-bold text-slate-800">Connecting doctors and patients worldwide for quality healthcare.</div>
          </div>

          <div className="sm:col-span-6 md:col-span-4 lg:col-span-4">
            <h6 className="text-sm text-slate-800 font-semibold mb-2">Services</h6>
            <ul className="text-sm font-medium space-y-2">
              <li>
                <a href="#" className="text-slate-500 hover:text-secondaryDark transition duration-150 ease-in-out">Home Care Services</a>
              </li>
              <li>
                <a href="#" className="text-slate-500 hover:text-secondaryDark transition duration-150 ease-in-out">Online Medical Consultation</a>
              </li>
              <li>
                <a href="#" className="text-slate-500 hover:text-secondaryDark transition duration-150 ease-in-out">24/7 Doctor Chat Support</a>
              </li>
            </ul>
          </div>

          <div className="sm:col-span-6 md:col-span-4 lg:col-span-4">
            <h6 className="text-sm text-slate-800 font-semibold mb-2">Contact Us</h6>
            <ul className="text-sm font-medium space-y-2">
              <li>
                <a href="#" className="text-slate-500 hover:text-secondaryDark transition duration-150 ease-in-out">Email: support@MedifyCare.com</a>
              </li>
              <li>
                <a href="#" className="text-slate-500 hover:text-secondaryDark transition duration-150 ease-in-out">Phone: +1 234 567 890</a>
              </li>
            </ul>
          </div>


        </div>

        <div className="md:flex md:items-center md:justify-between py-6 md:py-8 border-t border-slate-200">

          <ul className="flex space-x-6 mb-4 md:order-1 md:ml-4 md:mb-0">
            <li>
              <a className="text-secondaryDark hover:text-secondary transition duration-150 ease-in-out" href="#0" aria-label="Twitter">
                <svg className="w-5 h-5 fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path d="m6.329 1 4.369 5.594L15.75 1h3.068L12.12 8.414 20 18.5h-6.172l-4.833-6.116L3.464 18.5H.395l7.169-7.928L0 1h6.329Zm-.925 1.684H3.583l11.093 14.04h1.7L5.404 2.684Z" />
                </svg>
              </a>
            </li>
            <li>
              <a className="text-secondaryDark hover:text-secondary transition duration-150 ease-in-out" href="#0" aria-label="Facebook">
                <svg className="w-5 h-5 fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path d="M20 10.025C20 4.491 15.52 0 10 0S0 4.491 0 10.025c0 4.852 3.44 8.892 8 9.825v-6.817H6v-3.008h2V7.52a3.508 3.508 0 0 1 3.5-3.509H14v3.008h-2c-.55 0-1 .45-1 1.002v2.005h3v3.008h-3V20c5.05-.501 9-4.772 9-9.975Z" />
                </svg>
              </a>
            </li>
            <li>
              <a className="text-secondaryDark hover:text-secondary transition duration-150 ease-in-out" href="#0" aria-label="Telegram">
                <svg className="w-5 h-5 fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path d="M19.96 2.336a.421.421 0 0 0-.291-.308 1.543 1.543 0 0 0-.788.054S1.358 8.194.358 8.87c-.215.145-.288.23-.324.33-.173.485.366.694.366.694l4.517 1.428a.506.506 0 0 0 .229-.013c1.026-.63 10.332-6.335 10.873-6.527.083-.024.148 0 .131.061-.215.732-8.257 7.664-8.301 7.706a.16.16 0 0 0-.06.143l-.422 4.28s-.176 1.331 1.196 0a38.082 38.082 0 0 1 2.374-2.11c1.553 1.041 3.224 2.192 3.945 2.794.245.23.576.354.916.342.426-.05.774-.35.876-.754 0 0 3.192-12.471 3.298-14.142.011-.162.025-.268.027-.38.005-.13-.008-.26-.04-.387Z" />
                </svg>
              </a>
            </li>
            <li>
              <a className="text-secondaryDark hover:text-secondary transition duration-150 ease-in-out" href="#0" aria-label="Github">
                <svg className="w-5 h-5 fill-current" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                  <path d="M10.041 0C4.52 0 0 4.612 0 10.25c0 4.526 2.845 8.37 6.862 9.737.502.085.669-.257.669-.513v-1.708c-2.761.598-3.347-1.367-3.347-1.367-.419-1.196-1.088-1.537-1.088-1.537-1.004-.598 0-.598 0-.598 1.004.085 1.506 1.025 1.506 1.025.92 1.537 2.343 1.11 2.929.854.084-.683.335-1.11.67-1.367-2.26-.256-4.603-1.11-4.603-5.039 0-1.11.419-2.05 1.004-2.733 0-.342-.418-1.367.168-2.733 0 0 .836-.257 2.76 1.025.838-.257 1.674-.342 2.511-.342.837 0 1.674.085 2.51.342 1.925-1.367 2.762-1.025 2.762-1.025.586 1.452.167 2.477.084 2.733.669.683 1.004 1.623 1.004 2.733 0 3.93-2.343 4.783-4.603 5.04.335.341.67.939.67 1.879v2.818c0 .256.167.598.67.513 4.016-1.367 6.86-5.21 6.86-9.737C20.084 4.612 15.565 0 10.042 0Z" />
                </svg>
              </a>
            </li>
          </ul>

          <div className="text-sm text-slate-500 mr-4">© MedifyCare. All rights reserved.</div>

        </div>

      </div>
    </footer>
  )
}
