import React, { createContext } from "react";
import PropTypes from "prop-types";
import { useService } from "../services/api";

const apiService = useService();
export const ServiceContext = createContext(apiService);

function ApiContext({ children }) {
  return (
    <ServiceContext.Provider value={apiService}>
      {children}
    </ServiceContext.Provider>
  );
}

ApiContext.propTypes = {
  children: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.node),
    PropTypes.node,
  ]).isRequired,
};

export default ApiContext;
