<template>
  <section id="hero" class="hero fade-in">
    <div class="container hero-content">
      <div class="hero-text">
        <h2 class="gold-gradient">سحر الذهب.. ونقاء الألماس</h2>
        <p class="subtitle">تصاميم خالدة تجسد الفخامة العربية الأصيلة، مصاغة بأعلى درجات الدقة والجمال.</p>
        <div class="cta-group">
          <button class="primary-btn">اكتشف المجموعة</button>
          <button class="secondary-btn">خدمة العملاء</button>
        </div>
      </div>
      <div class="hero-image-container">
        <div class="image-placeholder silk-texture">
          <div class="placeholder-icon">⌚💍</div>
          <div class="image-caption">تصوير احترافي بدقة 8k</div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 120px 0 60px;
}

.hero-content {
  display: flex;
  align-items: center;
  gap: 4rem;
  width: 100%;
}

.hero-text {
  flex: 38;
  text-align: right;
}

.hero-image-container {
  flex: 62;
  height: 500px;
}

.hero-text h2 {
  font-size: clamp(2.5rem, 5vw, 4rem);
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.hero-text .subtitle {
  font-size: clamp(1rem, 2vw, 1.4rem);
  color: var(--text-muted);
  margin-bottom: 2.5rem;
  font-weight: 300;
}

.cta-group {
  display: flex;
  gap: 1.5rem;
}

.primary-btn, .secondary-btn {
  padding: 1rem 2rem;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  border-radius: 2px;
  transition: all 0.3s ease;
  white-space: nowrap;
}

.primary-btn {
  background: var(--emerald-deep);
  color: var(--text-white);
  border: none;
}

.primary-btn:hover {
  background: var(--emerald-light);
  box-shadow: 0 10px 20px rgba(12, 62, 42, 0.15);
}

.secondary-btn {
  background: transparent;
  color: var(--emerald-deep);
  border: 1px solid var(--emerald-deep);
}

.secondary-btn:hover {
  background: rgba(12, 62, 42, 0.05);
}

.image-placeholder {
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.05);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: 1px solid rgba(197, 160, 89, 0.3);
  position: relative;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

.placeholder-icon {
  font-size: 6rem;
  margin-bottom: 1rem;
}

.image-caption {
  font-family: var(--font-calligraphy);
  color: var(--gold-light);
  font-size: 1.1rem;
}

@media (max-width: 1024px) {
  .hero-content {
    flex-direction: column-reverse;
    gap: 3rem;
  }
  
  .hero-text {
    flex: 1;
    text-align: center;
  }
  
  .hero-image-container {
    flex: 1;
    width: 100%;
    height: 400px;
  }
  
  .cta-group {
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .hero {
    padding-top: 100px;
  }
  
  .hero-text h2 {
    font-size: 2.2rem;
  }
  
  .cta-group {
    flex-direction: column;
    width: 100%;
  }
  
  .primary-btn, .secondary-btn {
    width: 100%;
  }
  
  .hero-image-container {
    height: 300px;
  }
}
</style>
