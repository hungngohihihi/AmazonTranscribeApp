const express = require('express');
const multer = require('multer');
const path = require('path');

const app = express();
const fs = require('fs');
const filenameTxtPath = path.join(__dirname, '../texts/filename.txt');
const port = 3000;

// Sử dụng Multer để xử lý tệp tin được tải lên
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, path.join(__dirname, '../uploads/')); // Sửa đường dẫn này để đặt thư mục uploads ngang hàng với server
    },
    filename: (req, file, cb) => {
        cb(null, file.originalname);
        filenameupload = file.originalname;
        // Ghi dữ liệu vào file filename.txt
        // Xoá file nếu tồn tại
        fs.unlink(filenameTxtPath, (err) => {
            if (err && err.code !== 'ENOENT') {
                console.error(err);
            } else {
                // console.log('File deleted:', filenameTxtPath);

                // Tạo mới file và ghi dữ liệu
                fs.writeFile(filenameTxtPath, filenameupload, (err) => {
                    if (err) {
                        console.error(err);
                    } else {
                        // console.log('Data written to filename.txt');
                    }
                });
            }
        });
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
