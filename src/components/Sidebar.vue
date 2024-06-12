<template>
  <div class="sidebar">
    <ul>
      <li :class="{ active: $route.path === '/' }">
        <router-link to="/">
          <i class="fas fa-home"></i> Dashboard
        </router-link>
      </li>
      <li :class="{ active: $route.path === '/settings' }">
        <router-link to="/settings">
          <i class="fas fa-list"></i> Settings
        </router-link>
      </li>
      <li :class="{ active: $route.path === '/logs' }">
        <router-link to="/logs">
          <i class="fas fa-list"></i> Logs
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>
.sidebar {
  width: 200px;
  background-color: #3f51b5;
  color: white;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
}

.sidebar li {
  margin: 10px 0;
}

.sidebar a {
  text-decoration: none;
  color: white;
  display: flex;
  align-items: center;
  padding: 10px;
  border-radius: 4px;
  transition: background 0.3s;
}

.sidebar a:hover {
  background-color: #2c387e;
}

.sidebar i {
  margin-right: 10px;
}

.active {
  background-color: #2c387e;
}
</style>
