<template>
  <div class="app">
      <Sidebar />
      <div class="content">
        <router-view />
      </div>
  </div>
</template>

<script setup lang="ts">
import Sidebar from './components/Sidebar.vue';
</script>

<style scoped>
.app {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vh;
}

.header {
  display: flex;
  align-items: center;
  background-color: #3f51b5;
  color: white;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logo {
  height: 40px;
  margin-right: 10px;
}

.title {
  font-size: 1.5em;
  margin: 0;
}

.main-content {
  display: flex;
  flex: 1;
  overflow: hidden;
}

.content {
  color: #fff;
  padding: 16px;
}

@media (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
  }

  .logo {
    margin-bottom: 10px;
  }

  .main-content {
    flex-direction: column;
  }

  .content {
    padding: 10px;
  }
}
</style>
