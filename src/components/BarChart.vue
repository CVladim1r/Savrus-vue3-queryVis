<!-- src/components/BarChart.vue -->
<template>
    <div>
        <Bar :data="chartData" :options="chartOptions" />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Bar } from 'vue-chartjs';
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
} from 'chart.js';
import { fetchData } from '../api/api';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

interface DataItem {
    label: string;
    value: number;
}

const chartData = ref({
    labels: [] as string[],
    datasets: [
        {
            label: 'Dataset',
            backgroundColor: '#f87979',
            data: [] as number[],
        },
    ],
});

const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: false,
});

const loadChartData = async () => {
    try {
        const data: DataItem[] = await fetchData();
        chartData.value.labels = data.map(item => item.label);
        chartData.value.datasets[0].data = data.map(item => item.value);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

onMounted(() => {
    loadChartData();
});
</script>

<style scoped>
.card {
    background: #fff;
    padding: 16px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>
