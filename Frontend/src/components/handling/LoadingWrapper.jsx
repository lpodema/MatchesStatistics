import React, { Suspense } from "react";
import PropTypes from "prop-types";

function Loading({ children }) {
  return (
    <Suspense fallback={<p>Loading.................</p>}>{children}</Suspense>
  );
}

Loading.propTypes = {
  children: PropTypes.oneOfType([
    PropTypes.arrayOf(PropTypes.element),
    PropTypes.element.isRequired,
  ]).isRequired,
};

export default Loading;
