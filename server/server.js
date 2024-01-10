// const express = require('express');
// const multer = require('multer');
// const path = require('path');

// const app = express();
// const port = 3000;

// // Sử dụng Multer để xử lý tệp tin được tải lên
// const storage = multer.diskStorage({
//   destination: (req, file, cb) => {
//     cb(null, 'uploads/');
//   },
//   filename: (req, file, cb) => {
//     cb(null, file.originalname);
//   },
// });

// const upload = multer({ storage });

// // Đường dẫn gốc để serve các file tải lên
// app.use(express.static('uploads'));

// app.post('/upload', upload.single('video'), (req, res) => {
//   res.send('Tệp tin đã được tải lên thành công!');
// });

// app.listen(port, () => {
//   console.log(`Server is running at http://localhost:${port}`);
// });

const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();
const port = 3000;

// Sử dụng Multer để xử lý tệp tin được tải lên
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, path.join(__dirname, '../uploads/')); // Sửa đường dẫn này để đặt thư mục uploads ngang hàng với server
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname);
        
        // Truyền dữ liệu filename qua query parameter
        const filename = encodeURIComponent(file.originalname);
        const url = `http://localhost:3000/run_script?filename=${filename}`;
        // Gọi API hoặc thực hiện các xử lý khác tại đây để thông báo file main.py
        console.log(file.originalname);
    },
});


const upload = multer({ storage });

// Đường dẫn gốc để serve các file tải lên
app.use(express.static(path.join(__dirname, '../uploads/')));

app.post('/upload', upload.single('video'), (req, res) => {
    res.send('Tệp tin đã được tải lên thành công!');
});

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
