import {
  setCarInfo,
  setModal,
  setSearchStatus,
} from "../../redux/slices/search-slice";
import styles from "./input.module.css";

import { useDispatch, useSelector } from "react-redux";

import axios from "axios";

const Input = () => {
  const searchValue = useSelector((state) => state.search.value);
  const searchStatus = useSelector((state) => state.search.searchStatus);
  const dispatch = useDispatch();

  let isElectro = false;
  if (searchValue.length > 0) {
    if (searchValue[0] === "E") {
      isElectro = true;
    }
  }

  return (
    <div className={styles.input}>
      {isElectro ? (
        <input
          type="text"
          placeholder="1234AA3"
          readOnly={true}
          value={searchValue}
          style={{ color: "green" }}
        />
      ) : (
        <input
          type="text"
          placeholder="1234AA3"
          readOnly={true}
          value={searchValue}
        />
      )}
      <div className={styles.search}>
        <button
          disabled={searchValue.length !== 7}
          loading={"" + (searchStatus === "loading")}
          onClick={() => {
            dispatch(setSearchStatus("loading"));

            axios
              .get(
                `http://localhost:8000/get-car-info/plate-number?plate_number=${searchValue}`
              )
              .then((response) => {
                console.log(response);
                dispatch(setCarInfo(response.data));
                dispatch(setSearchStatus("load"));
              })
              .catch((error) => {
                if (error.response.status === 404) {
                  dispatch(setSearchStatus("searching"));
                  dispatch(
                    setModal({
                      is_shown: true,
                      title: "Машина не найдена",
                      text: "Машина не найдена в нашей базе данных",
                    })
                  );
                }
              });
          }}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="48"
            height="48"
            viewBox="0 0 48 48"
            fill="#000000"
            stroke="#000000"
          >
            <g
              class="nc-icon-wrapper"
              fill="currentFill"
              stroke-linejoin="miter"
              stroke-linecap="butt"
            >
              <line
                data-color="color-2"
                x1="44"
                y1="44"
                x2="31.314"
                y2="31.314"
                fill="none"
                stroke="currentStroke"
                stroke-linecap="square"
                stroke-miterlimit="10"
                stroke-width="2"
              ></line>{" "}
              <circle
                cx="20"
                cy="20"
                r="16"
                fill="none"
                stroke="currentStroke"
                stroke-linecap="square"
                stroke-miterlimit="10"
                stroke-width="2"
              ></circle>
            </g>
          </svg>
        </button>
      </div>
    </div>
  );
};

export default Input;
