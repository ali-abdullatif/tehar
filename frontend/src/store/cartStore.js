import { reactive, watch } from 'vue';
import { trackEvent } from './tracking';

// Load initial state from local storage
const savedCart = localStorage.getItem('jewelry_cart');
const initialState = savedCart ? JSON.parse(savedCart) : [];

export const cartState = reactive({
  items: initialState,
  isOpen: false,
  
  // Actions
  addItem(product) {
    const existing = this.items.find(i => i.id === product.id);
    if (existing) {
      existing.quantity++;
    } else {
      this.items.push({ ...product, quantity: 1 });
    }
    
    // Tracking ADD_TO_CART
    trackEvent('add_to_cart', product.id, 1);
    
    this.isOpen = true; // Open cart when item is added
  },

  checkoutTrack() {
    this.items.forEach(item => {
      trackEvent('purchase', item.id, item.quantity);
    });
  },
  
  removeItem(id) {
    const index = this.items.findIndex(i => i.id === id);
    if (index !== -1) this.items.splice(index, 1);
  },
  
  updateQuantity(id, delta) {
    const item = this.items.find(i => i.id === id);
    if (item) {
      item.quantity += delta;
      if (item.quantity <= 0) this.removeItem(id);
    }
  },
  
  clearCart() {
    this.items = [];
  },
  
  toggleCart() {
    this.isOpen = !this.isOpen;
  }
});

// Percent-calc getter
export const cartTotal = () => {
  return cartState.items.reduce((total, item) => total + (item.price * item.quantity), 0);
};

export const cartCount = () => {
  return cartState.items.reduce((total, item) => total + item.quantity, 0);
};

// Auto-save to LocalStorage
watch(() => cartState.items, (newItems) => {
  localStorage.setItem('jewelry_cart', JSON.stringify(newItems));
}, { deep: true });
