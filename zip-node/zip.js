
const fs = require('fs');
const zlib = require('zlib');
const archiver = require('archiver');

const output = fs.createWriteStream('example.zip');
const archive = archiver('zip');

output.on('close', () => {
  console.log(archive.pointer() + ' total bytes');
  console.log(
    'archiver has been finalized and the output file descriptor has closed.'
  );
});

archive.on('warning', (err) => {
  if (err.code === 'ENOENT') {
    console.warn(err);
  } else {
    throw err;
  }
});

archive.on('error', (err) => {
  throw err;
});

archive.pipe(output);

archive.file('file1.txt', { name: 'file1.txt' });
archive.file('file2.txt', { name: 'file2.txt' });

archive.finalize();
