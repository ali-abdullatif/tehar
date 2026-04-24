<script setup>
import Navbar from './components/Navbar.vue'
import HeroSection from './components/HeroSection.vue'
import CollectionSection from './components/CollectionSection.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="app-container">
    <Navbar />
    <main>
      <HeroSection />
      <CollectionSection />
    </main>
    <Footer />
  </div>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

main {
  flex: 1;
}
</style>
