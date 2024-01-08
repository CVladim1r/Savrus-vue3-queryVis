<template>
    <div class="ag-theme-alpine" style="height: 500px; width: 100%;">
      <ag-grid-vue
        class="ag-theme-alpine table-view"
        :columnDefs="columnDefs"
        :rowData="items"
        :defaultColDef="defaultColDef"
        rowSelection="multiple"
        @grid-ready="onGridReady"
        :sideBar="sideBar"
      ></ag-grid-vue>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, defineProps } from 'vue';
  import { AgGridVue } from 'ag-grid-vue3';
  import 'ag-grid-community/styles/ag-grid.css';
  import 'ag-grid-community/styles/ag-theme-alpine.css';
  import type { GridReadyEvent } from 'ag-grid-community';
  
  interface DataItem {
    [key: string]: any;
  }
  
  const props = defineProps<{
    items: DataItem[];
    headers: string[];
  }>();
  
  const columnDefs = ref(props.headers.map(header => ({ headerName: header, field: header })));
  
  const defaultColDef = ref({
    sortable: true,
    filter: true,
    resizable: true,
    enableRowGroup: true,
    enablePivot: true,
    enableValue: true,
    suppressMovable: false,
  });
  
  const onGridReady = (params: GridReadyEvent) => {
    params.api.sizeColumnsToFit();
  };
  
  const sideBar = ref({
    toolPanels: [
      {
        id: 'columns',
        labelDefault: 'Columns',
        labelKey: 'columns',
        toolPanel: 'agColumnsToolPanel',
        toolPanelParams: {
          suppressRowGroups: false,
          suppressValues: false,
          suppressPivots: true,
          suppressPivotMode: true,
        },
      },
    ],
    defaultToolPanel: 'columns',
  });
  </script>
  
  <style scoped>
  .table-view {
    width: 100%;
    height: 100%;
  }
  </style>
  