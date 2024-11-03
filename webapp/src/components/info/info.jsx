import styles from "./info.module.css";

const Info = () => {
  return (
    <div className={styles.info}>
      <p>
        Добро пожаловать в Номероавто РБ🇧🇾! Это&nbsp;— единственный в Беларуси
        Telegram-бот для регистрации и получения информации об авто и его
        владельце в Республике Беларусь!
      </p>
    </div>
  );
};

export default Info;
