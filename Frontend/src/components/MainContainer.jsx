import React from "react";
import Container from "@mui/material/Container";
import Header from "./Header";
import ReportTableMain from "./reportTable/ReportTableMain";

function MainContainer() {
  return (
    <Container maxWidth="lg" style={{ marginTop: "3rem" }}>
      <Header />
      <ReportTableMain />
    </Container>
  );
}

export default MainContainer;
