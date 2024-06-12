<template>
    <div class="card">
        <Radar :data="chartData" :options="chartOptions" />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Radar } from 'vue-chartjs';
import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    RadialLinearScale,
    PointElement,
    LineElement,
    Filler,
} from 'chart.js';
import { fetchRadarData } from '../../api/api';

ChartJS.register(Title, Tooltip, Legend, RadialLinearScale, PointElement, LineElement, Filler);

interface RadarDataItem {
    argument: string;
    number: number;
    cnt: number;
}

const chartData = ref({
    labels: [] as string[],
    datasets: [
        {
            label: 'Radar Dataset',
            backgroundColor: 'rgba(179,181,198,0.2)',
            borderColor: 'rgba(179,181,198,1)',
            pointBackgroundColor: 'rgba(179,181,198,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(179,181,198,1)',
            data: [] as number[],
        },
    ],
});

const chartOptions = ref({
    responsive: true,
    maintainAspectRatio: false,
});

const loadRadarData = async () => {
    try {
        const data: RadarDataItem[] = await fetchRadarData();
        chartData.value.labels = data.map(item => item.argument);
        chartData.value.datasets[0].data = data.map(item => item.cnt);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

onMounted(() => {
    loadRadarData();
});
</script>

<style scoped>
.card {
    border-radius: 8px;
    min-width: 300px;
    height: 300px;
}
</style>
