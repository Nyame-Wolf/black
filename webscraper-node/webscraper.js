const axios = require('axios');
const cheerio = require('cheerio');

const url = 'https://example.com';

axios
  .get(url)
  .then((response) => {
    const html = response.data;
    const $ = cheerio.load(html);
    const title = $('title').text();
    console.log(title);
  })
  .catch((error) => {
    console.log(error);
  });
