import React from 'react'

export default function ResetPasword() {
    return (
        <>
            <main className="relative grow flex h-screen">
                {/* Content */}
                <div className="w-full bg-slate-100">
                    <div className="h-full flex flex-col justify-center before:min-h-[4rem] md:before:min-h-[5rem] before:flex-1 after:flex-1">
                        <div className="px-4 sm:px-6">
                            <div className="w-full max-w-sm mx-auto">
                                <div className="py-16 md:py-20">
                                    <div className="mb-8">
                                        <h1 className="h2 font-uncut-sans mb-4 text-primary">Reset password</h1>
                                        <p className="text-gray-400">Enter your email address. If an account exists, you'll receive an email with a password reset link soon.</p>
                                    </div>
                                    {/* Form */}
                                    <form>
                                        <div className="space-y-4">
                                            <div>
                                                <label className="block text-sm text-gray-400 font-medium mb-1" htmlFor="email">Email</label>
                                                <input id="email" className="form-input py-2 w-full" type="email" required />
                                            </div>
                                        </div>
                                        <div className="mt-6">
                                            <button className="btn-sm text-white bg-gradient-to-t from-primary to-[#1d5f8f] hover:to-[#1a4d72] w-full shadow-lg group">
                                                Reset Password <span className="tracking-normal text-blue-200 group-hover:translate-x-0.5 transition-transform duration-150 ease-in-out ml-1">-&gt;</span>
                                            </button>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="hidden lg:block shrink-0 w-1/3 overflow-hidden before:bg-primary before:absolute before:inset-0 before:-z-10">
                    <div className="absolute left-1/2 -translate-x-1/2 pointer-events-none -z-10" aria-hidden="true">
                        <img src="{..}" className="max-w-none" alt="Hero" />
                    </div>
                    <div className="absolute left-1/2 -translate-x-1/2 pointer-events-none -z-10" aria-hidden="true">
                        <img src="{...}" className="max-w-none" alt="Auth" />
                    </div>
                </div>

            </main>
        </>
    )
}
