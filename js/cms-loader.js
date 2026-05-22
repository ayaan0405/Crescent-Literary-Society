document.addEventListener("DOMContentLoaded", async () => {
  try {
    const response = await fetch('data/carousel.json');
    if (!response.ok) return; // Silent fail, fallback to hardcoded if needed
    const data = await response.json();
    
    const carouselContainer = document.getElementById('hero-carousel');
    if (carouselContainer && data.slides && data.slides.length > 0) {
      // Clear existing hardcoded slides
      carouselContainer.innerHTML = '';
      
      // Inject CMS slides
      data.slides.forEach((slide, index) => {
        const div = document.createElement('div');
        div.className = index === 0 ? 'main-hero-bg active' : 'main-hero-bg';
        // Handle path resolution: Decap CMS might save absolute paths like /assets/uploads/...
        // or relative like assets/uploads/... 
        let imgSrc = slide.image;
        if (imgSrc.startsWith('/')) {
            imgSrc = imgSrc.substring(1);
        }
        
        div.style.backgroundImage = `url('${imgSrc}')`;
        div.setAttribute('role', 'img');
        div.setAttribute('aria-label', slide.altText || `Slide ${index + 1}`);
        carouselContainer.appendChild(div);
      });
      
      // Re-init carousel logic since DOM changed
      initCarousel();
    }
  } catch (err) {
    console.error("CMS Loader Error:", err);
  }
});

function initCarousel() {
  const slides = document.querySelectorAll(".hero-carousel .main-hero-bg");
  if (slides.length <= 1) return;

  // Clear existing interval if any (from carousel.js)
  if (window.heroCarouselInterval) clearInterval(window.heroCarouselInterval);

  let currentSlide = 0;
  const slideInterval = 5000;

  window.heroCarouselInterval = setInterval(() => {
    slides[currentSlide].classList.remove("active");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("active");
  }, slideInterval);
}
