import { configureStore } from '@reduxjs/toolkit'

import { searchSlice } from './slices/search-slice'

export const store = configureStore({
  reducer: {
    search: searchSlice.reducer
  }
})
