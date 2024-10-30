import styles from "./keyboard.module.css";
import { useDispatch, useSelector } from "react-redux";
import { setSearchValue } from "../../redux/slices/search-slice";

const Keyboard = () => {
  const dispatch = useDispatch();
  const searchValue = useSelector((state) => state.search.value);

  console.log(searchValue);

  const updateValue = (letter) => {
    if (letter === "-") {
      if (searchValue.length > 0) {
        const newSearchValue = searchValue.slice(0, searchValue.length - 1);
        dispatch(setSearchValue(newSearchValue));
      }
      return;
    }
    if (searchValue.length >= 7) {
      return;
    }
    const newSearchValue = searchValue + letter;
    dispatch(setSearchValue(newSearchValue));
  };

  const row1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
  const row2 = ["A", "B", "E", "I", "K", "M", "H"];
  const row3 = ["O", "P", "C", "T", "X"];

  let active_buttons = [];

  if (searchValue.length === 0) {
    active_buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "E"];
  }
  if (searchValue.length >= 1 && searchValue.length <= 3) {
    active_buttons = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
  }
  if (searchValue.length >= 4 && searchValue.length <= 5) {
    active_buttons = [
      "A",
      "B",
      "E",
      "I",
      "K",
      "M",
      "H",
      "O",
      "P",
      "C",
      "T",
      "X",
    ];
  }
  if (searchValue.length >= 6) {
    active_buttons = ["1", "2", "3", "4", "5", "6", "7"];
  }

  console.log(active_buttons)

  return (
    <div className={styles.keyboard}>
      <div className={styles.row}>
        {row1.map((el) => {
          if (active_buttons.includes(el)) {
            return (
              <button onClick={() => updateValue(el)} key={el}>
                {el}
              </button>
            );
          }
          return (
            <button onClick={() => updateValue(el)} disabled={true} key={el}>
              {el}
            </button>
          );
        })}
      </div>
      <div className={styles.row}>
        {row2.map((el) => {
          if (active_buttons.includes(el)) {
            return (
              <button onClick={() => updateValue(el)} key={el}>
                {el}
              </button>
            );
          }
          return (
            <button onClick={() => updateValue(el)} disabled={true} key={el}>
              {el}
            </button>
          );
        })}
      </div>
      <div className={styles.row}>
        {row3.map((el) => {
          if (active_buttons.includes(el)) {
            return (
              <button onClick={() => updateValue(el)} key={el}>
                {el}
              </button>
            );
          }
          return (
            <button onClick={() => updateValue(el)} disabled={true} key={el}>
              {el}
            </button>
          );
        })}
        <button onClick={() => updateValue("-")}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="24"
            height="24"
            viewBox="0 0 24 24"
          >
            <g fill="currentFill" class="nc-icon-wrapper">
              <path d="M6.53451 3H20.9993C21.5516 3 21.9993 3.44772 21.9993 4V20C21.9993 20.5523 21.5516 21 20.9993 21H6.53451C6.20015 21 5.88792 20.8329 5.70246 20.5547L0.369122 12.5547C0.145189 12.2188 0.145189 11.7812 0.369122 11.4453L5.70246 3.4453C5.88792 3.1671 6.20015 3 6.53451 3ZM7.06969 5L2.40302 12L7.06969 19H19.9993V5H7.06969ZM12.9993 10.5858L15.8277 7.75736L17.242 9.17157L14.4135 12L17.242 14.8284L15.8277 16.2426L12.9993 13.4142L10.1709 16.2426L8.75668 14.8284L11.5851 12L8.75668 9.17157L10.1709 7.75736L12.9993 10.5858Z"></path>
            </g>
          </svg>
        </button>
      </div>
    </div>
  );
};

export default Keyboard;
