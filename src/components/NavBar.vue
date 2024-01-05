<template>
    <div class="sidebar">
      <div class="sidebar-item" @click="navigateTo('settings')">Настройки</div>
      <div class="sidebar-item" @click="navigateTo('home')">Главная страница</div>
      <div class="sidebar-item" @click="navigateTo('logs')">Логи</div>
    </div>
  </template>
  
  <script setup>
  const navigateTo = (route) => {
    // Реализуйте переход по маршрутам
    console.log('Переход на страницу:', route);
  }
  </script>
  
  <style scoped>
  .sidebar {
    width: 200px;
    background-color: #f2f2f2;
    padding: 20px;
  }
  
  .sidebar-item {
    cursor: pointer;
    padding: 10px 0;
  }
  
  .sidebar-item:hover {
    background-color: #ddd;
  }
  </style>
  