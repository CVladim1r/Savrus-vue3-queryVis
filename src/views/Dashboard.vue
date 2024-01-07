<template>
    <h1>Графики и таблица</h1>
    <div class="dashboard">
        <div class="dashboard-card">
            <div class="caerd">
                <h3>Bar Chart</h3>
                <BarChart />
            </div>
            <div class="caerd">
                <h3>Radar Chart</h3>
                <RadarChart />
            </div>
        </div>

    
        <div class="card-table">
            <h3>Table</h3>
            <DataTable :items="testData" :headers="headers" />
        </div>
    </div>
</template>

<script setup lang="ts">
import BarChart from '../components/BarChart.vue';
import RadarChart from '../components/RadarChart.vue';
import DataTable from '../components/DataTable.vue';
import { fetchData, DataItem } from '../api/api';
import { ref, onMounted } from 'vue';

// Test data for the table
const testData: DataItem[] = [
  {
    SvrSeid: 13,
    SvrSrt: 1001,
    seid: 1,
    SRT: 1001,
    type: 'Error',
    name: 'Product A',
    deviceAddress: '192.168.0.1',
    deviceHostName: 'server1',
    severity: 'High',
    destinationAddress: '192.168.0.2',
    destinationUserName: 'admin',
    sourceAddress: '192.168.0.3',
    sourceUserName: 'system',
    deviceVendor: 'Vendor A',
    deviceProduct: 'Product X',
    agentAddress: '192.168.0.4'
  },
  {
    SvrSeid: 36,
    SvrSrt: 2671,
    seid: 54,
    SRT: 13853,
    type: 'Warning',
    name: 'Product B',
    deviceAddress: '192.168.0.5',
    deviceHostName: 'server2',
    severity: 'Medium',
    destinationAddress: '192.168.0.6',
    destinationUserName: 'user',
    sourceAddress: '192.168.0.7',
    sourceUserName: 'system',
    deviceVendor: 'Vendor B',
    deviceProduct: 'Product Y',
    agentAddress: '192.168.0.4'
  },
  {
    SvrSeid: 1734,
    SvrSrt: 1001,
    seid: 1,
    SRT: 1001,
    type: 'Error',
    name: 'Product A',
    deviceAddress: '192.168.0.1',
    deviceHostName: 'server1',
    severity: 'High',
    destinationAddress: '192.168.0.2',
    destinationUserName: 'root',
    sourceAddress: '192.168.0.3',
    sourceUserName: 'system',
    deviceVendor: 'Vendor A',
    deviceProduct: 'Product X',
    agentAddress: '192.168.0.13'
  },
  {
    SvrSeid: 464,
    SvrSrt: 147,
    seid: 5,
    SRT: 105321,
    type: 'Warning',
    name: 'Product B',
    deviceAddress: '192.168.0.5',
    deviceHostName: 'server2',
    severity: 'Medium',
    destinationAddress: '192.168.0.6',
    destinationUserName: 'user',
    sourceAddress: '192.168.0.7',
    sourceUserName: 'system',
    deviceVendor: 'Vendor B',
    deviceProduct: 'Product Y',
    agentAddress: '192.168.0.8'
  },
  {
    SvrSeid: 6,
    SvrSrt: 1005,
    seid: 1,
    SRT: 1001,
    type: 'Error',
    name: 'Product A',
    deviceAddress: '192.168.0.1',
    deviceHostName: 'server1',
    severity: 'High',
    destinationAddress: '192.168.0.2',
    destinationUserName: 'admin',
    sourceAddress: '192.168.0.4',
    sourceUserName: 'system',
    deviceVendor: 'Vendor A',
    deviceProduct: 'Product XXX',
    agentAddress: '192.168.0.4'
  },
  {
    SvrSeid: 49,
    SvrSrt: 1036,
    seid: 2,
    SRT: 3467,
    type: 'Warning',
    name: 'Product G',
    deviceAddress: '192.168.0.25',
    deviceHostName: 'server2',
    severity: 'Medium',
    destinationAddress: '192.168.0.56',
    destinationUserName: 'user',
    sourceAddress: '192.168.0.27',
    sourceUserName: 'system',
    deviceVendor: 'Vendor CB',
    deviceProduct: 'Product X',
    agentAddress: '192.168.0.1'
  },
];

const tableHeaders: string[] = Object.keys(testData[0]);

let data = ref<DataItem[]>(testData);
const headers = ref<string[]>(tableHeaders);

// The fetchData() function is no longer used since we're using test data
// onMounted(async () => {
//   try {
//     data.value = await fetchData();
//     headers.value = Object.keys(data.value[0]);
//   } catch (error) {
//     console.error('Error fetching data:', error);
//   }
// });
</script>


<style scoped>
.dashboard {
    padding: 24px;
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    flex-direction: column;
    justify-content: center;
}
.dashboard-card{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 16px;
}
.card {
    flex: 1;
    min-width: 300px;
    max-width: 300px;
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
