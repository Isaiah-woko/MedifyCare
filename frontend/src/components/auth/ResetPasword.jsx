import { Field, Form, Formik } from 'formik'
import React from 'react'
import * as Yup from 'yup'
import axios from 'axios'

export default function ResetPasword() {
    const initialValues = {
        email: '',
    };
    const validationSchema = Yup.object({
        email: Yup.string()
            .email('Invalid email address')
            .required('Email is required'),
    });
    const onSubmit = async (values, { setSubmitting, resetForm }) => {
        try {
            const response = await axios.post(`${process.env.REACT_APP_API_URL}/reset_password/<token>/<int:user_id>`, values);
            console.log('Server Response:', response.data);
            alert('Reset password email sent successfully!');
        } catch (error) {
            console.error('Error submitting form:', error);
            alert('Error submitting form');
        } finally {
            setSubmitting(false);
            resetForm();
        }
    };
    return (
        <>
            <main className="relative grow flex h-screen">
                <div className="w-full bg-light">
                    <div className="h-full flex flex-col justify-center before:min-h-[4rem] md:before:min-h-[5rem] before:flex-1 after:flex-1">
                        <div className="px-4 sm:px-6">
                            <div className="w-full max-w-sm mx-auto">
                                <div className="py-16 md:py-20">
                                    <div className="mb-8">
                                        <h1 className="h2 font-uncut-sans mb-4 text-black">Reset password</h1>
                                        <p className="text-gray-400">Enter your email address. If an account exists, you'll receive an email with a password reset link soon.</p>
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
                                                        <label className="block text-sm text-gray-400 font-medium mb-1" htmlFor="email">Email</label>
                                                        <Field id="email" name='email' className="form-input py-2 w-full" type="email" required />
                                                    </div>
                                                </div>
                                                <div className="mt-6">
                                                    <button type='submit' className="btn-sm text-white bg-gradient-to-t from-primary to-primaryLight hover:to-primaryDark w-full shadow-lg group">
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

                <div className="hidden lg:block shrink-0 w-2/5 overflow-hidden before:bg-primary before:absolute before:inset-0 before:-z-10">
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
