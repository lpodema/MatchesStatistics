import React from "react";
import PropTypes from "prop-types";

import Button from "@mui/material/Button";
import SaveAltIcon from "@mui/icons-material/SaveAlt";
import Papa from "papaparse";
import ExportDataGeneric from "./FileGenerator/ExportDataGeneric";
import CreateFile from "./FileGenerator/FileCreation";

function ButtonGenerateCSV({ rawData, name }) {
  const ExportDataCSV = new ExportDataGeneric();
  ExportDataCSV.setParser(Papa);
  ExportDataCSV.setFileGenerator(CreateFile);

  const handleOnClick = () => {
    console.log(rawData);
    ExportDataCSV.exportData(rawData, name, "csv", "text/csv;charset=utf-8;");
  };

  return (
    <Button
      onClick={handleOnClick}
      variant="contained"
      startIcon={<SaveAltIcon />}
    >
      Save Report to CSV
    </Button>
  );
}

ButtonGenerateCSV.propTypes = {
  rawData: PropTypes.instanceOf(Array).isRequired,
  name: PropTypes.string.isRequired,
};

export default ButtonGenerateCSV;
