<template>
  <transition name="drawer">
    <div v-if="cartState.isOpen" class="cart-overlay" @click.self="cartState.toggleCart">
      <div class="cart-drawer">
        <div class="cart-header">
          <button @click="cartState.toggleCart" class="close-btn">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <div class="header-title">
            <svg xmlns="http://www.w3.org/2000/svg" class="icon-gold" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z" />
            </svg>
            <h3>حقيبة التسوق</h3>
          </div>
        </div>

        <div v-if="cartState.items.length === 0" class="empty-cart">
          <div class="empty-icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" fill="none" viewBox="0 0 24 24" stroke="#d4af37">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
            </svg>
          </div>
          <p>حقيبة التسوق فارغة حالياً</p>
          <button @click="cartState.toggleCart" class="gold-btn">استعرض المجموعة</button>
        </div>

        <div v-else class="cart-body">
          <div class="cart-items">
            <div v-for="item in cartState.items" :key="item.id" class="cart-item">
              <div class="item-img" :style="item.image_url ? `background-image: url(${item.image_url})` : ''"></div>
              <div class="item-details">
                <h4>{{ item.name }}</h4>
                <p class="item-price">{{ (item.price * item.quantity).toLocaleString('ar-SA') }} ر.ي</p>
                <div class="qty-control">
                  <button @click="cartState.updateQuantity(item.id, -1)">-</button>
                  <span>{{ item.quantity }}</span>
                  <button @click="cartState.updateQuantity(item.id, 1)">+</button>
                </div>
              </div>
              <button @click="cartState.removeItem(item.id)" class="remove-btn">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
              </button>
            </div>
          </div>

          <div class="cart-footer">
            <div class="total-row">
              <span>الإجمالي:</span>
              <span class="total-price">{{ totalAmount.toLocaleString('ar-SA') }} ر.ي</span>
            </div>
            <button @click="checkoutWhatsApp" class="checkout-btn">
              <span>طلب عبر واتساب</span>
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" viewBox="0 0 24 24">
                <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.417-.003 6.557-5.338 11.892-11.893 11.892-1.997-.001-3.951-.5-5.688-1.448l-6.305 1.652zm6.599-3.835c1.544.917 3.41 1.401 5.316 1.402h.005c5.385 0 9.767-4.382 9.77-9.77.002-2.611-1.015-5.065-2.863-6.915-1.847-1.85-4.305-2.868-6.917-2.869-5.386 0-9.768 4.382-9.77 9.77-.001 2.1.548 4.146 1.591 5.922l-1.013 3.702 3.791-.993zm11.368-7.73c-.301-.151-1.78-.878-2.056-.979-.276-.1-.477-.151-.677.151-.2.3-.775 1.003-.951 1.254-.176.251-.352.281-.653.131-2.014-.941-2.584-1.439-3.551-3.135-.251-.439.251-.408.72-.84.238-.218.3-.399.3-.599s-.1-.376-.2-.476c-.099-.1-.477-1.155-.653-1.581-.171-.413-.344-.356-.477-.363-.121-.006-.259-.007-.399-.007-.14 0-.369.053-.562.261-.193.208-.737.72-.737 1.758s.757 2.056.862 2.197c.105.14 1.488 2.274 3.606 3.187.502.217.896.347 1.2.443.504.16 1.159.137 1.597.072.489-.072 1.481-.603 1.691-1.185.209-.583.209-1.084.146-1.185-.064-.101-.237-.151-.539-.302z"/>
              </svg>
            </button>
            <p class="footer-hint">سيتم تحويلك لمحادثة واتساب لإتمام الطلب</p>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { computed } from 'vue';
import { cartState, cartTotal } from '@/store/cartStore';
import { siteConfig } from '@/store/siteStore';

const totalAmount = computed(() => cartTotal());

const checkoutWhatsApp = () => {
  // Tracking PURCHASE
  cartState.checkoutTrack();

  const phone = siteConfig.footer_phone.replace(/\+/g, '').replace(/\s/g, ''); 
  let message = "*طلب جديد من متجر مجوهرات الملوك*\n\n";
  
  cartState.items.forEach(item => {
    message += `• ${item.name} (الكمية: ${item.quantity}) - ${item.price * item.quantity} ر.ي\n`;
  });
  
  message += `\n*الإجمالي: ${totalAmount.value} ر.ي*`;
  
  const encoded = encodeURIComponent(message);
  window.open(`https://wa.me/${phone}?text=${encoded}`, '_blank');
};
</script>

<style scoped>
.cart-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(4px);
  z-index: 2000;
  display: flex;
  justify-content: flex-start; /* Left side for Arabic RTL */
}

.cart-drawer {
  width: 100%;
  max-width: 420px;
  background: var(--bg-primary);
  height: 100%;
  display: flex;
  flex-direction: column;
  box-shadow: 20px 0 50px rgba(0,0,0,0.3);
  border-right: 1px solid rgba(212, 175, 55, 0.2);
}

.cart-header {
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

.header-title {
  display: flex;
  align-items: center;
  gap: 0.8rem;
}

.icon-gold {
  color: var(--gold-primary);
}

.cart-header h3 {
  margin: 0;
  font-family: var(--font-calligraphy);
  font-size: 1.4rem;
  color: var(--emerald-deep);
}

.close-btn {
  background: none;
  border: none;
  cursor: pointer;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  padding: 0.5rem;
  transition: color 0.3s;
}

.close-btn:hover {
  color: var(--gold-primary);
}

.cart-body {
  flex: 1;
  overflow-y: auto;
  padding: 1.5rem;
}

.cart-items {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.cart-item {
  display: flex;
  gap: 1rem;
  align-items: center;
  padding-bottom: 1.5rem;
  border-bottom: 1px solid rgba(0,0,0,0.03);
}

.item-img {
  width: 80px;
  height: 80px;
  background-size: cover;
  background-position: center;
  background-color: #f9f9f9;
  border-radius: 8px;
  flex-shrink: 0;
}

.item-details {
  flex: 1;
}

.item-details h4 {
  margin: 0 0 0.5rem;
  font-size: 1rem;
}

.item-price {
  color: var(--emerald-deep);
  font-weight: 600;
  margin: 0 0 0.8rem;
}

.qty-control {
  display: flex;
  align-items: center;
  gap: 1rem;
  background: #f5f5f5;
  width: fit-content;
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
}

.qty-control button {
  background: none;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  color: var(--emerald-deep);
}

.remove-btn {
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2rem;
  opacity: 0.3;
  transition: opacity 0.3s;
}

.remove-btn:hover { opacity: 1; }

.empty-cart {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 1.5rem;
  padding: 2rem;
}

.empty-icon { font-size: 4rem; }

.cart-footer {
  padding: 2rem;
  background: white;
  border-top: 1px solid rgba(0,0,0,0.05);
  box-shadow: 0 -10px 20px rgba(0,0,0,0.02);
}

.total-row {
  display: flex;
  justify-content: space-between;
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
}

.total-price { color: var(--emerald-deep); }

.checkout-btn {
  width: 100%;
  background: #25D366; /* WhatsApp Green */
  color: white;
  border: none;
  padding: 1.2rem;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 700;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.8rem;
  transition: all 0.3s ease;
}

.checkout-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(37, 211, 102, 0.3);
}

.footer-hint {
  text-align: center;
  font-size: 0.8rem;
  color: var(--text-muted);
  margin-top: 1rem;
}

/* Transitions */
.drawer-enter-active, .drawer-leave-active { transition: opacity 0.4s; }
.drawer-enter-from, .drawer-leave-to { opacity: 0; }

.drawer-enter-active .cart-drawer { transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1); }
.drawer-leave-active .cart-drawer { transition: transform 0.3s ease-in; }

.drawer-enter-from .cart-drawer { transform: translateX(-100%); }
.drawer-leave-to .cart-drawer { transform: translateX(-100%); }
</style>
