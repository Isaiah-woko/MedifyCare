import React from 'react';
import { useSelector } from 'react-redux';

const Services = () => {
    const allServices = useSelector((state) => state.services.allSerices.services);

    return (
        <div>
            <section className="bg-slate-50">
                <div className="max-w-6xl mx-auto px-4 sm:px-6">
                    <div className="py-12 md:py-20">
                        <div className="max-w-3xl mx-auto text-center pb-12 md:pb-20">
                            <h2 className="h2 font-playfair-display text-slate-800 mt-3 mb-8">
                                Our Services
                            </h2>
                            <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
                                {allServices.map((service, index) => (
                                    <div key={index}
                                        data-aos="fade-up"
                                        data-aos-anchor="[data-aos-id-testimonials]"
                                        data-aos-delay={service.delay}
                                    >
                                        <div className="relative rounded-md shadow-md overflow-hidden">
                                            <div className="aspect-w-1 aspect-h-1 bg-cover" style={{
                                                width: '250px',
                                                height: '250px', backgroundImage: `url('../assets/images/${service.image}')`
                                            }}></div>
                                            <div className="p-4">
                                                <h3 className="text-base font-medium text-gray-900">{service.name}</h3>
                                                <p className="text-sm text-gray-500">{service.description}</p>
                                            </div>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            </section >

        </div >
    );
};

export default Services;
