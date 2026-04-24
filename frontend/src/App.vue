<script setup>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
import CartDrawer from './components/CartDrawer.vue'
import { onMounted } from 'vue'
import { siteConfig } from '@/store/siteStore'

onMounted(() => {
  siteConfig.fetch()
})
</script>

<template>
  <div class="app-container">
    <Navbar />
    <main>
      <router-view></router-view>
    </main>
    <Footer />
    <CartDrawer />
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
