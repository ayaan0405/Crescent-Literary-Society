document.addEventListener("DOMContentLoaded", async () => {
  try {
    let carouselFile = 'data/carousel.json';
    const path = window.location.pathname;
    if (path.includes('house-of-debators')) carouselFile = 'data/debators-carousel.json';
    else if (path.includes('improv')) carouselFile = 'data/improv-carousel.json';
    else if (path.includes('writers-guild')) carouselFile = 'data/writers-carousel.json';
    else if (path.includes('quizzers-circuit')) carouselFile = 'data/quizzers-carousel.json';
    else if (path.includes('editorial-board')) carouselFile = 'data/editorial-carousel.json';

    const response = await fetch(carouselFile + '?t=' + new Date().getTime());
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

  // --- 2. Load Members ---
  try {
    const membersContainer = document.getElementById('members-grid');
    if (membersContainer) {
      try {
        const response = await fetch('data/members.json?t=' + new Date().getTime());
        if (!response.ok) throw new Error("Fetch failed: " + response.status);
        const data = await response.json();
        
        if (data.members && data.members.length > 0) {
          membersContainer.innerHTML = ''; // clear
          data.members.forEach((member, i) => {
            const delayClass = i % 3 === 1 ? 'delay-1' : (i % 3 === 2 ? 'delay-2' : '');
            let imgSrc = member.image || 'assets/members/member-placeholder.jpg';
            if (imgSrc.startsWith('/')) imgSrc = imgSrc.substring(1);
            
            membersContainer.innerHTML += `
              <div class="member-card fade-up visible ${delayClass}" style="opacity: 1; transform: none;">
                <img src="${imgSrc}" alt="${member.name}" loading="lazy">
                <h4>${member.name}</h4>
                <span class="member-role">${member.role}</span>
              </div>
            `;
          });
        } else {
          membersContainer.innerHTML = '<p>No members found.</p>';
        }
      } catch (innerErr) {
        membersContainer.innerHTML = `<p style="color:red">JS Error: ${innerErr.message}</p>`;
      }
    }
  } catch (err) {}

  // --- 3. Load Miraki ---
  try {
    const mirakiContainer = document.getElementById('miraki-grid');
    if (mirakiContainer) {
      try {
        const response = await fetch('data/miraki.json?t=' + new Date().getTime());
        if (!response.ok) throw new Error("Fetch failed: " + response.status);
        const data = await response.json();
        
        if (data.posts && data.posts.length > 0) {
          const sortedPosts = data.posts.sort((a, b) => new Date(b.date) - new Date(a.date));
          
          if (mirakiContainer) {
            mirakiContainer.innerHTML = '';
            sortedPosts.forEach(post => {
              const dateObj = new Date(post.date);
              const dateStr = dateObj.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
              let imgSrc = post.thumbnail || 'assets/hero/hero-bg.jpg';
              if (imgSrc.startsWith('/')) imgSrc = imgSrc.substring(1);
              const plainText = post.body ? post.body.replace(/[#*_\[\]>]/g, '') : '';
              
              mirakiContainer.innerHTML += `
                <div class="blog-card fade-up visible" style="opacity: 1; transform: none;">
                  <img src="${imgSrc}" alt="${post.title}" class="blog-thumb" loading="lazy">
                  <div class="blog-content">
                    <span class="blog-date">${dateStr}</span>
                    <h3 class="blog-title">${post.title}</h3>
                    <p class="blog-body-preview">${plainText.substring(0, 150)}...</p>
                    <div class="blog-author">— ${post.author || 'Editorial Board'}</div>
                  </div>
                </div>
              `;
            });
          }
          
          // Auto-update the preview in Writers Guild page
          const previewContainer = document.getElementById('latest-magazine-preview');
          if (previewContainer) {
            const latest = sortedPosts[0];
            let imgSrc = latest.thumbnail || 'assets/magazine/obverse-cover.jpg';
            if (imgSrc.startsWith('/')) imgSrc = imgSrc.substring(1);
            const plainText = latest.body ? latest.body.replace(/[#*_\[\]>]/g, '') : '';
            
            previewContainer.innerHTML = `
              <div style="flex-shrink:0; width:90px;">
                <img src="${imgSrc}" alt="${latest.title}" style="width:90px; border-radius:4px; box-shadow: 0 8px 30px rgba(0,0,0,0.5);" loading="lazy">
              </div>
              <div>
                <span class="eyebrow" style="margin-bottom:0.4rem;">Latest Magazine Issue</span>
                <h3 style="font-size:1.4rem; margin-bottom:0.5rem;">${latest.title}</h3>
                <p style="font-size:0.95rem;">${plainText.substring(0, 200)}...</p>
                <p style="font-size:0.85rem; margin-top:0.75rem; color:rgba(153,153,153,0.7);">
                  Published: ${new Date(latest.date).toLocaleDateString()} &middot; By: ${latest.author || 'Editorial Board'}
                </p>
              </div>
            `;
          }
        } else {
          if (mirakiContainer) {
            mirakiContainer.innerHTML = '<p style="text-align:center; width:100%;">No issues yet.</p>';
          }
        }
      } catch (innerErr) {}
    }
  } catch (err) {}

  // --- 4. Load Crescent Line ---
  try {
    const clContainer = document.getElementById('crescent-line-grid');
    if (clContainer) {
      try {
        const response = await fetch('data/crescent-line.json?t=' + new Date().getTime());
        if (!response.ok) throw new Error("Fetch failed: " + response.status);
        const data = await response.json();
        
        if (data.posts && data.posts.length > 0) {
          clContainer.innerHTML = '';
          const sortedPosts = data.posts.sort((a, b) => new Date(b.date) - new Date(a.date));
          sortedPosts.forEach(post => {
            const dateObj = new Date(post.date);
            const dateStr = dateObj.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
            let imgSrc = post.thumbnail || 'assets/hero/hero-bg.jpg';
            if (imgSrc.startsWith('/')) imgSrc = imgSrc.substring(1);
            const plainText = post.body ? post.body.replace(/[#*_\[\]>]/g, '') : '';
            
            clContainer.innerHTML += `
              <div class="blog-card fade-up visible" style="opacity: 1; transform: none;">
                <img src="${imgSrc}" alt="${post.title}" class="blog-thumb" loading="lazy">
                <div class="blog-content">
                  <span class="blog-date">${dateStr}</span>
                  <h3 class="blog-title">${post.title}</h3>
                  <p class="blog-body-preview">${plainText.substring(0, 150)}...</p>
                  <div class="blog-author">— ${post.author || 'Dean'}</div>
                </div>
              </div>
            `;
          });
        } else {
          clContainer.innerHTML = '<p style="text-align:center; width:100%;">No newsletters yet.</p>';
        }
      } catch (innerErr) {}
    }
  } catch (err) {}

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
