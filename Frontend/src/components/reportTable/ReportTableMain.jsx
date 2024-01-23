import React from "react";
import ReportTableWrapper from "./ReportTableWrapper";
import ServiceLayerWrapper from "../serviceLayer/ServiceWrapper";
import Loading from "../handling/LoadingWrapper";
import {
  ENDPOINT_REPORT,
  QUERY_PARAM_FORMAT_JSON,
  Columns,
} from "../../utils/consts";

function ReportTableMain() {
  return (
    <Loading>
      <ServiceLayerWrapper
        endpoint={ENDPOINT_REPORT}
        format={QUERY_PARAM_FORMAT_JSON}
      >
        <ReportTableWrapper columns={Columns} />
      </ServiceLayerWrapper>
    </Loading>
  );
}

export default ReportTableMain;
