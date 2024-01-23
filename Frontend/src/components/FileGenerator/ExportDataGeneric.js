class ExportDataGeneric {
  constructor() {
    this.parser = undefined;
    this.fileGenerator = undefined;
  }

  setParser(parser) {
    this.parser = parser;
  }

  setFileGenerator(fileGenerator) {
    this.fileGenerator = fileGenerator;
  }

  exportData(rawData, name, extension, encoding) {
    // FIXME add abstraction layer to allow for different parsers
    const data = this.parser.unparse(rawData);
    return this.fileGenerator(data, `${name}.${extension}`, `${encoding}`);
  }
}

export default ExportDataGeneric;
