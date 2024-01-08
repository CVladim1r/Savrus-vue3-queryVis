<template>
    <div class="ag-theme-alpine" style="height: 500px; width: 100%;">
      <ag-grid-vue
        class="ag-theme-alpine table-view"
        :columnDefs="columnDefs"
        :rowData="items"
        :defaultColDef="defaultColDef"
        :localeText="localeText"
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
    SvrSeid: number;
    SvrSrt: number;
    seid: number;
    SRT: number;
    type: string;
    name: string;
    deviceAddress: string;
    deviceHostName: string;
    severity: string;
    destinationAddress: string;
    destinationUserName: string;
    sourceAddress: string;
    sourceUserName: string;
    deviceVendor: string;
    deviceProduct: string;
    agentAddress: string;
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
  
  

  const localeText = ref({
  // Переводы заголовков и текстов
  page: "Страница",
  more: "ещё",
  to: "к",
  of: "из",
  next: "Следующая",
  last: "Последняя",
  first: "Первая",
  previous: "Предыдущая",
  loadingOoo: "Загрузка...",
  selectAll: "Выбрать все",
  searchOoo: "Поиск...",
  blanks: "Пусто",
  filterOoo: "Фильтр...",
  applyFilter: "Применить фильтр",
  equals: "Равно",
  notEqual: "Не равно",
  contains: "Содержит",
  notContains: "Не содержит",
  startsWith: "Начинается с",
  endsWith: "Заканчивается на",
  andCondition: "И",
  orCondition: "ИЛИ",
  group: "Группа",
  columns: "Колонки",
  filters: "Фильтры",
  pivotMode: "Режим сводной таблицы",
  groups: "Группы",
  values: "Значения",
  pivots: "Сводки",
  export: "Экспорт",
  csvExport: "Экспорт в CSV",
  excelExport: "Экспорт в Excel",
  pinColumn: "Закрепить колонку",
  autosizeThiscolumn: "Авторазмер этой колонки",
  autosizeAllColumns: "Авторазмер всех колонок",
  groupBy: "Группировать по",
  ungroupBy: "Разгруппировать по",
  resetColumns: "Сбросить колонки",
  expandAll: "Развернуть все",
  collapseAll: "Свернуть все",
  toolPanel: "Панель инструментов",
  noRowsToShow: "Нет данных для отображения",
  enabled: "Включено",
  pinLeft: "Закрепить слева",
  pinRight: "Закрепить справа",
  noPin: "Не закреплять",
  sum: "Сумма",
  min: "Минимум",
  max: "Максимум",
  none: "Нет",
  count: "Количество",
  average: "Среднее",
  copy: "Копировать",
  copyWithHeaders: "Копировать с заголовками",
  ctrlC: "Ctrl+C",
  paste: "Вставить",
  ctrlV: "Ctrl+V",
  rowGroupColumnsEmptyMessage: "Перетащите сюда для группировки",
  valueColumnsEmptyMessage: "Перетащите сюда для агрегации",
  pivotColumnsEmptyMessage: "Перетащите сюда для пивотирования",
  pinColumnLeft: "Закрепить колонку слева",
  pinColumnRight: "Закрепить колонку справа",
  noPinColumn: "Не закреплять колонку",
  avg: "Среднее",
});
  

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
  .ag-theme-alpine {
    height: 400px;
    min-width: 300px;
    width: auto;
    color: black;
  }
  .table-view {
    border-radius: 8px;
  }
</style>
  