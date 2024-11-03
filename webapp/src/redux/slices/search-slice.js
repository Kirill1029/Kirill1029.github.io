import { createSlice } from "@reduxjs/toolkit";

export const searchSlice = createSlice({
  name: "search",
  initialState: {
    value: "",
    status: "searching",
    car_info: null,
    modal: {
      is_shown: false,
      title: "",
      text: "",
    },
  },
  reducers: {
    setSearchValue: (state, action) => {
      state.value = action.payload;
    },
    setSearchStatus: (state, action) => {
      state.status = action.payload;
    },
    setCarInfo: (state, action) => {
      state.car_info = action.payload;
    },
    setModal: (state, action) => {
      state.modal = action.payload;
    }
  },
});

export const { setSearchValue, setSearchStatus, setCarInfo, setModal } =
  searchSlice.actions;
