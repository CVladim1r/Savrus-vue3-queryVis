<template>
  <div class="app">
    <Sidebar />
    <div class="main-content">
      <div class="content">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import Sidebar from './components/Sidebar.vue';
</script>

<style scoped>
.app {
  display: flex;
  height: 100vh;
}

.main-content {
  flex: 1;
}

.content {
  color: #fff;
  flex-direction: column;
}

.sidebar {
  width: 200px;
  background-color: #3f51b5;
  color: white;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

@media (max-width: 768px) {
  .sidebar {
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    z-index: 1000;
  }
}
</style>
