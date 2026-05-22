document.addEventListener("DOMContentLoaded", () => {
  const slides = document.querySelectorAll(".hero-carousel .main-hero-bg");
  if (slides.length <= 1) return;

  let currentSlide = 0;
  const slideInterval = 5000; // Change slide every 5 seconds

  window.heroCarouselInterval = setInterval(() => {
    // Remove active class from current slide
    slides[currentSlide].classList.remove("active");
    
    // Move to next slide
    currentSlide = (currentSlide + 1) % slides.length;
    
    // Add active class to new slide
    slides[currentSlide].classList.add("active");
  }, slideInterval);
});
