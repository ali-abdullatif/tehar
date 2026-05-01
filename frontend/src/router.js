import { createRouter, createWebHistory } from 'vue-router'
import AdminDashboard from './views/AdminDashboard.vue'
import AdminLogin from './views/AdminLogin.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('./views/Home.vue')
  },
  {
    path: '/product/:id',
    name: 'ProductDetail',
    component: () => import('./views/ProductDetail.vue')
  },
  {
    path: '/admin/login',
    name: 'AdminLogin',
    component: AdminLogin,
    // If already logged in, redirect straight to dashboard
    beforeEnter: (to, from, next) => {
      if (localStorage.getItem('admin_token')) {
        next('/admin')
      } else {
        next()
      }
    }
  },
  {
    path: '/admin',
    name: 'Admin',
    component: AdminDashboard,
    // Navigation guard: require a token
    meta: { requiresAuth: true }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    }
    return { top: 0 };
  }
})

// Global guard for all routes with requiresAuth
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !localStorage.getItem('admin_token')) {
    next('/admin/login')
  } else {
    next()
  }
})

export default router
