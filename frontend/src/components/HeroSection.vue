<template>
  <section 
    id="hero" 
    class="hero fade-in" 
    :style="siteConfig.hero_image ? { backgroundImage: `url(${siteConfig.hero_image})` } : {}"
    :class="{ 'has-bg': siteConfig.hero_image }"
  >
    <div class="hero-overlay" v-if="siteConfig.hero_image"></div>
    <div class="container hero-content">
      <div class="hero-text">
        <h2 class="hero-title">{{ siteConfig.hero_title }}</h2>
        <p class="subtitle">{{ siteConfig.hero_subtitle }}</p>
        <div class="cta-group">
          <button class="primary-btn" @click="scrollToCollection">اكتشف المجموعة</button>
          <button class="secondary-btn" @click="contactUs">تواصل معنا</button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { siteConfig } from '@/store/siteStore';

const scrollToCollection = () => {
  document.getElementById('collection')?.scrollIntoView({ behavior: 'smooth' });
};

const contactUs = () => {
  window.open(`https://wa.me/${siteConfig.footer_phone}`, '_blank');
};
</script>

<style scoped>
.hero {
  position: relative;
  width: 100%;
  aspect-ratio: 1698 / 624;
  min-height: 480px; /* minimum height to ensure content fits on smaller screens */
  display: flex;
  align-items: center;
  padding: 2rem 0;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-color: var(--bg-soft);
  overflow: hidden;
}

.hero.has-bg {
  /* Ensuring background behaves for premium feel */
  background-attachment: fixed; 
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    to left,
    rgba(255, 255, 255, 0.3) 0%,
    rgba(255, 255, 255, 0) 100%
  );
  z-index: 1;
}

.hero-content {
  position: relative;
  z-index: 2;
  width: 100%;
}

.hero-text {
  max-width: 600px;
  text-align: right;
}

.hero-text .hero-title {
  font-size: clamp(3rem, 6vw, 4.5rem);
  margin-bottom: 1.5rem;
  line-height: 1.1;
  font-weight: 700;
  color: var(--emerald-deep);
}

.hero-text .subtitle {
  font-size: clamp(1.1rem, 2vw, 1.6rem);
  color: var(--emerald-deep);
  margin-bottom: 3rem;
  font-weight: 400;
  line-height: 1.6;
}

.cta-group {
  display: flex;
  gap: 1.5rem;
}

.primary-btn, .secondary-btn {
  padding: 1.2rem 2.8rem;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  white-space: nowrap;
}

.primary-btn {
  background: var(--emerald-deep);
  color: var(--text-white);
  border: none;
  box-shadow: 0 10px 30px rgba(12, 62, 42, 0.2);
}

.primary-btn:hover {
  background: var(--emerald-light);
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(12, 62, 42, 0.3);
}

.secondary-btn {
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  color: var(--emerald-deep);
  border: 1px solid var(--emerald-deep);
}

.secondary-btn:hover {
  background: var(--emerald-deep);
  color: white;
  transform: translateY(-5px);
}

@media (max-width: 768px) {
  .hero {
    aspect-ratio: auto;
    min-height: 100vh;
    padding: 100px 1rem 60px;
    background-position: center center;
  }

  .hero-overlay {
    background: linear-gradient(
      to bottom,
      rgba(255, 255, 255, 0.95) 0%,
      rgba(255, 255, 255, 0.7) 100%
    );
  }
  
  .hero-text {
    max-width: 100%;
    text-align: center;
  }
  
  .hero-text h2 {
    font-size: 2.5rem;
  }
  
  .cta-group {
    justify-content: center;
    flex-direction: column;
    gap: 1rem;
  }

  .primary-btn, .secondary-btn {
    width: 100%;
  }
}
</style>
