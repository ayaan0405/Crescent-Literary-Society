document.addEventListener("DOMContentLoaded", async () => {
  try {
    const response = await fetch('data/carousel.json');
    if (response.ok) {
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
    }
  } catch (err) {
    console.error("CMS Loader Error (Carousel):", err);
  }

  // Blog Loader
  try {
    const blogContainer = document.getElementById('blog-grid');
    if (blogContainer) {
      try {
        const response = await fetch('data/blog.json?t=' + new Date().getTime());
        if (!response.ok) {
          blogContainer.innerHTML = `<p style="color:red">Fetch failed: ${response.status} ${response.statusText}</p>`;
          return;
        }
        
        const data = await response.json();
        if (data.posts && data.posts.length > 0) {
          blogContainer.innerHTML = ''; // Clear loading text
          
          const sortedPosts = data.posts.sort((a, b) => new Date(b.date) - new Date(a.date));
          
          sortedPosts.forEach(post => {
            const card = document.createElement('div');
            card.className = 'blog-card fade-up visible'; // Add visible immediately so it doesn't get stuck transparent
            card.style.opacity = '1';
            card.style.transform = 'none';
            
            // Format date
            const dateObj = new Date(post.date);
            const dateStr = dateObj.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
            
            // Fix image path
            let imgSrc = post.thumbnail || 'assets/hero/hero-bg.jpg';
            if (imgSrc.startsWith('/')) imgSrc = imgSrc.substring(1);
            
            // Convert markdown to plain text for preview (simple strip)
            const plainText = post.body ? post.body.replace(/[#*_\[\]>]/g, '') : '';
            
            card.innerHTML = `
              <img src="${imgSrc}" alt="${post.title}" class="blog-thumb" loading="lazy">
              <div class="blog-content">
                <span class="blog-date">${dateStr}</span>
                <h3 class="blog-title">${post.title}</h3>
                <p class="blog-body-preview">${plainText.substring(0, 150)}...</p>
                <div class="blog-author">— ${post.author || 'Anonymous'}</div>
              </div>
            `;
            blogContainer.appendChild(card);
          });
        } else {
          blogContainer.innerHTML = '<p style="text-align:center; width:100%;">No posts yet.</p>';
        }
      } catch (innerErr) {
         blogContainer.innerHTML = `<p style="color:red">JS Error: ${innerErr.message}</p>`;
      }
    }
  } catch (err) {
    console.error("CMS Loader Error (Blog):", err);
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
