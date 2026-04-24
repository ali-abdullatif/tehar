<script setup>
import { ref } from 'vue'
import { cartState, cartCount } from '@/store/cartStore'

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}
</script>

<template>
  <nav class="navbar glass-morphism" :class="{ 'menu-open': isMenuOpen }">
    <div class="container nav-content">
      <div class="logo">
        <img src="@/assets/logo.png" alt="مجوهرات الملوك" class="nav-logo" />
      </div>
      
      <!-- Desktop Links -->
      <ul class="nav-links desktop-only">
        <li><a href="#hero">الرئيسية</a></li>
        <li><a href="#collection">المجموعات</a></li>
        <li><a href="#about">عن دارنا</a></li>
        <li><a href="#contact">اتصل بنا</a></li>
      </ul>

      <!-- Cart & Mobile Toggle -->
      <div class="nav-extra">
        <button class="cart-toggle" @click="cartState.toggleCart" aria-label="Cart">
          <svg xmlns="http://www.w3.org/2000/svg" class="nav-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
          </svg>
          <span v-if="cartCount() > 0" class="cart-badge">{{ cartCount() }}</span>
        </button>

        <button class="menu-toggle mobile-only" @click="toggleMenu" aria-label="Toggle Menu">
          <span class="bar" :class="{ 'active': isMenuOpen }"></span>
          <span class="bar" :class="{ 'active': isMenuOpen }"></span>
          <span class="bar" :class="{ 'active': isMenuOpen }"></span>
        </button>
      </div>
    </div>

    <!-- Mobile Menu Overlay -->
    <div class="mobile-menu" :class="{ 'active': isMenuOpen }">
      <ul class="mobile-nav-links">
        <li><a href="#hero" @click="toggleMenu">الرئيسية</a></li>
        <li><a href="#collection" @click="toggleMenu">المجموعات</a></li>
        <li><a href="#about" @click="toggleMenu">عن دارنا</a></li>
        <li><a href="#contact" @click="toggleMenu">اتصل بنا</a></li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
  padding: 1rem 0;
  transition: all 0.4s ease;
}

.nav-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-extra {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.nav-logo {
  height: 45px;
  width: auto;
  object-fit: contain;
  /* Natural emerald color for the light navbar */
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 2rem;
}

.nav-links a {
  font-weight: 400;
  font-size: 1.1rem;
  color: var(--text-main);
}

.nav-links a:hover {
  color: var(--emerald-light);
}

.gold-btn {
  background: var(--emerald-deep);
  color: var(--text-white);
  border: none;
  padding: 0.6rem 1.5rem;
  font-family: var(--font-sans);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  border-radius: 2px;
}

.gold-btn.w-full {
  width: 100%;
}

.gold-btn:hover {
  background: var(--emerald-light);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(12, 62, 42, 0.2);
}

.cart-toggle {
  position: relative;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  display: flex;
  align-items: center;
  transition: transform 0.3s ease;
}

.nav-icon {
  width: 28px;
  height: 28px;
  color: var(--gold-primary);
}

.cart-badge {
  position: absolute;
  top: 0;
  left: 0;
  background: #ff4757;
  color: white;
  font-size: 0.75rem;
  font-weight: 700;
  min-width: 18px;
  height: 18px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2px;
  border: 2px solid white;
}

/* Mobile Toggle Styles */
.menu-toggle {
  display: none;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 10px;
  flex-direction: column;
  gap: 6px;
}

.bar {
  display: block;
  width: 25px;
  height: 2px;
  background-color: var(--emerald-deep);
  transition: all 0.3s ease;
}

.bar.active:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}
.bar.active:nth-child(2) {
  opacity: 0;
}
.bar.active:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

/* Mobile Menu Styles */
.mobile-menu {
  position: fixed;
  top: 0;
  right: -100%;
  width: 80%;
  height: 100vh;
  background: var(--bg-primary);
  padding: 100px 2rem;
  transition: all 0.5s cubic-bezier(0.77,0.2,0.05,1.0);
  box-shadow: -10px 0 30px rgba(12, 62, 42, 0.1);
  border-left: 1px solid rgba(12, 62, 42, 0.05);
}

.mobile-menu.active {
  right: 0;
}

.mobile-nav-links {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  text-align: center;
}

.mobile-nav-links a {
  font-size: 1.5rem;
  font-family: var(--font-calligraphy);
  color: var(--emerald-deep);
}

.desktop-only {
  display: flex;
}

.mobile-only {
  display: none;
}

@media (max-width: 768px) {
  .desktop-only {
    display: none;
  }
  .mobile-only {
    display: flex;
  }
  .logo h1 {
    font-size: 1.5rem;
  }
}

.mt-2 {
  margin-top: 2rem;
}
</style>
