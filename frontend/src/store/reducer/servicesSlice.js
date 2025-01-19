import { createSlice } from '@reduxjs/toolkit';
import service from '../../api/services.json'

const servicesSlice = createSlice({
  name: 'services',
  initialState: {
    allSerices: service,
    services: [],
    status: 'idle',
    error: null,
  },
  reducers: {},
});

export default servicesSlice.reducer;
