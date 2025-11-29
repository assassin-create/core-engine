const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
  }

  parse() {
    const fileBuffer = fs.readFileSync(this.filePath);
    const fileContent = fileBuffer.toString('utf8');

    const lines = fileContent.split('\n');
    const parsedData = {};

    lines.forEach((line) => {
      const trimmedLine = line.trim();
      if (trimmedLine &&!trimmedLine.startsWith('#')) {
        const [key, value] = trimmedLine.split('=');
        parsedData[key.trim()] = value.trim();
      }
    });

    return parsedData;
  }
}

module.exports = Parser;