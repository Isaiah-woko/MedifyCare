import { Link } from 'react-router-dom'
import SocialLogin from './SocialLogin';
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';

const initialValues = {
    email: '',
    password: '',
}
const validationSchema = Yup.object({
    email: Yup.string().required('Email is required to login'),
    password: Yup.string().required('Password is required to login'),
})
const onSubmit = async (values, { setSubmitting, resetForm }) => {
    try {
        const response = await axios.post(`${process.env.REACT_APP_API_URL}/login`, values);
        console.log('Server Response:', response.data);
        alert('Form submitted successfully!');
    } catch (error) {
        console.error('Error submitting form:', error);
        alert('Error submitting form');
    } finally {
        setSubmitting(false);
        resetForm();
    }
};

export default function SignIn() {
    return (
        <>
            <main className="relative grow flex">
                <div className="w-full bg-light">
                    <div className="h-full flex flex-col justify-center before:min-h-[4rem] md:before:min-h-[5rem] before:flex-1 after:flex-1">
                        <div className="px-4 sm:px-6">
                            <div className="w-full max-w-sm mx-auto">
                                <div className="py-16 md:py-20">
                                    <div className="mb-8">
                                        <h1 className="h2 font-uncut-sans text-black">Welcome Back!</h1>
                                    </div>
                                    <Formik
                                        initialValues={initialValues}
                                        validationSchema={validationSchema}
                                        onSubmit={onSubmit}
                                    >
                                        {({ isSubmitting }) => (
                                            <Form>
                                                <div className="space-y-4">
                                                    <div>
                                                        <div>
                                                            <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="email">Email <span className="text-red-500">*</span></label>
                                                            <Field id="email" name='email' className="form-input py-2 w-full" type="email" required />
                                                        </div>
                                                        <ErrorMessage name="email" component="div" className="text-red-500 text-sm" />
                                                    </div>
                                                    <div>
                                                        <div className="flex justify-between">
                                                            <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="password">Password <span className="text-red-500">*</span></label>
                                                            <Link className="text-sm font-medium text-secondary hover:text-secondaryLight ml-2" to="/reset-password">Forget?</Link>
                                                        </div>
                                                        <Field id="password" name='password' className="form-input py-2 w-full" type="password" autoComplete="on" required />
                                                        <ErrorMessage name="password" component="div" className="text-red-500 text-sm" />
                                                    </div>
                                                </div>
                                                <div className="mt-6">
                                                    <button type='submit' className="btn-sm text-white bg-gradient-to-t from-primary to-primaryLight hover:to-primaryDark w-full shadow-lg group">
                                                        Sign In <span className="tracking-normal text-blue-200 group-hover:translate-x-0.5 transition-transform duration-150 ease-in-out ml-1">-&gt;</span>
                                                    </button>
                                                </div>
                                            </Form>
                                        )}
                                    </Formik>
                                    <SocialLogin />
                                    <div className="mt-6">
                                        <div className="text-sm text-gray-400">
                                            Don't you have an account? <Link className="font-medium text-secondary hover:text-secondaryLight" to="/signup">Sign Up</Link>
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
