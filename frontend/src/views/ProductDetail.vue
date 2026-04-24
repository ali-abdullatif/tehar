<template>
  <div class="product-detail section-padding">
    <div class="container">
      
      <button @click="$router.push('/')" class="back-link">
        <span>←</span> العودة للمجموعة
      </button>

      <div v-if="loading" class="loader-wrap">
        <div class="spinner"></div>
      </div>

      <div v-else-if="product" class="product-grid">
        <!-- Gallery Section -->
        <div class="gallery-column">
          <div class="main-image-wrap glass-morphism">
            <img :src="activeImage" :alt="product.name" class="main-image" />
          </div>
          
          <div v-if="allImages.length > 1" class="thumbnails-row">
            <div 
              v-for="(img, idx) in allImages" 
              :key="idx"
              class="thumb-item"
              :class="{ active: activeImage === img }"
              @click="activeImage = img"
            >
              <img :src="img" alt="Thumbnail" />
            </div>
          </div>
        </div>

        <!-- Info Section -->
        <div class="info-column">
          <div class="product-header">
            <span v-if="product.category" class="cat-badge">{{ product.category.name }}</span>
            <h1 class="gold-gradient">{{ product.name }}</h1>
            <p class="price-tag">{{ product.price.toLocaleString('ar-SA') }} ر.س</p>
          </div>

          <div class="description-box">
            <h4>عن هذه القطعة</h4>
            <p>{{ product.description || 'لا يوجد وصف متاح لهذه القطعة الملكية.' }}</p>
          </div>

          <div class="action-box">
            <div class="qty-selector">
              <label>الكمية</label>
              <div class="qty-btn-group">
                <button @click="quantity > 1 ? quantity-- : null">-</button>
                <span>{{ quantity }}</span>
                <button @click="quantity++">+</button>
              </div>
            </div>

            <button @click="addToCart" class="add-to-cart-btn">
              <span>إضافة للحقيبة</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
              </svg>
            </button>
          </div>

          <div class="assurance-list">
            <div class="assurance-item">
              <svg xmlns="http://www.w3.org/2000/svg" class="icon-gold" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-7.714 2.143L11 21l-2.286-6.857L1 12l7.714-2.143L11 3z" />
              </svg>
              <p>ذهب عيار ١٨ قيراط نقي</p>
            </div>
            <div class="assurance-item">
              <svg xmlns="http://www.w3.org/2000/svg" class="icon-gold" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
              </svg>
              <p>أحجار كريمة منتقاة بعناية</p>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="error-msg">
        <p>عذراً، لم نتمكن من العثور على هذه القطعة.</p>
        <button @click="$router.push('/')">العودة للرئيسية</button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import axios from 'axios';
import { cartState } from '@/store/cartStore';

const API_URL = 'http://localhost:8000';
const route = useRoute();
const product = ref(null);
const loading = ref(true);
const activeImage = ref('');
const quantity = ref(1);

const fetchProduct = async () => {
  try {
    const res = await axios.get(`${API_URL}/items/${route.params.id}`);
    product.value = res.data;
    // Set first image as active
    activeImage.value = product.value.image_url || (product.value.images[0]?.url) || '';
  } catch (e) {
    console.error('Error fetching product:', e);
  } finally {
    loading.value = false;
  }
};

const allImages = computed(() => {
  if (!product.value) return [];
  const gallery = product.value.images.map(img => img.url);
  const primary = product.value.image_url;
  
  // Return unique set of images (sometimes primary is also in gallery)
  return [...new Set([primary, ...gallery])].filter(i => i);
});

const addToCart = () => {
  for (let i = 0; i < quantity.value; i++) {
    cartState.addItem(product.value);
  }
};

onMounted(fetchProduct);
</script>

<style scoped>
.product-detail {
  min-height: 80vh;
  padding-top: 140px;
  background: var(--bg-deep);
}

.back-link {
  background: none;
  border: none;
  color: var(--gold-primary);
  cursor: pointer;
  font-size: 1rem;
  margin-bottom: 2rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: opacity 0.3s;
}
.back-link:hover { opacity: 0.7; }

.product-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: start;
}

/* Gallery */
.main-image-wrap {
  width: 100%;
  aspect-ratio: 1/1;
  background: white;
  border-radius: 20px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(212, 175, 55, 0.2);
  margin-bottom: 1.5rem;
}
.main-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.thumbnails-row {
  display: flex;
  gap: 1rem;
  overflow-x: auto;
  padding-bottom: 0.5rem;
}

.thumb-item {
  width: 80px;
  height: 80px;
  border-radius: 10px;
  border: 2px solid transparent;
  cursor: pointer;
  overflow: hidden;
  background: white;
  flex-shrink: 0;
  transition: all 0.2s;
}
.thumb-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.thumb-item.active {
  border-color: var(--gold-primary);
  transform: scale(0.95);
}

/* Info */
.info-column {
  color: white;
}

.cat-badge {
  display: inline-block;
  background: rgba(212, 175, 55, 0.1);
  color: var(--gold-light);
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

h1 {
  font-family: var(--font-calligraphy);
  font-size: 3.5rem;
  margin-bottom: 1rem;
}

.price-tag {
  font-size: 2rem;
  color: var(--gold-primary);
  font-weight: 700;
  margin-bottom: 3rem;
}

.description-box {
  margin-bottom: 3rem;
  line-height: 1.8;
}
.description-box h4 {
  color: var(--gold-light);
  margin-bottom: 1rem;
  font-size: 1.2rem;
}
.description-box p {
  color: rgba(255,255,255,0.7);
}

.action-box {
  background: rgba(255,255,255,0.03);
  padding: 2rem;
  border-radius: 16px;
  border: 1px solid rgba(212, 175, 55, 0.1);
  margin-bottom: 3rem;
}

.qty-selector {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 2rem;
}
.qty-btn-group {
  display: flex;
  align-items: center;
  background: rgba(255,255,255,0.05);
  border-radius: 30px;
  padding: 0.5rem 1.5rem;
  gap: 1.5rem;
}
.qty-btn-group button {
  background: none;
  border: none;
  color: white;
  font-size: 1.5rem;
  cursor: pointer;
}

.add-to-cart-btn {
  width: 100%;
  background: linear-gradient(135deg, #0c3e2a 0%, #1a6645 100%);
  color: white;
  border: 1px solid var(--gold-primary);
  padding: 1.2rem;
  border-radius: 12px;
  font-size: 1.2rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.add-to-cart-btn:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(12, 62, 42, 0.5);
}

.assurance-list {
  display: flex;
  gap: 2rem;
}
.assurance-item {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  color: rgba(255,255,255,0.5);
  font-size: 0.9rem;
}
.assurance-item .icon { font-size: 1.2rem; }

.loader-wrap {
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(212, 175, 55, 0.2);
  border-top-color: var(--gold-primary);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

@media (max-width: 992px) {
  .product-grid { grid-template-columns: 1fr; gap: 3rem; }
  h1 { font-size: 2.5rem; }
}
</style>
