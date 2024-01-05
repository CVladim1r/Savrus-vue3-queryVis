<!-- src/views/Dashboard.vue -->
<template>
    <div class="dashboard">
        <div class="card">
            <h3>Bar Chart</h3>
            <BarChart />
        </div>
        <div class="card">
            <h3>Radar Chart</h3>
            <RadarChart />
        </div>
    </div>
</template>

<script setup lang="ts">
import BarChart from '../components/BarChart.vue';
import RadarChart from '../components/RadarChart.vue';
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
</style>
