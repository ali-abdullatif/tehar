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

      <!-- Main Grid -->
      <div class="dashboard-grid">
        
        <!-- ── Category Management ── -->
        <div class="panel glass-morphism category-panel">
          <h3 class="panel-title">📂 إدارة الأقسام</h3>
          <form @submit.prevent="addCategory" class="mini-form">
            <input v-model="newCategoryName" type="text" placeholder="اسم القسم الجديد..." required />
            <button type="submit" class="mini-submit-btn">إضافة</button>
          </form>
          <div class="category-list">
            <div v-for="cat in categories" :key="cat.id" class="category-tag">
              <span>{{ cat.name }}</span>
              <button @click="deleteCategory(cat.id)" class="tag-delete">✕</button>
            </div>
          </div>
        </div>

        <!-- ── Add Item Form ── -->
        <div class="panel glass-morphism">
          <h3 class="panel-title">✦ إضافة قطعة جديدة</h3>
          <form @submit.prevent="addItem">

            <div class="form-group">
              <label>اسم القطعة</label>
              <input v-model="newItem.name" type="text" required placeholder="مثال: خاتم زمرد ملكي" />
            </div>

            <div class="form-group">
              <label>السعر (ر.س)</label>
              <input v-model.number="newItem.price" type="number" step="0.01" required placeholder="0.00" />
            </div>

            <div class="form-group">
              <label>القسم</label>
              <select v-model="newItem.category_id" class="custom-select">
                <option :value="null">بدون قسم</option>
                <option v-for="cat in categories" :key="cat.id" :value="cat.id">
                  {{ cat.name }}
                </option>
              </select>
            </div>

            <div class="form-group">
              <label>الوصف</label>
              <textarea v-model="newItem.description" rows="3" placeholder="تفاصيل القطعة..."></textarea>
            </div>

            <!-- Image Upload with Preview -->
            <div class="form-group">
              <label>الصورة الرئيسية (Thumbnail)</label>
              <div
                class="upload-zone"
                :class="{ 'has-image': imagePreview, 'dragging': isDragging }"
                @click="$refs.fileInput.click()"
                @dragover.prevent="isDragging = true"
                @dragleave.prevent="isDragging = false"
                @drop.prevent="handleDrop"
              >
                <img v-if="imagePreview" :src="imagePreview" class="image-preview" alt="Preview" />
                <div v-else class="upload-placeholder">
                  <span class="upload-icon">🖼</span>
                  <p>اضغط لرفع الصورة الرئيسية</p>
                </div>
              </div>
              <input ref="fileInput" type="file" accept="image/*" style="display:none" @change="handleFileSelect" />
            </div>

            <!-- Gallery Images -->
            <div class="form-group gallery-form-group">
              <label>صور إضافية للمجموعة (Gallery)</label>
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

            <!-- Upload progress bar -->
            <div v-if="uploadProgress > 0 && uploadProgress < 100" class="progress-bar-wrap">
              <div class="progress-bar" :style="{ width: uploadProgress + '%' }"></div>
            </div>

            <button type="submit" class="submit-btn" :disabled="loading">
              <span v-if="loading" class="spinner"></span>
              <span v-else>✦ إضافة إلى المجموعة</span>
            </button>
          </form>
        </div>

        <!-- ── Items List ── -->
        <div class="panel glass-morphism">
          <h3 class="panel-title">💎 المجموعة الحالية</h3>

          <div v-if="fetchLoading" class="center-msg">جاري التحميل...</div>
          <div v-else-if="items.length === 0" class="empty-state">
            <span style="font-size:3rem">🫙</span>
            <p>لا توجد قطع حالياً، أضف أولى قطعك!</p>
          </div>

          <div v-else class="items-list">
            <transition-group name="list" tag="div">
              <div v-for="item in items" :key="item.id" class="item-row">
                <div class="item-img-wrap">
                  <img
                    v-if="item.image_url"
                    :src="item.image_url"
                    :alt="item.name"
                    class="item-thumb"
                  />
                  <div v-else class="item-thumb-placeholder">✨</div>
                </div>
                <div class="item-info">
                  <div class="item-name">{{ item.name }}</div>
                  <div class="item-price">
                    {{ item.price.toLocaleString('ar-SA') }} ر.س
                    <span v-if="item.category" class="item-cat-badge">{{ item.category.name }}</span>
                  </div>
                </div>
                <div class="item-actions">
                  <button @click="editItem(item)" class="edit-btn" title="تعديل">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 210.336H3V17.5L16.732 3.732z" />
                    </svg>
                  </button>
                  <button @click="deleteItem(item.id)" class="delete-btn" title="حذف">
                    <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                  </button>
                </div>
              </div>
            </transition-group>
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
                <label>السعر (ر.س)</label>
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
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const API_URL = 'http://localhost:8000';
const router = useRouter();

// Reactive state
const items = ref([]);
const categories = ref([]);
const loading = ref(false);
const fetchLoading = ref(true);
const uploadProgress = ref(0);
const imagePreview = ref(null);
const selectedFile = ref(null);
const isDragging = ref(false);
const fileInput = ref(null);

const newItem = ref({ name: '', price: null, description: '', category_id: null, gallery_images: [] });
const newCategoryName = ref('');
const galleryLoading = ref(false);

// Edit state
const editingItem = ref(null);
const editLoading = ref(false);
const editImagePreview = ref(null);
const editSelectedFile = ref(null);
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
    newItem.value = { name: '', price: null, description: '', category_id: null, gallery_images: [] };
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

@media (max-width: 1200px) {
  .dashboard-grid { grid-template-columns: 1fr 1fr; }
  .category-panel { grid-column: span 2; }
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

input, textarea {
  width: 100%;
  padding: 0.8rem 1rem;
  background: rgba(10, 30, 20, 0.7);
  border: 1px solid rgba(255,255,255,0.12);
  color: #f0ebe0;
  border-radius: 8px;
  font-size: 0.95rem;
  transition: border-color 0.3s ease;
  box-sizing: border-box;
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
