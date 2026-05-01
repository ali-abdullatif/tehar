<template>
  <section id="collection" class="collection section-padding">
    <div class="container">
      <div class="section-header">
        <h3 class="gold-gradient">روائعنا المختارة</h3>
        <p>نخبة من أجود المصاغ المرصع بأنقى الأحجار الكريمة</p>
      </div>
      
      <div v-if="loading" style="text-align: center; color: white;">جاري التحميل...</div>
      <div v-else-if="items.length === 0" style="text-align: center; color: white;">لا توجد قطع حالياً.</div>

      <div v-else class="collection-groups">
        <div v-for="(group, catName) in groupedItems" :key="catName" class="category-section">
          <h4 class="category-title">✦ {{ catName }}</h4>
          <div class="grid-layout">
            <div v-for="item in group" :key="item.id" class="jewelry-card glass-morphism" @click="$router.push(`/product/${item.id}`)">
              <div class="card-image-placeholder">
                <img v-if="item.image_url" :src="item.image_url" class="card-img" />
                <svg v-else xmlns="http://www.w3.org/2000/svg" class="placeholder-icon" width="48" height="48" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                </svg>
              </div>
              <div class="card-content">
                <h5>{{ item.name }}</h5>
                <p class="price">{{ item.price.toLocaleString('en-US') }} ر.ي</p>
                <div class="card-actions">
                  <button @click.stop="cartState.addItem(item)" class="add-cart-btn">
                    إضافة للحقيبة 🛒
                  </button>
                  <button class="view-btn">التفاصيل</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import { cartState } from '@/store/cartStore';

const API_URL = '/api';
const items = ref([]);
const loading = ref(true);

const fetchItems = async () => {
  try {
    const response = await axios.get(`${API_URL}/items`);
    items.value = response.data;
  } catch (error) {
    console.error('Error fetching items:', error);
  } finally {
    loading.value = false;
  }
};

const groupedItems = computed(() => {
  const groups = {};
  items.value.forEach(item => {
    const catName = item.category ? item.category.name : 'أقسام متنوعة';
    if (!groups[catName]) groups[catName] = [];
    groups[catName].push(item);
  });
  return groups;
});

onMounted(fetchItems);
</script>

<style scoped>
.section-padding {
  padding: 100px 0;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
  padding: 0 1rem;
}

.section-header h3 {
  font-size: clamp(2rem, 4vw, 3rem);
  margin-bottom: 1rem;
}

.section-header p {
  font-size: clamp(1rem, 1.5vw, 1.2rem);
  color: var(--text-muted);
}

.collection-groups {
  display: flex;
  flex-direction: column;
  gap: 5rem;
}

.category-section {
  position: relative;
}

.category-title {
  font-family: var(--font-calligraphy);
  font-size: 2.2rem;
  color: var(--emerald-deep);
  margin-bottom: 2.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(12, 62, 42, 0.08);
}

.grid-layout {
  display: flex;
  overflow-x: auto;
  gap: 2.5rem;
  padding-bottom: 2rem; /* Space for the scrollbar */
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.grid-layout::-webkit-scrollbar {
  height: 8px;
}
.grid-layout::-webkit-scrollbar-track {
  background: rgba(12, 62, 42, 0.05);
  border-radius: 4px;
}
.grid-layout::-webkit-scrollbar-thumb {
  background: var(--emerald-deep);
  border-radius: 4px;
}

.jewelry-card {
  flex: 0 0 auto;
  width: 300px;
  scroll-snap-align: start;
  padding: 1.5rem;
  background: var(--bg-soft);
  transition: all 0.4s ease;
  cursor: pointer;
  border: 1px solid rgba(12, 62, 42, 0.05);
}

.jewelry-card:hover {
  transform: translateY(-5px);
  border-color: var(--emerald-deep);
  box-shadow: 0 15px 30px rgba(12, 62, 42, 0.08);
}

.card-image-placeholder {
  height: 250px;
  background: rgba(12, 62, 42, 0.03);
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1.5rem;
}

.card-image-placeholder .icon {
  font-size: 3rem;
}

.card-content h4 {
  font-family: var(--font-sans);
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  color: var(--text-main);
}

.price {
  color: var(--emerald-deep);
  font-weight: 600;
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}

.view-btn {
  width: 100%;
  background: transparent;
  border: 1px solid var(--emerald-deep);
  color: var(--emerald-deep);
  padding: 0.8rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.view-btn:hover {
  background: var(--emerald-deep);
  color: var(--text-white);
}

.card-actions {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.add-cart-btn {
  width: 100%;
  background: var(--emerald-deep);
  color: white;
  border: none;
  padding: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.add-cart-btn:hover {
  background: var(--emerald-light);
  transform: translateY(-2px);
  box-shadow: 0 4px 10px rgba(12, 62, 42, 0.2);
}

.view-btn {
  font-size: 0.9rem;
}

.card-image-placeholder {
  height: 250px;
  background: rgba(12, 62, 42, 0.03);
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1.5rem;
  overflow: hidden;
  border-radius: 12px;
}

.card-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.placeholder-icon {
  color: var(--gold-primary);
  opacity: 0.3;
}

@media (max-width: 768px) {
  .section-padding {
    padding: 60px 0;
  }
  .grid-layout {
    gap: 1.5rem;
    padding: 0 1rem;
  }
  .section-header {
    margin-bottom: 2.5rem;
  }
}

@media (max-width: 480px) {
  .grid-layout {
    grid-template-columns: 1fr;
  }
  .jewelry-card {
    padding: 1rem;
  }
}
</style>
