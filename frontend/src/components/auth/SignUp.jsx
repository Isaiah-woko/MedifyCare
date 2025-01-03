import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import SocialLogin from './SocialLogin';

export default function SignUp() {
    const [role, setRole] = useState('patient');
    const handleRole = (e) => {
        setRole(e.target.value);
    }
    return (
        <>
            <main className="relative grow flex">
                <div className="w-full bg-slate-100">
                    <div className="h-full flex flex-col justify-center before:min-h-[4rem] md:before:min-h-[5rem] before:flex-1 after:flex-1">
                        <div className="px-4 sm:px-6">
                            <div className="w-full max-w-sm mx-auto">
                                <div className="py-16 md:py-20">
                                    <div className="mb-8">
                                        <h1 className="h2 font-uncut-sans text-primary">Sign Up</h1>
                                    </div>
                                    {/* Form */}
                                    <form>
                                        <div className="space-y-4">
                                            <div>
                                                <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="name">User Name <span className="text-red-500">*</span></label>
                                                <input id="name" className="form-input py-2 w-full" type="text" required />
                                            </div>
                                            <div>
                                                <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="email">Email <span className="text-red-500">*</span></label>
                                                <input id="email" className="form-input py-2 w-full" type="email" required />
                                            </div>
                                            <div>
                                                <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="password">Password</label>
                                                <input id="password" className="form-input py-2 w-full" type="password" autoComplete="on" required />
                                            </div>
                                            <div>
                                                <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="password">Confirm Password</label>
                                                <input id="password" className="form-input py-2 w-full" type="password" autoComplete="on" required />
                                            </div>
                                            <div>
                                                <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="role">Role <span className="text-red-500">*</span></label>
                                                <select onChange={handleRole} id="role" className="form-select py-2 w-full" required>
                                                    <option value="patient">Patient</option>
                                                    <option value="doctor">Doctor</option>
                                                </select>
                                            </div>
                                            {role === 'doctor' && (
                                                <>
                                                    <div>
                                                        <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="speciality">Speciality <span className="text-red-500">*</span></label>
                                                        <input id="speciality" className="form-input py-2 w-full" type="text" required />
                                                    </div>
                                                    <div>
                                                        <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="bio">Bio</label>
                                                        <textarea id="bio" className="form-textarea py-2 w-full" rows="4" required />
                                                    </div>
                                                    <div>
                                                        <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="image">Image</label>
                                                        <input id="image" className="form-input py-2 w-full" type="file" required />
                                                    </div>
                                                </>)}
                                        </div>
                                        <div className="mt-6">
                                            <button className="btn-sm text-white bg-gradient-to-t from-primary to-[#1d5f8f] hover:to-[#1a4d72] w-full shadow-lg group">
                                                Sign Up <span className="tracking-normal text-blue-200 group-hover:translate-x-0.5 transition-transform duration-150 ease-in-out ml-1">-&gt;</span>
                                            </button>
                                        </div>
                                    </form>
                                    <SocialLogin />
                                    <div className="text-sm text-gray-500 italic mt-6 mb-4">
                                        By filling out this form, I consent to the collection and use of my personal data.
                                    </div>
                                    <div className="pt-4 border-t border-primary">
                                        <div className="text-sm text-gray-400">
                                            Already have an account? <Link className="font-medium text-blue-500 hover:text-blue-400" to="/signin">Sign In</Link>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="hidden lg:block shrink-0 w-1/3 overflow-hidden before:bg-primary before:absolute before:inset-0 before:-z-10">
                    <div className="absolute left-1/2 -translate-x-1/2 pointer-events-none -z-10" aria-hidden="true">
                        <img src="{..}" className="max-w-none" alt="Hero Illustration" />
                    </div>
                    <div className="absolute left-1/2 -translate-x-1/2 pointer-events-none -z-10" aria-hidden="true">
                        <img src="{...}" className="max-w-none" alt="Auth Illustration" />
                    </div>
                </div>

            </main>
        </>
    )
}
