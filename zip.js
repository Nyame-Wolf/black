/*
1.) initializa npm
 $ npm init 
- follow the prompts
2.)install archiver. Note that fs and zlib belong 
to node so already installed. 
    $ npm install archiver
3.) Run the code in terminal
     $ node zip.js
NOTE: provide path to the files. alternitively 
create two files file1.txt and file2.txt in the 
same directory
*/
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

archive.file('/path/to/myfiles/file1.txt', { name: 'file1.txt' });
archive.file('/path/to/myfiles/file2.txt', { name: 'file2.txt' });

archive.finalize();
