import React from "react";
import "./App.css";
import Container from "./components/MainContainer";
import ApiContext, { ServiceContext } from "./context/context";

function MainApp() {
  return (
    <React.StrictMode>
      <div className="App">
        <main>
          <ApiContext value={ServiceContext}>
            <Container />
          </ApiContext>
        </main>
      </div>
    </React.StrictMode>
  );
}

export default MainApp;
