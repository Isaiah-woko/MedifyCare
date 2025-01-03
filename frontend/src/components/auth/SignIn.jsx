import { Link } from 'react-router-dom'
import SocialLogin from './SocialLogin';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';

const initialValues = {
    user_name:'',
    password:'',
}
const validationSchema = Yup.object({ 
    user_name: Yup.string().required('User Name is required to login'),
    password: Yup.string().required('Password is required to login'),
})
const onSubmit = (values) => {
    console.log(JSON.stringify(values, null, 2));
}

export default function SignIn() {
    return (
        <>
            <main className="relative grow flex">
                <div className="w-full bg-slate-100">
                    <div className="h-full flex flex-col justify-center before:min-h-[4rem] md:before:min-h-[5rem] before:flex-1 after:flex-1">
                        <div className="px-4 sm:px-6">
                            <div className="w-full max-w-sm mx-auto">
                                <div className="py-16 md:py-20">
                                    <div className="mb-8">
                                        <h1 className="h2 font-uncut-sans text-primary">Welcome Back!</h1>
                                    </div>
                                    {/* Form */}
                                    <Formik
                                        initialValues={initialValues}
                                        validationSchema={validationSchema}
                                        onSubmit={onSubmit}
                                        >
                                    <Form>
                                        <div className="space-y-4">
                                            <div>
                                                <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="user_name">User Name <span className="text-red-500">*</span></label>
                                                <Field id="user_name" name="user_name" className="form-input py-2 w-full" type="text" required />
                                                <ErrorMessage name="user_name" component="div" className="text-red-500 text-sm" />
                                            </div>
                                            <div>
                                                <div className="flex justify-between">
                                                    <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="password">Password <span className="text-red-500">*</span></label>
                                                    <Link className="text-sm font-medium text-blue-500 hover:text-blue-400 ml-2" to="/reset-password">Forget?</Link>
                                                </div>
                                                <Field id="password" name='password' className="form-input py-2 w-full" type="password" autoComplete="on" required />
                                                <ErrorMessage name="password" component="div" className="text-red-500 text-sm" />
                                            </div>
                                        </div>
                                        <div className="mt-6">
                                            <button type='submit' className="btn-sm text-white bg-gradient-to-t from-primary to-[#1d5f8f] hover:to-[#1a4d72] w-full shadow-lg group">
                                                Sign In <span className="tracking-normal text-blue-200 group-hover:translate-x-0.5 transition-transform duration-150 ease-in-out ml-1">-&gt;</span>
                                            </button>
                                        </div>
                                    </Form>
                                    </Formik>
                                    <SocialLogin />
                                    <div className="mt-6">
                                        <div className="text-sm text-gray-400">
                                            Don't you have an account? <Link className="font-medium text-blue-500 hover:text-blue-400" to="/signup">Sign Up</Link>
                                        </div>
                                    </div>
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
