<!-- src/views/Dashboard.vue -->
<template>
    <h1>Графики и таблица</h1>
    <div class="dashboard">
        <div class="card">
            <h3>Bar Chart</h3>
            <BarChart />
        </div>
        <div class="card">
            <h3>Radar Chart</h3>
            <RadarChart />
        </div>
        <div class="card">
            <h3>Table</h3>
            <DataTable :items="data" :headers="headers" />
        </div>
    </div>
</template>

<script setup lang="ts">
import BarChart from '../components/BarChart.vue';
import RadarChart from '../components/RadarChart.vue';
import DataTable from '../components/DataTable.vue';
import { fetchData, DataItem } from '../api/api';
import { ref, onMounted } from 'vue';

let data = ref<DataItem[]>([]);
const headers = ref<string[]>([]);

onMounted(async () => {
  try {
    data.value = await fetchData();
    headers.value = Object.keys(data.value[0]);
  } catch (error) {
    console.error('Error fetching data:', error);
  }
});
</script>

<style scoped>
.dashboard {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    padding: 16px;
}
.card {
    flex: 1;
    min-width: 300px;
    max-width: 600px;
    background: #fff;
    padding: 16px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
h3{
    color: rgb(63, 65, 78);
    font-size: large;
    font-weight: 500;
}
</style>
