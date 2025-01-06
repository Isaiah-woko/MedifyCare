import { Link } from 'react-router-dom'

export default function CTA() {
  return (
    <section className="bg-primaryDark">
      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">
          <div className="relative max-w-3xl mx-auto text-center">
            <div className="relative">
              <h2 className="h2 font-playfair-display text-slate-100 mb-4">Your Health, Your Way</h2>
              <p className="text-xl text-slate-400 mb-8">Personalized care tailored to your needs.</p>
              <div>
                <Link className="btn text-white bg-secondaryDark hover:bg-secondary group" to="/consult">
                  Get Started Now <span className="tracking-normal text-blue-300 group-hover:translate-x-0.5 transition-transform duration-150 ease-in-out ml-1">-&gt;</span>
                </Link>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>
  )
}