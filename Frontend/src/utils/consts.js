export const ENDPOINT_REPORT = "/players/report/";
export const QUERY_PARAM_FORMAT_JSON = "format=json";

export const Columns = [
  { field: "UUID", headerName: "UUID", type: "string", flex: 1 },
  { field: "nickname", headerName: "Nickname", type: "string", flex: 1 },
  { field: "score", headerName: "Score", type: "number", width: 60 },
  {
    field: "date_joined",
    headerName: "Date joined",
    type: "string",
    flex: 1,
  },
  {
    field: "last_played",
    headerName: "Last played",
    type: "string",
    flex: 1,
  },
];
