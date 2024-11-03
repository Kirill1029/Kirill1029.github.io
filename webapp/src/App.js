import "./App.css";

import SearchPage from "./pages/search-page";
import ResultPage from "./pages/result-page";
import Modal from "./components/modal/modal";

import { useDispatch, useSelector } from "react-redux";
import { setModal, setSearchStatus } from "./redux/slices/search-slice";

function App() {
  const status = useSelector((state) => state.search.status);
  const modal = useSelector((state) => state.search.modal);

  const dispatch = useDispatch();

  return (
    <div className="App">
      <Modal
        modal={modal}
        setModal={(val) => {
          dispatch(setModal(val));
        }}
      />
      {(status === "searching" || status === "loading") && <SearchPage />}
      {status === "load" && <ResultPage />}
    </div>
  );
}

export default App;
