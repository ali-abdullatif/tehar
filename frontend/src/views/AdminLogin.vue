<template>
  <div class="login-page">
    <!-- Decorative background elements -->
    <div class="bg-orb orb-1"></div>
    <div class="bg-orb orb-2"></div>

    <div class="login-card glass-morphism">
      <!-- Logo / Branding -->
      <div class="login-header">
        <img src="@/assets/logo.png" alt="Logo" class="login-logo" />
        <h1 class="gold-gradient">لوحة التحكم</h1>
        <p class="subtitle">تسجيل دخول المشرف</p>
      </div>

      <!-- Error Alert -->
      <transition name="fade">
        <div v-if="error" class="error-alert">
          <span>⚠</span> {{ error }}
        </div>
      </transition>

      <!-- Login Form -->
      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group">
          <label for="username">اسم المستخدم</label>
          <div class="input-wrapper">
            <span class="input-icon">👤</span>
            <input
              id="username"
              v-model="username"
              type="text"
              placeholder="أدخل اسم المستخدم"
              required
              :disabled="loading"
              autocomplete="username"
            />
          </div>
        </div>

        <div class="form-group">
          <label for="password">كلمة المرور</label>
          <div class="input-wrapper">
            <span class="input-icon">🔒</span>
            <input
              id="password"
              v-model="password"
              :type="showPassword ? 'text' : 'password'"
              placeholder="أدخل كلمة المرور"
              required
              :disabled="loading"
              autocomplete="current-password"
            />
            <button
              type="button"
              class="toggle-password"
              @click="showPassword = !showPassword"
            >{{ showPassword ? '🙈' : '👁' }}</button>
          </div>
        </div>

        <button type="submit" class="login-btn" :disabled="loading">
          <span v-if="loading" class="spinner"></span>
          <span v-else>دخول</span>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

const API_URL = 'http://192.168.43.239:8000';
const router = useRouter();

const username = ref('');
const password = ref('');
const loading = ref(false);
const error = ref('');
const showPassword = ref(false);

const handleLogin = async () => {
  loading.value = true;
  error.value = '';

  // FastAPI's OAuth2 login expects form-encoded data
  const formData = new URLSearchParams();
  formData.append('username', username.value);
  formData.append('password', password.value);

  try {
    const response = await axios.post(`${API_URL}/auth/login`, formData, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });
    localStorage.setItem('admin_token', response.data.access_token);
    router.push('/admin');
  } catch (err) {
    error.value = err.response?.data?.detail || 'خطأ في بيانات الدخول. حاول مجدداً.';
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--bg-deep);
  position: relative;
  overflow: hidden;
  padding: 2rem;
}

/* Decorative glowing orbs */
.bg-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.15;
  pointer-events: none;
}

.orb-1 {
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, #0c3e2a, transparent);
  top: -100px;
  right: -100px;
  animation: float 8s ease-in-out infinite;
}

.orb-2 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, #d4af37, transparent);
  bottom: -80px;
  left: -80px;
  animation: float 10s ease-in-out infinite reverse;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-30px) scale(1.05); }
}

/* Card */
.login-card {
  width: 100%;
  max-width: 440px;
  padding: 3rem 2.5rem;
  border-radius: 20px;
  position: relative;
  z-index: 1;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(212, 175, 55, 0.15);
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(20px);
  animation: slideUp 0.6s ease;
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Header */
.login-header {
  text-align: center;
  margin-bottom: 2.5rem;
}

.login-logo {
  height: 64px;
  width: auto;
  object-fit: contain;
  filter: brightness(0) invert(1);
  display: block;
  margin: 0 auto 1rem auto;
}

@keyframes pulse-gold {
  0%, 100% { text-shadow: 0 0 10px rgba(212, 175, 55, 0.4); }
  50% { text-shadow: 0 0 25px rgba(212, 175, 55, 0.8); }
}

h1 {
  font-size: 2rem;
  margin-bottom: 0.4rem;
}

.subtitle {
  color: var(--text-muted);
  font-size: 0.95rem;
}

/* Error */
.error-alert {
  background: rgba(206, 55, 55, 0.15);
  border: 1px solid rgba(206, 55, 55, 0.4);
  color: #ff8585;
  border-radius: 8px;
  padding: 0.8rem 1rem;
  margin-bottom: 1.5rem;
  font-size: 0.9rem;
  text-align: center;
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.3s; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

/* Form */
.login-form { display: flex; flex-direction: column; gap: 1.5rem; }

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: var(--text-muted);
  font-size: 0.9rem;
  font-weight: 500;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

.input-icon {
  position: absolute;
  right: 1rem;
  font-size: 1rem;
  pointer-events: none;
  z-index: 1;
}

.input-wrapper input {
  width: 100%;
  padding: 0.9rem 3rem 0.9rem 1rem;
  background: #ffffff;
  border: 1px solid #cccccc;
  border-radius: 10px;
  color: #000000;
  font-size: 1rem;
  transition: all 0.3s ease;
  direction: rtl;
  box-sizing: border-box;
}

.input-wrapper input::placeholder {
  color: #888888;
}

/* Override browser autofill white background */
.input-wrapper input:-webkit-autofill,
.input-wrapper input:-webkit-autofill:hover,
.input-wrapper input:-webkit-autofill:focus {
  -webkit-text-fill-color: #f0ebe0;
  -webkit-box-shadow: 0 0 0 1000px rgba(10, 30, 20, 0.9) inset;
  transition: background-color 5000s ease-in-out 0s;
}

.input-wrapper input:focus {
  outline: none;
  border-color: #d4af37;
  background: rgba(255, 255, 255, 0.09);
  box-shadow: 0 0 0 3px rgba(212, 175, 55, 0.1);
}

.input-wrapper input:disabled {
  opacity: 0.5;
}

.toggle-password {
  position: absolute;
  left: 1rem;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  padding: 0;
  line-height: 1;
}

/* Login Button */
.login-btn {
  width: 100%;
  padding: 1rem;
  background: linear-gradient(135deg, #0c3e2a 0%, #1a6645 100%);
  border: 1px solid rgba(212, 175, 55, 0.3);
  color: white;
  border-radius: 10px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 0.5rem;
  position: relative;
  overflow: hidden;
}

.login-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(12, 62, 42, 0.5);
  border-color: rgba(212, 175, 55, 0.6);
}

.login-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Spinner */
.spinner {
  display: inline-block;
  width: 20px;
  height: 20px;
  border: 2px solid rgba(255,255,255,0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
</style>
