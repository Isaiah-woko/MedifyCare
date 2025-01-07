
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const filterSelect = document.getElementById('filter-select');
    const doctorCards = document.querySelectorAll('.doctor-card');
  
    function filterDoctors() {
        const searchTerm = searchInput.value.toLowerCase();
        const selectedSpecialty = filterSelect.value.toLowerCase();
  
        doctorCards.forEach(card => {
            const doctorName = card.querySelector('h3').textContent.toLowerCase();
            const doctorSpecialty = card.getAttribute('data-specialty').toLowerCase();
  
            const matchesSearch = doctorName.includes(searchTerm);
            const matchesSpecialty = selectedSpecialty === '' || doctorSpecialty === selectedSpecialty;
  
            if (matchesSearch && matchesSpecialty) {
                card.classList.remove('hidden');
            } else {
                card.classList.add('hidden');
            }
        });
    }
  
    searchInput.addEventListener('input', filterDoctors);
    filterSelect.addEventListener('change', filterDoctors);
  
    // Handle modal for video call request
    const videoCallModal = document.getElementById('videoCallModal');
    const videoCallClose = videoCallModal.querySelector('.close');
  
    document.querySelectorAll('.videoCallRequestBtn').forEach(button => {
        button.addEventListener('click', function() {
            const doctorId = this.getAttribute('data-doctor-id');
            document.getElementById('doctorId').value = doctorId;
            videoCallModal.style.display = 'block';
        });
    });
  
    videoCallClose.addEventListener('click', function() {
        videoCallModal.style.display = 'none';
    });
  
    window.onclick = function(event) {
        if (event.target === videoCallModal) {
            videoCallModal.style.display = 'none';
        }
    }
  
    // Handle modal for coming soon
    const comingSoonModal = document.getElementById('comingSoonModal');
    const comingSoonClose = comingSoonModal.querySelector('.close');
  
    document.querySelectorAll('#schedule-btn').forEach(button => {
  button.addEventListener('click', function(event) {
    event.preventDefault();
    comingSoonModal.style.display = 'block';
  });
  });
  
    
  
    comingSoonClose.addEventListener('click', function() {
        comingSoonModal.style.display = 'none';
    });
  
    window.onclick = function(event) {
        if (event.target === comingSoonModal) {
            comingSoonModal.style.display = 'none';
        }
    }
  });
  