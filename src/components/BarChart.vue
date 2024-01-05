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
  
  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:3000/api/data');
      const data: DataItem[] = await response.json();
      chartData.value.labels = data.map((item: DataItem) => item.label);
      chartData.value.datasets[0].data = data.map((item: DataItem) => item.value);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  
  onMounted(() => {
    fetchData();
  });
  </script>
  
  <style>
  /* Добавь свои стили здесь */
  </style>
  