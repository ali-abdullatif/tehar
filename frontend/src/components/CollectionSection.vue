<template>
  <section id="collection" class="collection section-padding">
    <div class="container">
      <div class="section-header">
        <h3 class="gold-gradient">روائعنا المختارة</h3>
        <p>نخبة من أجود المصاغ المرصع بأنقى الأحجار الكريمة</p>
      </div>
      
      <div v-if="loading" style="text-align: center; color: white;">جاري التحميل...</div>
      <div v-else-if="items.length === 0" style="text-align: center; color: white;">لا توجد قطع حالياً.</div>

      <div v-else class="grid-layout">
        <div v-for="item in items" :key="item.id" class="jewelry-card glass-morphism">
          <div class="card-image-placeholder" :style="item.image_url ? `background-image: url(${item.image_url}); background-size: cover; background-position: center;` : ''">
            <span v-if="!item.image_url" class="icon">✨</span>
          </div>
          <div class="card-content">
            <h4>{{ item.name }}</h4>
            <p class="price">{{ item.price }} ر.س</p>
            <button class="view-btn">عرض التفاصيل</button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const API_URL = 'http://localhost:8000';
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

.grid-layout {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.jewelry-card {
  padding: 1.5rem;
  background: var(--bg-soft);
  transition: all 0.4s ease;
  cursor: pointer;
  border: 1px solid rgba(12, 62, 42, 0.05);
}

.jewelry-card:hover {
  transform: translateY(-10px);
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
