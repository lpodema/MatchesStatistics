import React, { useEffect, useState } from "react";
import Paper from "@mui/material/Paper";
import Typography from "@mui/material/Typography";
import Grid from "@mui/material/Grid";
import PropTypes from "prop-types";
import ReportTableUI from "./ReportTableUI";
import ErrorBoundary from "../handling/ErrorBoundary";
import generateFormattedTimeStamp from "../../utils/helpers";
import ButtonGenerateCSV from "../ButtonGenerateCSV";

function ReportTableWrapper({ loading, data, columns }) {
  const [timestamp, setTimestamp] = useState(undefined);

  useEffect(() => {
    setTimestamp(generateFormattedTimeStamp());
  }, [data]);

  return (
    <div style={{ height: "100%", width: "100%" }}>
      {!loading && data && (
        <ErrorBoundary>
          <Paper sx={{ width: "100%", mb: 5 }}>
            <ReportTableUI players={data} columns={columns} />
            <Grid
              container
              spacing={2}
              justifyContent="center"
              alignItems="center"
              style={{ padding: "2rem" }}
            >
              <Grid item xs={9}>
                <Typography variant="p" align="left">
                  Report generated on {timestamp}
                </Typography>
              </Grid>
              <Grid item xs={3}>
                <ButtonGenerateCSV rawData={data} name="data" />
              </Grid>
            </Grid>
          </Paper>
        </ErrorBoundary>
      )}
    </div>
  );
}

ReportTableWrapper.propTypes = {
  loading: PropTypes.bool.isRequired,
  data: PropTypes.instanceOf(Array).isRequired,
  columns: PropTypes.instanceOf(Array).isRequired,
};

export default ReportTableWrapper;
