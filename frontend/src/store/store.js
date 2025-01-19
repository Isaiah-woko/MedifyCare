import { configureStore } from '@reduxjs/toolkit';
import servicesReducer from './reducer/servicesSlice';

const store = configureStore({
  reducer: {
    services: servicesReducer,
  },
});

export default store;