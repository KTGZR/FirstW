const express = require('express');
const routes = require('./routes/index.js');
const bodyParser = require('body-parser');
const {PythonShell} = require('python-shell');
const pool = require('./config/db.js');
const path = require('path');
const app = express();

const port = 8000;
const filePath = path.join(__dirname,'./Equipment/data.xlsx');
app.set('view engine','ejs');
app.use(express.static(__dirname + '/public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

routes(app);

pool.query('SELECT NOW()', (err, res) => {
  if(err) {
    console.error('Error connecting to the database', err.stack);
  } else {
    console.log('Connected to the database:', res.rows);
  }
});


app.get('/',(req,res)=>{
  res.render('index');
});

app.get('/download',(req,res)=>{

  // res.setHeader('Content-Disposition','attachment; filename=Holidays.xlsx');
  // res.setHeader('Content-Type','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
  const options = {
    scriptPath:'./scripts/'
  }
  PythonShell.run('CollectData.py',options).then(messages=>{
    console.log('Данные с базы собраны в файл')
  })
  res.sendFile(filePath)
});

app.post('/takeDate', (req, res) => {
  const startDate = req.body.start_date;
  const endDate = req.body.end_date;
  if(startDate===''|endDate===''){
    alert('Проверьте заполнение дат');
    return;
  }

  console.log(`Дата начала: ${startDate}, Дата конца: ${endDate}`);

  const options = {
    scriptPath:'./scripts',
    args: [startDate, endDate] 
  };

  PythonShell.run('FromDB.py', options).then(messages=>{
    console.log('Скрипт отработан.');
    res.redirect('/download');
  });
  });



app.listen(port, () => {

  console.log(`Сервер запущен на порту ${port}`);

});


app.post('/afterauth', async (req, res) => {
  try {
    const email = req.body.email;
    const password = req.body.pass;
    const query = 'SELECT * FROM public.users WHERE email like $1 AND password like $2'; 
    const result = await pool.query(query, [email, password]);
    if (result.rows.length > 0) {
      res.redirect('/success'); 
    } else {
      res.send('Неверные данные'); 
    }
  } catch (error) {
    console.error('Ошибка при запросе к базе данных:', error);
    res.status(500).send('Ошибка сервера');
  }
});


app.get('/success',(req,res)=>{
  res.render('afteraut');
});
  
  app.get('/data', (req, res) => {
    pool.query('select * from public.holidays', (err, result) => {
      if (err) {
        console.error('Ошибка при запросе к базе данных:', err);
        res.status(500).send('Ошибка сервера');
      } else {
        const rows = result.rows;
        if (rows.length()===0){
          res.send("Таблица пуста, данные не были загружены либо были удалены")
        } else {
        let htmlTable = `<table>
          <thead>
            <tr>`;
        for (const key in rows[0]) {
          htmlTable += `<th>${key}</th>`;
        }
        htmlTable += `</tr>
          </thead>
          <tbody>`;
  
        rows.forEach(row => {
          htmlTable += `<tr>`;
          for (const key in row) {
            htmlTable += `<td>${row[key]}</td>`;
          }
          htmlTable += `</tr>`;
        });
  
        htmlTable += `</tbody>
        </table>`;
  
        res.send(htmlTable);
      }
    }
    });
  });

