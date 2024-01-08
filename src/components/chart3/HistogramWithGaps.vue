<template>
    <div class="card">
      <canvas ref="histogramChart"></canvas>
    </div>
</template>

<script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { Chart, registerables } from 'chart.js';
  Chart.register(...registerables);

  const props = defineProps<{
    data: { labels: string[]; datasets: { data: number[]; backgroundColor: string; }[] };
  }>();

  const histogramChart = ref<HTMLCanvasElement | null>(null);

  onMounted(() => {
    if (histogramChart.value) {
      new Chart(histogramChart.value, {
        type: 'bar',
        data: props.data,
        options: {
          responsive: true,
          scales: {
            x: {
              stacked: true,
            },
            y: {
              stacked: false,
            },
          },
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
  