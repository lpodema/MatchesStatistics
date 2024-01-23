import React, { useContext, useEffect, useState } from "react";
import PropTypes from "prop-types";
import { ServiceContext } from "../../context/context";

function ServiceWrapper({ children, endpoint, format }) {
  const apiService = useContext(ServiceContext);
  const [loading, setLoading] = useState(true);
  const [data, setData] = useState(undefined);

  const fetchData = async () => {
    try {
      const response = await apiService.apiGet(endpoint, format);
      setData(response.data.results);
      setLoading(false);
    } catch (error) {
      console.error(error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  useEffect(() => {
    const interv = setInterval(() => {
      fetchData();
    }, 10000);
    return () => {
      clearInterval(interv);
    };
  }, []);

  return (
    <div>{!loading && React.cloneElement(children, { loading, data })}</div>
  );
}

ServiceWrapper.propTypes = {
  children: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.node),
    PropTypes.node,
  ]).isRequired,
  endpoint: PropTypes.string.isRequired,
  format: PropTypes.string.isRequired,
};

export default ServiceWrapper;
