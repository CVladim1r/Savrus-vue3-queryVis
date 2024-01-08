<template>
    <div class="card">
      <canvas ref="pieChart"></canvas>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { Chart, registerables } from 'chart.js';
  Chart.register(...registerables);
  
  const props = defineProps<{
    data: { labels: string[]; datasets: { data: number[]; backgroundColor: string[]; }[] };
  }>();
  
  const pieChart = ref<HTMLCanvasElement | null>(null);
  
  onMounted(() => {
    if (pieChart.value) {
      new Chart(pieChart.value, {
        type: 'pie',
        data: props.data,
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top',
            },
          },
        },
      });
    }
  });
  </script>
  
  <style scoped>
  canvas {
    width: 100% !important;
    height: auto !important;
  }

  .card {
    border-radius: 8px;
    min-width: 300px;
    height: 300px;
}
  </style>
  