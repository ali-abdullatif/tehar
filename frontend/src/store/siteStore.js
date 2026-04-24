import { reactive } from 'vue';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const siteConfig = reactive({
  hero_title: 'مجوهرات الملوك',
  hero_subtitle: 'الأناقة التي تليق بكم. حكايات من الذهب والألماس تروى بكل فخر وانتماء.',
  hero_image: '', // Primary hero background
  footer_address: 'جدة، المملكة العربية السعودية',
  footer_email: 'info@kingsjewelry.com',
  footer_phone: '966500000000',
  
  loading: true,
  
  async fetch() {
    this.loading = true;
    try {
      const res = await axios.get(`${API_URL}/config`);
      res.data.forEach(item => {
        if (this.hasOwnProperty(item.key)) {
          this[item.key] = item.value;
        }
      });
    } catch (e) {
      console.error('Error fetching site config:', e);
    } finally {
      this.loading = false;
    }
  },
  
  async update(key, value) {
    try {
      const token = localStorage.getItem('admin_token');
      await axios.post(`${API_URL}/config`, { key, value }, {
        headers: { Authorization: `Bearer ${token}` }
      });
      this[key] = value;
    } catch (e) {
      console.error('Error updating config:', e);
    }
  }
});
