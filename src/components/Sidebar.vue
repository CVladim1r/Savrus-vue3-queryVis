<template>
  <div class="sidebar">
    <ul>
      <li><router-link to="/">Dashboard</router-link></li>
      <li><router-link to="/logs">Logs</router-link></li>
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
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  overflow-y: auto;
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
  display: block;
  padding: 10px;
  border-radius: 4px;
  transition: background 0.3s;
}

.sidebar a:hover {
  background-color: #2c387e;
}

@media (max-width: 768px) {
  .sidebar {
    width: 100%;
    height: auto;
    position: relative;
  }

  .sidebar ul {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
  }

  .sidebar li {
    margin: 5px 0;
  }
}
</style>
