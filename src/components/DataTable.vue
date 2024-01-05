<template>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th v-for="header in headers" :key="header">{{ header }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items" :key="item.SvrSeid">
            <td>{{ item.SvrSeid }}</td>
            <td>{{ item.SvrSrt }}</td>
            <td>{{ item.seid }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, defineProps } from 'vue';
  
  interface DataItem {
    SvrSeid: number;
    SvrSrt: number;
    seid: number;
  }
  
  const props = defineProps<{
    items: DataItem[];
    headers: string[];
  }>();
  
  </script>
  
  <style scoped>
  .table-container {
    overflow-x: auto;
  }
  table {
    color: rgb(47, 32, 71);
    width: 100%;
    border-collapse: collapse;
  }
  th, td {
    padding: 8px;
    border: 1px solid #313131;
    text-align: left;
  }
  th {
    background-color: #292929;
  }
  </style>
  