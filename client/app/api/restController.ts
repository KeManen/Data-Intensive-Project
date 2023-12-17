// api.ts

import axios, { AxiosResponse, AxiosError } from 'axios';

const apiUrl = 'http://0.0.0.0:8000';

interface ApiResponse<T = any> {
  data: T;
}

export const get = async <T>(url: string): Promise<ApiResponse<T>> => {
  try {
    const response: AxiosResponse<T> = await axios.get(`${apiUrl}${url}`);
    return { data: response.data };
  } catch (error) {
    handleApiError(error as AxiosError);
    throw error;
  }
};

export const post = async <T>(url: string, data: any): Promise<ApiResponse<T>> => {
  try {
    const response: AxiosResponse<T> = await axios.post(`${apiUrl}${url}`, data);
    return { data: response.data };
  } catch (error) {
    handleApiError(error as AxiosError);
    throw error;
  }
};

// You can add more functions like put, delete, etc. as needed

const handleApiError = (error: AxiosError) => {
  // Handle error logging, redirection, or any other logic here
  console.error('API Request Error:', error.message);
};
