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
  flex: 1;
  width: 900px;
  background: #fff;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
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
