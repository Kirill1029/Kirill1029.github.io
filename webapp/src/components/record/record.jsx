import styles from "./record.module.css";

const Record = (props) => {
  const record = props.record;
  console.log(record);
  const date = new Date(record.timestamp * 1000);
  return (
    <div className={styles.record}>
      <h2 className={styles.title}>
        {`${date.getDate()}-${date.getMonth() + 1}-${date.getFullYear()}`}.{" "}
        {record.place}
      </h2>
      <p className={styles.description}>{record.description}</p>
      {record.photo_id && (
        <img
          alt=""
          className={styles.image}
          src={
            "http://localhost:8000/get-photo?photo_id=" + record.photo_id
          }
        />
      )}
      {record.verified === 1 && (
        <span className={styles.verified}>Верифицировано</span>
      )}
    </div>
  );
};

export default Record;
