const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

// Пример маршрута для получения данных
app.get('/api/data', (req, res) => {
  // Здесь будет логика для получения данных из базы данных
  const data = [
    { label: 'Category 1', value: 10 },
    { label: 'Category 2', value: 20 },
    { label: 'Category 3', value: 30 },
  ];
  res.json(data);
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
