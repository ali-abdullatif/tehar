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
            <div class="badges-row">
              <span v-if="product.category" class="cat-badge">{{ product.category.name }}</span>
              <span v-if="product.product_code" class="code-badge">رمز القطعة: {{ product.product_code }}</span>
            </div>
            <h1>{{ product.name }}</h1>
            <p class="price-tag">{{ product.price.toLocaleString('en-US') }} ر.ي</p>
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

            <button @click="inquireWhatsApp" class="whatsapp-btn">
              <span>استفسار عبر الواتساب</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.417-.003 6.557-5.338 11.892-11.893 11.892-1.997-.001-3.951-.5-5.688-1.448l-6.305 1.652zm6.599-3.835c1.544.917 3.41 1.401 5.316 1.402h.005c5.385 0 9.767-4.382 9.77-9.77.002-2.611-1.015-5.065-2.863-6.915-1.847-1.85-4.305-2.868-6.917-2.869-5.386 0-9.768 4.382-9.77 9.77-.001 2.1.548 4.146 1.591 5.922l-1.013 3.702 3.791-.993zm11.368-7.73c-.301-.151-1.78-.878-2.056-.979-.276-.1-.477-.151-.677.151-.2.3-.775 1.003-.951 1.254-.176.251-.352.281-.653.131-2.014-.941-2.584-1.439-3.551-3.135-.251-.439.251-.408.72-.84.238-.218.3-.399.3-.599s-.1-.376-.2-.476c-.099-.1-.477-1.155-.653-1.581-.171-.413-.344-.356-.477-.363-.121-.006-.259-.007-.399-.007-.14 0-.369.053-.562.261-.193.208-.737.72-.737 1.758s.757 2.056.862 2.197c.105.14 1.488 2.274 3.606 3.187.502.217.896.347 1.2.443.504.16 1.159.137 1.597.072.489-.072 1.481-.603 1.691-1.185.209-.583.209-1.084.146-1.185-.064-.101-.237-.151-.539-.302z"/>
              </svg>
            </button>
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
import { siteConfig } from '@/store/siteStore';
import { trackEvent } from '@/store/tracking';

const API_URL = 'http://tihar.site:8000';
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
    
    // Tracking VIEW event
    trackEvent('view', product.value.id);
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

const inquireWhatsApp = () => {
  const phone = siteConfig.footer_phone.replace(/\+/g, '').replace(/\s/g, ''); 
  const shopName = siteConfig.hero_title || 'مجوهرات تيهار';
  
  let message = `مرحبًا ${shopName} 👋\n`;
  message += `عندي استفسار بخصوص المنتج: ${product.value.name}\n`;
  if (product.value.product_code) message += `🔢 الكود: ${product.value.product_code}\n`;
  message += `💰 السعر: ${product.value.price.toLocaleString('en-US')} ر.ي\n`;
  message += `📎 رابط المنتج: ${window.location.href}\n`;
  
  const encoded = encodeURIComponent(message);
  window.open(`https://wa.me/${phone}?text=${encoded}`, '_blank');
};

onMounted(() => {
  window.scrollTo(0, 0);
  fetchProduct();
});
</script>

<style scoped>
.product-detail {
  min-height: 80vh;
  padding-top: 140px;
  background: var(--bg-soft);
}

.back-link {
  background: none;
  border: none;
  color: var(--emerald-deep);
  cursor: pointer;
  font-size: 1.1rem;
  font-weight: 600;
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
.gallery-column, .info-column {
  min-width: 0;
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
  border: 1px solid rgba(12, 62, 42, 0.08);
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
  border-color: var(--emerald-deep);
  transform: scale(0.95);
}

/* Info */
.info-column {
  color: var(--text-main);
}

.cat-badge {
  display: inline-block;
  background: rgba(12, 62, 42, 0.06);
  color: var(--emerald-deep);
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  font-size: 0.9rem;
  font-weight: 600;
}

.code-badge {
  display: inline-block;
  background: rgba(0, 0, 0, 0.04);
  color: var(--text-muted);
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  font-size: 0.9rem;
}

.badges-row {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

h1 {
  font-family: var(--font-calligraphy);
  font-size: 3.5rem;
  margin-bottom: 1rem;
  color: var(--emerald-deep);
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
  color: var(--emerald-deep);
  margin-bottom: 1rem;
  font-size: 1.2rem;
}
.description-box p {
  color: var(--text-muted);
}

.action-box {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  border: 1px solid rgba(12, 62, 42, 0.08);
  box-shadow: 0 4px 20px rgba(0,0,0,0.02);
  margin-bottom: 3rem;
}

.qty-selector {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 2rem;
}
.qty-selector label {
  font-weight: 600;
  color: var(--emerald-deep);
}
.qty-btn-group {
  display: flex;
  align-items: center;
  background: var(--bg-soft);
  border-radius: 30px;
  padding: 0.5rem 1.5rem;
  gap: 1.5rem;
}
.qty-btn-group button {
  background: none;
  border: none;
  color: var(--emerald-deep);
  font-size: 1.5rem;
  cursor: pointer;
  font-weight: 600;
}

.add-to-cart-btn {
  width: 100%;
  background: var(--emerald-deep);
  color: white;
  border: none;
  padding: 1.2rem;
  border-radius: 12px;
  font-size: 1.2rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  transition: all 0.3s ease;
}
.add-to-cart-btn:hover {
  background: var(--emerald-light);
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(12, 62, 42, 0.15);
}

.whatsapp-btn {
  width: 100%;
  background: #25D366;
  color: white;
  border: none;
  padding: 1.2rem;
  border-radius: 12px;
  font-size: 1.2rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  transition: all 0.3s ease;
  margin-top: 1rem;
}
.whatsapp-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(37, 211, 102, 0.2);
}

.loader-wrap {
  height: 400px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.spinner {
  width: 40px;
  height: 40px;
  border: 3px solid rgba(12, 62, 42, 0.1);
  border-top-color: var(--emerald-deep);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

@media (max-width: 992px) {
  .product-grid { grid-template-columns: 1fr; gap: 3rem; }
  h1 { font-size: 2.5rem; }
}

@media (max-width: 480px) {
  .product-detail { padding-top: 100px; }
  .main-image-wrap { aspect-ratio: 4/5; border-radius: 12px; }
  h1 { font-size: 2rem; line-height: 1.3; }
  .qty-selector { flex-wrap: wrap; gap: 1rem; }
  .price-tag { font-size: 1.5rem; }
}
</style>
