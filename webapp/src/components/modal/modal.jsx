import styles from "./modal.module.css";

const Modal = (props) => {
  const modal = props.modal;
  const setModal = props.setModal;
  if (modal.is_shown)
    return (
      <>
        <div className={styles.background}></div>
        <div className={styles.modal}>
          <button
            className={styles.close}
            onClick={() =>
              setModal({
                is_shown: false,
                title: "",
                text: "",
              })
            }
          >
            x
          </button>
          <h2 className={styles.title}>{modal.title}</h2>
          <p className={styles.text}>{modal.text}</p>
          <button
            className={styles.ok}
            onClick={() =>
              setModal({
                is_shown: false,
                title: "",
                text: "",
              })
            }
          >
            OK
          </button>
        </div>
      </>
    );
  return <></>;
};

export default Modal;
