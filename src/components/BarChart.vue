<template>
    <div class="card">
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
import { fetchBarChartData } from '../api/api';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

interface BarChartDataItem {
    destinationUserName: string;
    sum: number;
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
        const data: BarChartDataItem[] = await fetchBarChartData();
        chartData.value.labels = data.map(item => item.destinationUserName);
        chartData.value.datasets[0].data = data.map(item => item.sum);
    } catch (error) {
        console.error('Error fetching bar chart data:', error);
    }
};

onMounted(() => {
    loadChartData();
});
</script>

<style scoped>
.card {
    border-radius: 8px;
    min-width: 300px;
    height: 300px;
}
</style>
