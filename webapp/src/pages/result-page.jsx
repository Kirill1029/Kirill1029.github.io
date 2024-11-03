import styles from "./result-page.module.css";

import Header from "../components/header/header";

import Record from "../components/record/record";
import { useDispatch, useSelector } from "react-redux";
import {
  setCarInfo,
  setSearchStatus,
  setSearchValue,
} from "../redux/slices/search-slice";

function ResultPage() {
  const car_info = useSelector((state) => state.search.car_info);
  const dispatch = useDispatch();
  console.log(car_info);
  return (
    <>
      <Header />
      <button
        className={styles.back}
        onClick={() => {
          dispatch(setSearchStatus("searching"));
          dispatch(setCarInfo(null));
          dispatch(setSearchValue(""));
        }}
      >
        X
      </button>
      {car_info.records.map((el) => (
        <Record record={el} />
      ))}
    </>
  );
}

export default ResultPage;
