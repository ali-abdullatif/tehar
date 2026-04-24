<template>
  <div class="analytics-container">
    <div v-if="loading" class="loader-overlay">
      <div class="spinner"></div>
      <p>جاري تحليل البيانات...</p>
    </div>

    <div v-else class="analytics-grid">
      
      <!-- TopRow: Summary Cards -->
      <div class="summary-cards">
        <div class="stat-box glass-morphism">
          <h4>معدل التحويل</h4>
          <div class="val">{{ conversionRate }}%</div>
          <div class="sub">نسبة (عرض ← شراء)</div>
        </div>
        <div class="stat-box glass-morphism">
          <h4>تخلي عن السلة</h4>
          <div class="val text-red">{{ stats.cart_abandonment_rate }}%</div>
          <div class="sub">إضافة للسلة بدون شراء</div>
        </div>
        <div class="stat-box glass-morphism">
          <h4>إجمالي المبيعات</h4>
          <div class="val">{{ stats.conversion_funnel.purchase }}</div>
          <div class="sub">قطعة مباعة</div>
        </div>
      </div>

      <!-- Main Charts Grid -->
      <div class="charts-inner-grid">
        
        <!-- Sales Over Time (Line) -->
        <div class="chart-card glass-morphism">
          <h3>📈 المبيعات اليومية</h3>
          <div class="chart-wrap">
            <Line :data="dailySalesData" :options="chartOptions" />
          </div>
        </div>

        <!-- Funnel (Bar) -->
        <div class="chart-card glass-morphism">
          <h3>🌪 قمع المبيعات</h3>
          <div class="chart-wrap">
            <Bar :data="funnelData" :options="chartOptions" />
          </div>
        </div>

        <!-- Hourly Activity (Bar) -->
        <div class="chart-card glass-morphism">
          <h3>🕒 النشاط بالساعات</h3>
          <div class="chart-wrap">
            <Bar :data="hourlyData" :options="chartOptions" />
          </div>
        </div>

        <!-- Top Products Viewed -->
        <div class="chart-card glass-morphism">
          <h3>💎 الأكثر مشاهدة</h3>
          <div class="chart-wrap">
            <Bar :data="topProductsData" :options="horizontalBarOptions" />
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Filler
} from 'chart.js';
import { Bar, Line } from 'vue-chartjs';

ChartJS.register(
  Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale,
  LineElement, PointElement, Filler
);

const stats = ref({
  daily_sales: [],
  hourly_activity: [],
  top_viewed: [],
  top_cart: [],
  conversion_funnel: { views: 0, add_to_cart: 0, purchase: 0 },
  cart_abandonment_rate: 0
});
const loading = ref(true);

const conversionRate = computed(() => {
  if (stats.value.conversion_funnel.views === 0) return 0;
  return ((stats.value.conversion_funnel.purchase / stats.value.conversion_funnel.views) * 100).toFixed(1);
});

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: { display: false }
  },
  scales: {
    y: { beginAtZero: true, grid: { color: 'rgba(212, 175, 55, 0.1)' } },
    x: { grid: { display: false } }
  }
};

const horizontalBarOptions = {
  ...chartOptions,
  indexAxis: 'y'
};

const fetchStats = async () => {
  try {
    const token = localStorage.getItem('admin_token');
    const res = await axios.get('http://localhost:8000/analytics/dashboard', {
      headers: { Authorization: `Bearer ${token}` }
    });
    stats.value = res.data;
  } catch (e) {
    console.error('Error fetching analytics:', e);
  } finally {
    loading.value = false;
  }
};

onMounted(fetchStats);

// Chart Data Drivers
const dailySalesData = computed(() => ({
  labels: stats.value.daily_sales.map(s => s.date),
  datasets: [{
    label: 'المبيعات',
    data: stats.value.daily_sales.map(s => s.count),
    borderColor: '#d4af37',
    backgroundColor: 'rgba(212, 175, 55, 0.1)',
    fill: true,
    tension: 0.4
  }]
}));

const funnelData = computed(() => ({
  labels: ['مشاهدة', 'إضافة للسلة', 'شراء'],
  datasets: [{
    data: [
      stats.value.conversion_funnel.views,
      stats.value.conversion_funnel.add_to_cart,
      stats.value.conversion_funnel.purchase
    ],
    backgroundColor: ['#0c3e2a', '#d4af37', '#25D366']
  }]
}));

const hourlyData = computed(() => ({
  labels: Array.from({length: 24}, (_, i) => i),
  datasets: [{
    label: 'النشاط',
    data: stats.value.hourly_activity.reduce((acc, curr) => {
      acc[curr.hour] = curr.count;
      return acc;
    }, Array(24).fill(0)),
    backgroundColor: '#d4af37'
  }]
}));

const topProductsData = computed(() => ({
  labels: stats.value.top_viewed.map(p => p.product_name),
  datasets: [{
    label: 'المشاهدات',
    data: stats.value.top_viewed.map(p => p.count),
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderColor: '#d4af37',
    borderWidth: 1
  }]
}));
</script>

<style scoped>
.analytics-container { padding: 1rem; }
.analytics-grid { display: flex; flex-direction: column; gap: 2rem; }

.summary-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.stat-box {
  padding: 1.5rem;
  text-align: center;
  border-radius: 12px;
}

.stat-box h4 { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 0.5rem; }
.stat-box .val { font-size: 2rem; font-weight: 700; color: var(--gold-primary); }
.val.text-red { color: #ff4757; }
.stat-box .sub { font-size: 0.75rem; opacity: 0.6; margin-top: 0.5rem; }

.charts-inner-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.chart-card {
  padding: 1.5rem;
  border-radius: 16px;
  height: 350px;
  display: flex;
  flex-direction: column;
}

.chart-card h3 { font-size: 1.1rem; margin-bottom: 1.5rem; color: #d4af37; }
.chart-wrap { flex: 1; min-height: 0; }

.loader-overlay {
  height: 400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: var(--gold-primary);
}

@media (max-width: 992px) {
  .charts-inner-grid { grid-template-columns: 1fr; }
}
</style>
