<template>
  <div class="admin-dashboard">
    <div class="dash-container">

      <!-- Header Bar -->
      <div class="dash-header glass-morphism">
        <div class="header-left">
          <img src="@/assets/logo.png" alt="Logo" class="header-logo" />
          <div>
            <h1 class="gold-gradient">لوحة التحكم</h1>
            <p class="header-sub">إدارة المجموعة الملكية</p>
          </div>
        </div>
        <button @click="logout" class="logout-btn">
          <span>خروج</span>
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
          </svg>
        </button>
      </div>

      <!-- Stats Row -->
      <div class="stats-row">
        <div class="stat-card glass-morphism">
          <svg xmlns="http://www.w3.org/2000/svg" class="gold-icon" width="32" height="32" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
          </svg>
          <div>
            <div class="stat-number">{{ items.length }}</div>
            <div class="stat-label">إجمالي القطع</div>
          </div>
        </div>
        <div class="stat-card glass-morphism">
          <span class="stat-icon">📂</span>
          <div>
            <div class="stat-number">{{ categories.length }}</div>
            <div class="stat-label">الأقسام</div>
          </div>
        </div>
      </div>

      <!-- Tab Navigation -->
      <div class="tab-nav glass-morphism">
        <button 
          class="tab-btn" 
          :class="{ active: activeTab === 'items' }"
          @click="activeTab = 'items'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
          </svg>
          <span>المجموعة الملكية</span>
        </button>
        <button 
          class="tab-btn" 
          :class="{ active: activeTab === 'categories' }"
          @click="activeTab = 'categories'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" />
          </svg>
          <span>الأقسام</span>
        </button>
        <button 
          class="tab-btn" 
          :class="{ active: activeTab === 'site' }"
          @click="activeTab = 'site'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
          </svg>
          <span>إعدادات الموقع</span>
        </button>
        <button 
          class="tab-btn" 
          :class="{ active: activeTab === 'analytics' }"
          @click="activeTab = 'analytics'"
        >
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 002 2h2a2 2 0 002-2" />
          </svg>
          <span>الإحصائيات</span>
        </button>
      </div>

      <!-- Main Content -->
      <div class="dashboard-content">
        
        <!-- Tab: Items -->
        <div v-if="activeTab === 'items'" class="tab-pane items-grid">
          
          <!-- ── Add Item Form ── -->
          <div class="panel glass-morphism">
            <h3 class="panel-title">✦ إضافة قطعة جديدة</h3>
            <form @submit.prevent="addItem">
              <div class="form-group">
                <label>اسم القطعة</label>
                <input v-model="newItem.name" type="text" required placeholder="مثال: خاتم زمرد ملكي" />
              </div>
              <div class="form-group">
                <label>رمز القطعة (SKU)</label>
                <input v-model="newItem.product_code" type="text" placeholder="مثال: RNG-123" />
              </div>
              <div class="form-group">
                <label>السعر (ر.ي)</label>
                <input v-model.number="newItem.price" type="number" step="0.01" required placeholder="0.00" />
              </div>
              <div class="form-group">
                <label>القسم</label>
                <select v-model="newItem.category_id" class="custom-select">
                  <option :value="null">بدون قسم</option>
                  <option v-for="cat in categories" :key="cat.id" :value="cat.id">{{ cat.name }}</option>
                </select>
              </div>
              <div class="form-group">
                <label>الوصف</label>
                <textarea v-model="newItem.description" rows="3" placeholder="تفاصيل القطعة..."></textarea>
              </div>
              <div class="form-group">
                <label>الصورة الرئيسية</label>
                <div class="upload-zone" :class="{ 'has-image': imagePreview }" @click="$refs.fileInput.click()">
                  <img v-if="imagePreview" :src="imagePreview" class="image-preview" />
                  <div v-else class="upload-placeholder"><span>اضغط لرفع الصورة</span></div>
                </div>
                <input ref="fileInput" type="file" accept="image/*" style="display:none" @change="handleFileSelect" />
              </div>

              <!-- Gallery Images -->
              <div class="form-group">
                <label>صور المجموعة (اختياري)</label>
                <div class="gallery-upload-grid">
                  <div v-for="(img, idx) in newItem.gallery_images" :key="idx" class="gallery-thumb">
                    <img :src="img" />
                    <button type="button" @click="newItem.gallery_images.splice(idx, 1)" class="thumb-remove">✕</button>
                  </div>
                  <button type="button" class="add-gallery-btn" @click="$refs.galleryInput.click()" :disabled="galleryLoading">
                    <span v-if="galleryLoading" class="spinner-small"></span>
                    <span v-else>+</span>
                  </button>
                </div>
                <input ref="galleryInput" type="file" accept="image/*" style="display:none" @change="handleGalleryUpload" />
              </div>
              <button type="submit" class="submit-btn" :disabled="loading">✦ إضافة إلى المجموعة</button>
            </form>
          </div>

          <!-- ── Items List ── -->
          <div class="panel glass-morphism">
            <h3 class="panel-title">💎 المجموعة الحالية</h3>
            <div v-if="fetchLoading" class="center-msg">جاري التحميل...</div>
            <div v-else class="items-list">
              <div v-for="item in items" :key="item.id" class="item-row">
                <div class="item-img-wrap"><img v-if="item.image_url" :src="item.image_url" class="item-thumb" /></div>
                <div class="item-info">
                  <div class="item-name">{{ item.name }}</div>
                  <div class="item-price">{{ item.price.toLocaleString('en-US') }} ر.ي</div>
                </div>
                <div class="item-actions">
                  <button @click="editItem(item)" class="edit-btn">✏️</button>
                  <button @click="deleteItem(item.id)" class="delete-btn">🗑</button>
                </div>
              </div>
            </div>
          </div>

        </div>

        <!-- Tab: Categories -->
        <div v-if="activeTab === 'categories'" class="tab-pane single-panel">
          <div class="panel glass-morphism category-panel-large">
            <h3 class="panel-title">📂 إدارة الأقسام</h3>
            <p class="panel-desc">أضف أقساماً جديدة لتنظيم مجموعتك الملكية</p>
            <form @submit.prevent="addCategory" class="mini-form">
              <input v-model="newCategoryName" type="text" placeholder="اسم القسم الجديد..." required class="luxury-input-gold" />
              <button type="submit" class="mini-submit-btn">إضافة قسم جديد</button>
            </form>
            <div class="category-list-large">
              <div v-for="cat in categories" :key="cat.id" class="category-tag-large glass-morphism">
                <span>{{ cat.name }}</span>
                <button @click="deleteCategory(cat.id)" class="tag-delete">✕</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Tab: Site Settings -->
        <div v-if="activeTab === 'site'" class="tab-pane single-panel">
          <div class="panel glass-morphism site-config-panel-large">
            <h3 class="panel-title">🏠 محتوى الموقع</h3>
            <p class="panel-desc">تحكم في نصوص وصور الواجهة الرئيسية ومعلومات التواصل</p>
            
            <div class="config-layout">
              <div class="config-section">
                <h4>✨ القسم الرئيسي</h4>
                <div class="form-group">
                  <label>عنوان الرئيسية</label>
                  <input v-model="siteConfig.hero_title" @change="siteConfig.update('hero_title', siteConfig.hero_title)" type="text" />
                </div>
                <div class="form-group">
                  <label>الوصف الترحيبي</label>
                  <textarea v-model="siteConfig.hero_subtitle" @change="siteConfig.update('hero_subtitle', siteConfig.hero_subtitle)" rows="3"></textarea>
                </div>
              </div>

              <div class="config-section">
                <h4>🖼 صورة الواجهة</h4>
                <div class="hero-preview-zone" @click="$refs.heroInput.click()" :class="{ 'is-loading': heroUploading }">
                  <div v-if="heroUploading" class="upload-overlay">
                    <span class="spinner"></span>
                  </div>
                  <img v-if="siteConfig.hero_image && !heroUploading" :src="siteConfig.hero_image" class="hero-preview-img" />
                  <div v-else-if="!heroUploading" class="hero-preview-placeholder">
                    <span>رفع صورة احترافية (1920x1080)</span>
                  </div>
                </div>
                <input ref="heroInput" type="file" style="display:none" accept="image/*" @change="handleHeroUpload" />
              </div>

              <div class="config-section full-width">
                <h4>📞 معلومات التواصل</h4>
                <div class="config-grid-3">
                  <div class="form-group">
                    <label>العنوان</label>
                    <input v-model="siteConfig.footer_address" @change="siteConfig.update('footer_address', siteConfig.footer_address)" type="text" />
                  </div>
                  <div class="form-group">
                    <label>البريد الإلكتروني</label>
                    <input v-model="siteConfig.footer_email" @change="siteConfig.update('footer_email', siteConfig.footer_email)" type="text" />
                  </div>
                  <div class="form-group">
                    <label>رقم الواتساب</label>
                    <input v-model="siteConfig.footer_phone" @change="siteConfig.update('footer_phone', siteConfig.footer_phone)" type="text" placeholder="966..." />
                  </div>
                </div>
                <div class="form-group" style="margin-top: 1.5rem;">
                  <label>مقدمة رسالة الواتساب</label>
                  <textarea v-model="siteConfig.whatsapp_message" @change="siteConfig.update('whatsapp_message', siteConfig.whatsapp_message)" rows="3" placeholder="أدخل الرسالة التي ستظهر في بداية طلب الواتساب..."></textarea>
                </div>
              </div>
              <div class="config-section full-width" style="margin-top: 2rem;">
                <h4>💾 النسخ الاحتياطي</h4>
                <p class="panel-desc">تحميل نسخة احتياطية من قاعدة البيانات والصور المرفوعة</p>
                <button @click="handleExport" class="export-btn" :disabled="exporting">
                  <span v-if="exporting" class="spinner-small"></span>
                  <span v-else>تحميل نسخة احتياطية (Zip)</span>
                </button>
              </div>
            </div>
          </div>
        </div>

        <!-- Tab: Analytics -->
        <div v-if="activeTab === 'analytics'" class="tab-pane">
           <AnalyticsCharts />
        </div>

      </div>

      </div>

      <!-- ── Edit Modal ── -->
      <transition name="modal">
        <div v-if="editingItem" class="modal-overlay" @click.self="cancelEdit">
          <div class="modal-card glass-morphism">
            <div class="modal-header">
              <h3 class="panel-title" style="margin-bottom:0; border:none; padding-bottom:0;">✏️ تعديل القطعة</h3>
              <button @click="cancelEdit" class="modal-close">✕</button>
            </div>
            <form @submit.prevent="updateItem">
              <div class="form-group">
                <label>اسم القطعة</label>
                <input v-model="editingItem.name" type="text" required />
              </div>
              <div class="form-group">
                <label>رمز القطعة (SKU)</label>
                <input v-model="editingItem.product_code" type="text" />
              </div>
              <div class="form-group">
                <label>السعر (ر.ي)</label>
                <input v-model.number="editingItem.price" type="number" step="0.01" required />
              </div>
              <div class="form-group">
                <label>القسم</label>
                <select v-model="editingItem.category_id" class="custom-select">
                  <option :value="null">بدون قسم</option>
                  <option v-for="cat in categories" :key="cat.id" :value="cat.id">
                    {{ cat.name }}
                  </option>
                </select>
              </div>
              <div class="form-group">
                <label>الوصف</label>
                <textarea v-model="editingItem.description" rows="3"></textarea>
              </div>
              <div class="form-group">
                <label>الصورة الرئيسية</label>
                <div
                  class="upload-zone mini"
                  :class="{ 'has-image': editImagePreview, 'dragging': editIsDragging }"
                  @click="$refs.editFileInput.click()"
                  @dragover.prevent="editIsDragging = true"
                  @dragleave.prevent="editIsDragging = false"
                  @drop.prevent="handleEditDrop"
                >
                  <img v-if="editImagePreview" :src="editImagePreview" class="image-preview" alt="Preview" />
                  <div v-else class="upload-placeholder">
                    <span class="upload-icon">🖼</span>
                    <p>رفع صورة</p>
                  </div>
                </div>
                <input ref="editFileInput" type="file" accept="image/*" style="display:none" @change="handleEditFileSelect" />
              </div>

              <!-- Edit Gallery -->
              <div class="form-group">
                <label>صور المجموعة</label>
                <div class="gallery-upload-grid">
                  <div v-for="(img, idx) in editingItem.gallery_urls" :key="idx" class="gallery-thumb">
                    <img :src="img" />
                    <button type="button" @click="editingItem.gallery_urls.splice(idx, 1)" class="thumb-remove">✕</button>
                  </div>
                  <button type="button" class="add-gallery-btn" @click="$refs.editGalleryInput.click()" :disabled="galleryLoading">
                    <span v-if="galleryLoading" class="spinner-small"></span>
                    <span v-else>+</span>
                  </button>
                </div>
                <input ref="editGalleryInput" type="file" accept="image/*" style="display:none" @change="handleEditGalleryUpload" />
              </div>
              <div class="modal-actions">
                <button type="button" class="cancel-btn" @click="cancelEdit">إلغاء</button>
                <button type="submit" class="submit-btn" :disabled="editLoading">
                  <span v-if="editLoading" class="spinner"></span>
                  <span v-else>✦ حفظ التعديلات</span>
                </button>
              </div>
            </form>
          </div>
        </div>
      </transition>

    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { siteConfig } from '@/store/siteStore';
import AnalyticsCharts from '@/components/AnalyticsCharts.vue';

const API_URL = '/api';
const router = useRouter();

// Reactive state
const activeTab = ref('items');
const items = ref([]);
const categories = ref([]);
const loading = ref(false);
const fetchLoading = ref(true);
const uploadProgress = ref(0);
const imagePreview = ref(null);
const selectedFile = ref(null);
const isDragging = ref(false);
const fileInput = ref(null);
const galleryInput = ref(null);

const newItem = ref({ name: '', product_code: '', price: null, description: '', category_id: null, gallery_images: [] });
const newCategoryName = ref('');
const galleryLoading = ref(false);
const heroUploading = ref(false);

// Edit state
const editingItem = ref(null);
const editLoading = ref(false);
const editImagePreview = ref(null);
const editSelectedFile = ref(null);

const exporting = ref(false);
const editIsDragging = ref(false);
const editFileInput = ref(null);

// Helper: get auth header
const authHeader = () => ({
  headers: { Authorization: `Bearer ${localStorage.getItem('admin_token')}` }
});

// Fetch items from backend
const fetchItems = async () => {
  fetchLoading.value = true;
  try {
    const res = await axios.get(`${API_URL}/items`);
    items.value = res.data;
  } catch (e) {
    console.error('Error fetching items:', e);
  } finally {
    fetchLoading.value = false;
  }
};

const fetchCategories = async () => {
  try {
    const res = await axios.get(`${API_URL}/categories`);
    categories.value = res.data;
  } catch (e) {
    console.error('Error fetching categories:', e);
  }
};

// Category Management
const addCategory = async () => {
  if (!newCategoryName.value.trim()) return;
  try {
    await axios.post(`${API_URL}/categories`, { name: newCategoryName.value }, authHeader());
    newCategoryName.value = '';
    await fetchCategories();
  } catch (e) {
    console.error('Error adding category:', e);
  }
};

const deleteCategory = async (id) => {
  if (!confirm('سيتم حذف القسم فقط، القطع ستبقى بدون قسم. هل أنت متأكد؟')) return;
  try {
    await axios.delete(`${API_URL}/categories/${id}`, authHeader());
    await fetchCategories();
    await fetchItems(); // Refresh items to update categories display
  } catch (e) {
    console.error('Error deleting category:', e);
  }
};

// File selection from input
const handleFileSelect = (e) => {
  const file = e.target.files[0];
  if (file) setFile(file);
};

// Drag-and-drop
const handleDrop = (e) => {
  isDragging.value = false;
  const file = e.dataTransfer.files[0];
  if (file && file.type.startsWith('image/')) setFile(file);
};

const setFile = (file) => {
  selectedFile.value = file;
  const reader = new FileReader();
  reader.onload = (e) => { imagePreview.value = e.target.result; };
  reader.readAsDataURL(file);
};

const clearImage = () => {
  imagePreview.value = null;
  selectedFile.value = null;
  if (fileInput.value) fileInput.value.value = '';
};

// Upload image to backend, returns URL
const uploadImageFile = async (file) => {
  if (!file) return null;
  const formData = new FormData();
  formData.append('file', file);
  const res = await axios.post(`${API_URL}/upload`, formData, {
    ...authHeader(),
    headers: { ...authHeader().headers, 'Content-Type': 'multipart/form-data' },
  });
  return res.data.url;
};

const handleExport = async () => {
  exporting.value = true;
  try {
    const token = localStorage.getItem('admin_token');
    const response = await axios.get(`${API_URL}/backup/export`, {
      headers: { Authorization: `Bearer ${token}` },
      responseType: 'blob'
    });
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'tihar_backup.zip');
    document.body.appendChild(link);
    link.click();
    link.parentNode.removeChild(link);
  } catch (error) {
    alert('حدث خطأ أثناء تصدير النسخة الاحتياطية');
    console.error(error);
  } finally {
    exporting.value = false;
  }
};

const handleHeroUpload = async (e) => {
  const file = e.target.files[0];
  if (!file) return;
  heroUploading.value = true;
  try {
    const url = await uploadImageFile(file);
    if (url) {
      siteConfig.hero_image = url;
      siteConfig.update('hero_image', url);
    }
  } catch (e) {
    console.error('Error uploading hero image:', e);
  } finally {
    heroUploading.value = false;
  }
};

const handleGalleryUpload = async (e) => {
  const file = e.target.files[0];
  if (!file) return;
  galleryLoading.value = true;
  try {
    const url = await uploadImageFile(file);
    if (url) newItem.value.gallery_images.push(url);
  } finally {
    galleryLoading.value = false;
  }
};

const handleEditGalleryUpload = async (e) => {
  const file = e.target.files[0];
  if (!file) return;
  galleryLoading.value = true;
  try {
    const url = await uploadImageFile(file);
    if (url) editingItem.value.gallery_urls.push(url);
  } finally {
    galleryLoading.value = false;
  }
};

// Add new item
const addItem = async () => {
  loading.value = true;
  try {
    // 1. Upload image if selected
    const imageUrl = await uploadImageFile(selectedFile.value);

    // 2. Create item
    await axios.post(
      `${API_URL}/items`,
      {
        ...newItem.value,
        image_url: imageUrl || ''
      },
      authHeader()
    );

    // 3. Reset form
    newItem.value = { name: '', product_code: '', price: null, description: '', category_id: null, gallery_images: [] };
    clearImage();
    await fetchItems();
  } catch (e) {
    if (e.response?.status === 401) {
      logout();
    } else {
      console.error('Error adding item:', e);
    }
  } finally {
    loading.value = false;
  }
};

// Delete item
const deleteItem = async (id) => {
  if (!confirm('هل أنت متأكد من حذف هذه القطعة؟')) return;
  try {
    await axios.delete(`${API_URL}/items/${id}`, authHeader());
    await fetchItems();
  } catch (e) {
    if (e.response?.status === 401) logout();
    else console.error('Error deleting item:', e);
  }
};

// ── Edit Item ──
const editItem = (item) => {
  editingItem.value = { 
    ...item, 
    gallery_urls: item.images ? item.images.map(i => i.url) : [] 
  };
  editImagePreview.value = item.image_url || null;
  editSelectedFile.value = null;
};

const cancelEdit = () => {
  editingItem.value = null;
  editImagePreview.value = null;
  editSelectedFile.value = null;
};

const handleEditFileSelect = (e) => {
  const file = e.target.files[0];
  if (file) setEditFile(file);
};

const handleEditDrop = (e) => {
  editIsDragging.value = false;
  const file = e.dataTransfer.files[0];
  if (file && file.type.startsWith('image/')) setEditFile(file);
};

const setEditFile = (file) => {
  editSelectedFile.value = file;
  const reader = new FileReader();
  reader.onload = (e) => { editImagePreview.value = e.target.result; };
  reader.readAsDataURL(file);
};

const clearEditImage = () => {
  editImagePreview.value = null;
  editSelectedFile.value = null;
  if (editFileInput.value) editFileInput.value.value = '';
};

const uploadEditImage = async () => {
  if (!editSelectedFile.value) return null;
  const formData = new FormData();
  formData.append('file', editSelectedFile.value);
  const res = await axios.post(`${API_URL}/upload`, formData, {
    ...authHeader(),
    headers: { ...authHeader().headers, 'Content-Type': 'multipart/form-data' },
  });
  return res.data.url;
};

const updateItem = async () => {
  editLoading.value = true;
  try {
    // Upload new image if file was selected
    let imageUrl = editingItem.value.image_url;
    if (editSelectedFile.value) {
      imageUrl = await uploadEditImage();
    } else if (!editImagePreview.value) {
      imageUrl = ''; // image was removed
    }

    await axios.put(
      `${API_URL}/items/${editingItem.value.id}`,
      {
        name: editingItem.value.name,
        product_code: editingItem.value.product_code || null,
        price: editingItem.value.price,
        description: editingItem.value.description || '',
        category_id: editingItem.value.category_id,
        image_url: imageUrl || '',
        gallery_images: editingItem.value.gallery_urls
      },
      authHeader()
    );
    cancelEdit();
    await fetchItems();
  } catch (e) {
    if (e.response?.status === 401) logout();
    else console.error('Error updating item:', e);
  } finally {
    editLoading.value = false;
  }
};

// Logout
const logout = () => {
  localStorage.removeItem('admin_token');
  router.push('/admin/login');
};

onMounted(async () => {
  await fetchCategories();
  await fetchItems();
});
</script>

<style scoped>
.admin-dashboard {
  min-height: 100vh;
  background: var(--bg-deep);
  color: var(--text-white);
  padding-top: 80px;
}

.dash-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

/* Header */
.dash-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1.5rem 2rem;
  margin-bottom: 1.5rem;
  border-radius: 16px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(212,175,55,0.15);
}

.header-left {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-logo {
  height: 48px;
  width: auto;
  object-fit: contain;
  filter: brightness(0) invert(1);
}

h1 { font-size: 1.8rem; margin: 0; }
.header-sub { color: var(--text-muted); font-size: 0.85rem; margin: 0; }

.logout-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.6rem 1.2rem;
  background: rgba(206,55,55,0.15);
  border: 1px solid rgba(206,55,55,0.35);
  color: #ff8585;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.95rem;
  transition: all 0.3s ease;
}
.logout-btn:hover {
  background: rgba(206,55,55,0.3);
}

/* Stats */
.stats-row {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.stat-card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.2rem 1.8rem;
  border-radius: 12px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(212,175,55,0.1);
}

.stat-icon { font-size: 2rem; }
.stat-number { font-size: 2rem; font-weight: 700; color: #d4af37; line-height: 1; }
.stat-label { color: var(--text-muted); font-size: 0.85rem; }

/* Grid */
.dashboard-grid {
  display: grid;
  grid-template-columns: 280px 1fr 1fr;
  gap: 1.5rem;
}

.gold-icon {
  color: var(--gold-primary);
}

.sub-section-title {
  color: var(--gold-light);
  margin: 2rem 0 1rem;
  font-size: 1.1rem;
  border-bottom: 1px solid rgba(212,175,55,0.1);
  padding-bottom: 0.5rem;
}

.config-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1.5rem;
}

.config-grid.compact {
  grid-template-columns: 1fr 1fr;
}

.site-config-panel {
  grid-column: span 1;
}

@media (max-width: 1200px) {
  .dashboard-grid { grid-template-columns: 1fr; }
  .site-config-panel { grid-column: span 1; }
}

.panel {
  padding: 2rem;
  border-radius: 16px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(212,175,55,0.1);
}

.category-panel {
  display: flex;
  flex-direction: column;
}

.mini-form {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.mini-form input {
  padding: 0.6rem;
  font-size: 0.85rem;
  flex: 1;
}

.mini-submit-btn {
  background: #d4af37;
  color: #0c3e2a;
  border: none;
  border-radius: 6px;
  padding: 0 1rem;
  font-weight: 600;
  cursor: pointer;
  font-size: 0.8rem;
}

.category-list {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
}

.category-tag {
  background: rgba(212,175,55,0.1);
  border: 1px solid rgba(212,175,55,0.2);
  color: #d4af37;
  padding: 0.4rem 0.8rem;
  border-radius: 20px;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.tag-delete {
  background: none;
  border: none;
  color: #ff8585;
  cursor: pointer;
  padding: 0;
  font-size: 0.8rem;
}

.custom-select {
  width: 100%;
  padding: 0.8rem 1rem;
  background: rgba(10, 30, 20, 0.7);
  border: 1px solid rgba(255,255,255,0.12);
  color: #f0ebe0;
  border-radius: 8px;
  font-size: 0.95rem;
  appearance: none;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23d4af37' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: left 1rem center;
  background-size: 1em;
}

.item-cat-badge {
  display: inline-block;
  font-size: 0.7rem;
  background: rgba(212,175,55,0.1);
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  margin-right: 0.5rem;
}

.panel-title {
  color: #d4af37;
  font-size: 1.1rem;
  margin-bottom: 1.8rem;
  padding-bottom: 0.8rem;
  border-bottom: 1px solid rgba(212,175,55,0.15);
}

/* Form */
.form-group { margin-bottom: 1.4rem; }

label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--text-muted);
  font-size: 0.9rem;
}

input, textarea, .custom-select {
  width: 100%;
  padding: 0.8rem 1rem;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(212, 175, 55, 0.2);
  border-radius: 8px;
  color: #1a2e25;
  outline: none;
  transition: all 0.2s;
}

.luxury-input-gold {
  background: #fffcf0 !important;
  border: 2px solid #d4af37 !important;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1);
  color: #0c3e2a !important;
  font-weight: 600;
}

input::placeholder, textarea::placeholder {
  color: #888888;
}

input:focus, textarea:focus {
  outline: none;
  border-color: #d4af37;
  box-shadow: 0 0 0 3px rgba(212,175,55,0.1);
}

/* Override browser autofill white background */
input:-webkit-autofill,
input:-webkit-autofill:hover,
input:-webkit-autofill:focus {
  -webkit-text-fill-color: #f0ebe0;
  -webkit-box-shadow: 0 0 0 1000px rgba(10, 30, 20, 0.9) inset;
  transition: background-color 5000s ease-in-out 0s;
}

/* Upload Zone */
.upload-zone {
  border: 2px dashed rgba(212,175,55,0.3);
  border-radius: 10px;
  min-height: 160px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  background: rgba(255,255,255,0.02);
}
.upload-zone:hover, .upload-zone.dragging {
  border-color: #d4af37;
  background: rgba(212,175,55,0.05);
}
.upload-zone.has-image { border-style: solid; border-color: rgba(212,175,55,0.4); }

.upload-placeholder { text-align: center; }
.upload-icon { font-size: 2.5rem; display: block; margin-bottom: 0.5rem; }
.upload-placeholder p { color: var(--text-muted); margin: 0.4rem 0; font-size: 0.9rem; }
.upload-hint { color: rgba(255,255,255,0.3); font-size: 0.78rem; }

.image-preview {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}

.image-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 0.9rem;
  opacity: 0;
  transition: opacity 0.3s;
}
.upload-zone:hover .image-overlay { opacity: 1; }

.remove-image-btn {
  margin-top: 0.5rem;
  background: none;
  border: none;
  color: #ff8585;
  cursor: pointer;
  font-size: 0.85rem;
  padding: 0;
}

/* Progress bar */
.progress-bar-wrap {
  height: 4px;
  background: rgba(255,255,255,0.1);
  border-radius: 2px;
  margin-bottom: 1rem;
  overflow: hidden;
}
.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, #0c3e2a, #d4af37);
  border-radius: 2px;
  transition: width 0.3s ease;
}

/* Submit */
.submit-btn {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(135deg, #0c3e2a 0%, #1a6645 100%);
  border: 1px solid rgba(212,175,55,0.3);
  color: white;
  border-radius: 10px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}
.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(12,62,42,0.5);
}
.submit-btn:disabled { opacity: 0.5; cursor: not-allowed; }

.spinner {
  display: inline-block;
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* Items List */
.items-list { display: flex; flex-direction: column; gap: 0.8rem; max-height: 520px; overflow-y: auto; padding-right: 4px; }

.item-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.8rem;
  background: rgba(255,255,255,0.04);
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,0.06);
  transition: border-color 0.3s ease;
}
.item-row:hover { border-color: rgba(212,175,55,0.2); }

.item-img-wrap { flex-shrink: 0; }
.item-thumb {
  width: 56px;
  height: 56px;
  object-fit: cover;
  border-radius: 8px;
  border: 1px solid rgba(212,175,55,0.2);
}
.item-thumb-placeholder {
  width: 56px;
  height: 56px;
  background: rgba(255,255,255,0.06);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
}
.upload-zone {
  width: 100%;
  height: 180px;
  border: 2px dashed rgba(212, 175, 55, 0.2);
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  overflow: hidden;
  position: relative;
  transition: all 0.3s;
}

.upload-zone.mini { height: 120px; }

.gallery-upload-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin-top: 1rem;
}

.gallery-thumb {
  width: 60px;
  height: 60px;
  border-radius: 8px;
  position: relative;
  border: 1px solid rgba(212, 175, 55, 0.3);
}
.gallery-thumb img { width: 100%; height: 100%; object-fit: cover; border-radius: 7px; }

.thumb-remove {
  position: absolute;
  top: -5px;
  left: -5px;
  width: 20px;
  height: 20px;
  background: #ff4757;
  color: white;
  border: none;
  border-radius: 50%;
  font-size: 0.7rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.add-gallery-btn {
  width: 60px;
  height: 60px;
  border: 2px dashed rgba(212, 175, 55, 0.3);
  background: none;
  color: var(--gold-primary);
  font-size: 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
}
.add-gallery-btn:hover { background: rgba(212, 175, 55, 0.05); }

.spinner-small {
  width: 15px;
  height: 15px;
  border: 2px solid rgba(212, 175, 55, 0.2);
  border-top-color: var(--gold-primary);
  border-radius: 50%;
  animation: rotate 1s linear infinite;
}
@keyframes rotate { to { transform: rotate(360deg); } }

.item-info { flex: 1; }
.item-name { font-weight: 600; font-size: 0.95rem; margin-bottom: 0.2rem; }
.item-price { color: #d4af37; font-size: 0.85rem; }

.item-actions {
  display: flex;
  gap: 0.4rem;
  flex-shrink: 0;
}

.edit-btn {
  background: rgba(212,175,55,0.15);
  border: 1px solid rgba(212,175,55,0.3);
  border-radius: 8px;
  padding: 0.5rem 0.7rem;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.2s ease;
}
.edit-btn:hover { background: rgba(212,175,55,0.3); }

.delete-btn {
  background: rgba(206,55,55,0.15);
  border: 1px solid rgba(206,55,55,0.3);
  border-radius: 8px;
  padding: 0.5rem 0.7rem;
  cursor: pointer;
  font-size: 1rem;
  transition: all 0.2s ease;
}
.delete-btn:hover { background: rgba(206,55,55,0.3); }

/* Tabs */
.tab-nav {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  padding: 0.5rem;
  border-radius: 12px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(212,175,55,0.1);
}

.tab-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  padding: 1rem;
  background: none;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s;
}

.tab-btn svg {
  width: 20px;
  height: 20px;
  opacity: 0.7;
}

.tab-btn:hover {
  background: rgba(212, 175, 55, 0.05);
  color: var(--gold-light);
}

.tab-btn.active {
  background: var(--gold-primary);
  color: #ffffff;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2);
}

.tab-btn.active svg {
  color: #ffffff;
  opacity: 1;
}

/* Grids */
.items-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
}

.single-panel {
  max-width: 1000px;
  margin: 0 auto;
}

.panel-desc {
  color: var(--text-muted);
  margin-bottom: 2rem;
  font-size: 0.9rem;
}

/* Category Large */
.category-list-large {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
  margin-top: 2rem;
}

.category-tag-large {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(212,175,55,0.1);
  color: var(--emerald-deep);
  font-weight: 600;
}

/* Site Config Large */
.config-layout {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
}

.config-section h4 {
  color: var(--gold-light);
  margin-bottom: 1.5rem;
  font-size: 1.1rem;
}

.config-section.full-width {
  grid-column: span 2;
}

.config-grid-3 {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1.5rem;
}

.hero-preview-zone {
  width: 100%;
  height: 250px;
  border-radius: 12px;
  overflow: hidden;
  border: 2px dashed rgba(212,175,55,0.3);
  cursor: pointer;
  position: relative;
}

.hero-preview-zone.is-loading {
  pointer-events: none;
  opacity: 0.8;
}

.upload-overlay {
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
  border-radius: 12px;
}

.hero-preview-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-preview-placeholder {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--text-muted);
  text-align: center;
  padding: 2rem;
}

.export-btn {
  background: linear-gradient(135deg, #0c3e2a 0%, #1a6645 100%);
  color: white;
  border: 1px solid rgba(212, 175, 55, 0.4);
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
  margin-top: 1rem;
}
.export-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
}
.export-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

@media (max-width: 992px) {
  .items-grid, .config-layout, .config-grid-3 {
    grid-template-columns: 1fr;
  }
  .config-section.full-width {
    grid-column: span 1;
  }
  .tab-nav {
    flex-direction: column;
  }
}

/* ── Edit Modal ── */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.7);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1rem;
}

.modal-card {
  width: 100%;
  max-width: 520px;
  max-height: 90vh;
  overflow-y: auto;
  padding: 2rem;
  border-radius: 16px;
  background: rgba(15,30,22,0.95);
  border: 1px solid rgba(212,175,55,0.2);
  box-shadow: 0 30px 60px rgba(0,0,0,0.5);
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.modal-close {
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 1.4rem;
  cursor: pointer;
  padding: 0.2rem 0.5rem;
  transition: color 0.2s;
}
.modal-close:hover { color: #ff8585; }

.modal-actions {
  display: flex;
  gap: 1rem;
  margin-top: 0.5rem;
}

.cancel-btn {
  flex: 1;
  padding: 0.9rem;
  background: rgba(255,255,255,0.06);
  border: 1px solid rgba(255,255,255,0.12);
  color: var(--text-muted);
  border-radius: 10px;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.2s;
}
.cancel-btn:hover { background: rgba(255,255,255,0.1); color: white; }

.modal-actions .submit-btn { flex: 2; }

/* Modal transition */
.modal-enter-active { transition: all 0.3s ease; }
.modal-leave-active { transition: all 0.2s ease; }
.modal-enter-from { opacity: 0; }
.modal-enter-from .modal-card { transform: scale(0.92) translateY(20px); }
.modal-leave-to { opacity: 0; }
.modal-leave-to .modal-card { transform: scale(0.95); }

/* Modal scrollbar */
.modal-card::-webkit-scrollbar { width: 4px; }
.modal-card::-webkit-scrollbar-track { background: transparent; }
.modal-card::-webkit-scrollbar-thumb { background: rgba(212,175,55,0.3); border-radius: 2px; }

/* Empty / Loading */
.center-msg, .empty-state {
  text-align: center;
  color: var(--text-muted);
  padding: 3rem 1rem;
}
.empty-state p { margin-top: 1rem; }

/* List transition */
.list-enter-active, .list-leave-active { transition: all 0.4s ease; }
.list-enter-from { opacity: 0; transform: translateX(20px); }
.list-leave-to { opacity: 0; transform: translateX(-20px); }

/* Scrollbar */
.items-list::-webkit-scrollbar { width: 4px; }
.items-list::-webkit-scrollbar-track { background: transparent; }
.items-list::-webkit-scrollbar-thumb { background: rgba(212,175,55,0.3); border-radius: 2px; }

@media (max-width: 1024px) {
  .dashboard-grid { grid-template-columns: 1fr; }
}

@media (max-width: 600px) {
  .dash-container { padding: 1rem; }
  h1 { font-size: 1.4rem; }
}
</style>
