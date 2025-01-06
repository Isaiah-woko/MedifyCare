import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import doctors from '../api/doctors.json';

export default function Consult() {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedRole, setSelectedRole] = useState('All');
  const navigate = useNavigate();

  const filteredDoctors = doctors.filter((doctor) => {
    const matchesRole =
      selectedRole === 'All' || doctor.role.toLowerCase().includes(selectedRole.toLowerCase());
    const matchesSearch = doctor.name.toLowerCase().includes(searchTerm.toLowerCase());
    return matchesRole && matchesSearch;
  });

  const handleCardClick = (doctorId) => {
    navigate(`/chat/${doctorId}`);
  };

  return (
    <section className="bg-slate-50">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">
          <div className="max-w-3xl mx-auto text-center pb-12 md:pb-20">
            <h2 className="h2 font-playfair-display text-slate-800">
              Get expert medical advice from our team of specialists
            </h2>
          </div>

          <div className="flex gap-4 justify-center mb-8">
            <select
              className="border rounded px-4 py-2"
              value={selectedRole}
              onChange={(e) => setSelectedRole(e.target.value)}>
              <option value="All">All Roles</option>
              <option value="CEO">CEO</option>
              <option value="Doctor">Doctor</option>
              <option value="Specialist">Specialist</option>
            </select>
            <input
              type="text"
              placeholder="Search by name"
              className="border rounded px-4 py-2"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
            />
          </div>

          <div
            className="max-w-sm mx-auto sm:max-w-none grid gap-12 sm:grid-cols-2 md:grid-cols-3 sm:gap-x-6 sm:gap-y-8 items-start mb-12 md:mb-16 "
            data-aos-id-testimonials>
            {filteredDoctors.map((doctor) => (
              <article
                key={doctor.id}
                className="h-full flex flex-col bg-white p-6 shadow-xl cursor-pointer"
                data-aos="fade-up"
                data-aos-anchor="[data-aos-id-testimonials]"
                data-aos-delay={doctor.delay}
                onClick={() => handleCardClick(doctor.id)}>
                <header>
                  <div className="flex items-center mb-4">
                    <div className="relative mr-5">
                      <img
                        className="rounded-full shrink-0"
                        // src={doctor.image}
                        src='../assets/images/img.jpg'
                        width={48}
                        height={48}
                        alt={doctor.name}
                      />
                    </div>
                    <p>{doctor.name}</p>
                  </div>
                </header>
                <div className="grow mb-3">
                  <p className="text-slate-500 italic">{doctor.quote}</p>
                </div>
                <footer className="text-sm font-medium">
                  <a
                    className="text-slate-800 hover:text-blue-600 transition duration-150 ease-in-out"
                    href="#0"
                  >
                    {doctor.name}
                  </a>
                  <span className="text-slate-300"> · </span>
                  <span className="text-slate-500">{doctor.role}</span>
                </footer>
              </article>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
