import React from "react";
import PropTypes from "prop-types";
import { DataGrid } from "@mui/x-data-grid";
import ErrorBoundary from "../handling/ErrorBoundary";

function ReportTableUI(props) {
  const { players, columns } = props;

  return (
    <ErrorBoundary>
      <DataGrid
        rows={players}
        columns={columns}
        getRowId={(row) => row.UUID}
        hideFooter
      />
    </ErrorBoundary>
  );
}

ReportTableUI.propTypes = {
  players: PropTypes.instanceOf(Array).isRequired,
  columns: PropTypes.instanceOf(Array).isRequired,
};

export default ReportTableUI;
