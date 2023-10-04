// Spawn a python process from JS 

const { spawn } = require('child_process');

const pythonProcess_barcode = spawn('python', ['./src/logic/barcode/barcode_gen.py']);

pythonProcess_barcode.stdout.on('data', (data) => {
    console.log(data.toString());
});


const pythonProcess_qr = spawn('python', ['./src/logic/qr/qr_gen.py']);

pythonProcess_qr.stdout.on('data', (data) => {
    console.log(data.toString());
});
