import React from 'react'
import { Formik, Form, Field, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';


const initialValues = {
    password: '',
    password2: ''
}
const validationSchema = Yup.object({
    password: Yup.string().required('Enter a new password'),
    password2: Yup.string().oneOf([Yup.ref('password'), null], 'Passwords must match').required('Confirm your new password'),
});
const onSubmit = async (values, { setSubmitting, resetForm }) => {
    try {
        const response = await axios.post(`${process.env.REACT_APP_API_URL}/reset-password`, values);
        console.log('Response:', response);
        alert('Password reset successful');
    } catch (error) {
        console.error('Error:', error);
        alert('Error resetting password');
    } finally {
        setSubmitting(false);
        resetForm();
    }
};

export default function NewPassword() {
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
                                        <p className="text-gray-400">Enter your new password.</p>
                                    </div>
                                    {/* Form */}
                                    <Formik
                                        initialValues={initialValues}
                                        validationSchema={validationSchema}
                                        onSubmit={onSubmit}>
                                            {({ isSubmitting }) => (
                                        <Form>
                                            <div className="space-y-4">
                                                <div>
                                                    <div className="flex justify-between">
                                                        <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="password">Password <span className="text-red-500">*</span></label>
                                                    </div>
                                                    <Field id="password" name='password' className="form-input py-2 w-full" type="password" autoComplete="on" required />
                                                    <ErrorMessage name="password" component="div" className="text-red-500 text-sm" />
                                                </div>
                                                <div>
                                                    <div className="flex justify-between">
                                                        <label className="block text-sm text-gray-600 font-medium mb-1" htmlFor="password2">Confirm Password <span className="text-red-500">*</span></label>
                                                    </div>
                                                    <Field id="password2" name='password2' className="form-input py-2 w-full" type="password" autoComplete="on" required />
                                                    <ErrorMessage name="password2" component="div" className="text-red-500 text-sm" />
                                                </div>
                                            </div>
                                            <div className="mt-6">
                                                <button type='submit' className="btn-sm text-white bg-gradient-to-t from-primary to-[#1d5f8f] hover:to-[#1a4d72] w-full shadow-lg group">
                                                    Reset Password <span className="tracking-normal text-blue-200 group-hover:translate-x-0.5 transition-transform duration-150 ease-in-out ml-1">-&gt;</span>
                                                </button>
                                            </div>
                                        </Form>
                                            )}
                                    </Formik>
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
