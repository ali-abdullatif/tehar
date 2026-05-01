<script setup>
import { siteConfig } from '@/store/siteStore';
</script>

<template>
  <footer id="contact" class="footer glass-morphism">
    <div class="container footer-content">
      <div class="footer-brand">
        <router-link to="/">
          <img src="@/assets/logo.png" alt="مجوهرات تيهار" class="footer-logo" />
        </router-link>
        <p>{{ siteConfig.hero_subtitle }}</p>
      </div>
      <div class="footer-contact">
        <h4>تواصل معنا</h4>
        <p>{{ siteConfig.footer_address }}</p>
        <p>واتساب: <a :href="`https://wa.me/${siteConfig.footer_phone.replace(/\+/g, '').replace(/\s/g, '')}`" target="_blank" style="color: var(--gold-light); font-weight: 600;">{{ siteConfig.footer_phone }}+</a></p>
        <p>البريد: {{ siteConfig.footer_email }}</p>
      </div>
    </div>
    <div class="copyright">
      <p>&copy; ٢٠٢٦ مجوهرات تيهار. جميع الحقوق محفوظة.</p>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  margin-top: auto;
  padding: 60px 0 20px;
  background: var(--emerald-deep);
  color: var(--text-white);
}

.footer-content {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 4rem;
  margin-bottom: 40px;
}

.footer-logo {
  height: 60px;
  width: auto;
  object-fit: contain;
  margin-bottom: 1.5rem;
  filter: brightness(0) invert(1); /* Make it white for dark background */
}

.footer-brand p {
  color: rgba(255, 255, 255, 0.7);
  max-width: 400px;
}

.footer-links h4, .footer-contact h4 {
  color: var(--gold-light);
  margin-bottom: 1.5rem;
  font-family: var(--font-sans);
}

.footer-links ul {
  list-style: none;
}

.footer-links li {
  margin-bottom: 0.8rem;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.7);
}

.footer-links a:hover {
  color: var(--gold-primary);
}

.footer-contact p {
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 0.8rem;
}

.copyright {
  text-align: center;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 20px;
  color: rgba(255, 255, 255, 0.5);
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .footer-content {
    grid-template-columns: 1fr;
    gap: 2rem;
    text-align: center;
  }
  .footer-brand p {
    margin: 0 auto;
  }
}
</style>
