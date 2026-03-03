// Simple gallery slider
let currentSlide = 0;
const slides = document.querySelectorAll('.gallery-slide');
const nextBtn = document.querySelector('.gallery-next');
const prevBtn = document.querySelector('.gallery-prev');

function showSlide(idx) {
  slides.forEach((slide, i) => {
    slide.style.display = i === idx ? 'block' : 'none';
  });
}
if (slides.length) {
  showSlide(currentSlide);
  nextBtn.addEventListener('click', () => {
    currentSlide = (currentSlide + 1) % slides.length;
    showSlide(currentSlide);
  });
  prevBtn.addEventListener('click', () => {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    showSlide(currentSlide);
  });
}
// Simple fade-in on scroll
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('fade-in');
    }
  });
}, { threshold: 0.2 });
document.querySelectorAll('section').forEach(sec => observer.observe(sec)); 