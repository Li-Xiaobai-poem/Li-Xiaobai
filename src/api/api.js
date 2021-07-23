// appfront/src/api/api.js
import axiosInstance from './index'

const axios = axiosInstance
//从后获取
export const getPoem= () => {return axios.get(`http://localhost:8000/app1/api/`)}
//向后端传送
export const addColloctions = (keyword) => {return axios.post(`http://localhost:8000/app1/api/`, {'name': bookName, 'author': bookAuthor})}
