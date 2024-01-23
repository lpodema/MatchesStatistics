const generateFormattedTimeStamp = () => {
  const currentDate = new Date();
  const formatter = new Intl.DateTimeFormat("es-ES", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
  const formattedDate = formatter.format(currentDate);
  return formattedDate;
};

export default generateFormattedTimeStamp;
