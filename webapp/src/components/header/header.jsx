import styles from "./header.module.css";

import logo from "../../media/LogoProgramm.png";

const Header = () => {
    return (
      <header className={styles.header}>
        <div className={styles.logo}>
          <img src={logo} alt="Nomeroavto logo" />
        </div>
        <label htmlFor={styles.logo} className={styles.label}>
          Nomeroavto
        </label>
      </header>
    );
}

export default Header