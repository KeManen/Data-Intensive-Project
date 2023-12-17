import axios, { AxiosResponse, AxiosError } from 'axios';

const apiUrl = 'http://python_server:8000';

export const get = async (url: string): Promise<AxiosResponse<any>> => {
  try {
    const response: AxiosResponse<any> = await axios.get(`${apiUrl}${url}`);
    return response.data;
  } catch (error) {
    handleApiError(error as AxiosError);
    throw error;
  }
};

export const post = async (url: string, data: any): Promise<AxiosResponse<any>> => {
  try {
    const response: AxiosResponse<any> = await axios.post(`${apiUrl}${url}`, data);
    return response.data;
  } catch (error) {
    handleApiError(error as AxiosError);
    throw error;
  }
};

export const put = async (url: string, data: any): Promise<AxiosResponse<any>> => {
  try {
    const response: AxiosResponse<any> = await axios.put(`${apiUrl}${url}`, data);
    return response.data;
  } catch (error) {
    handleApiError(error as AxiosError);
    throw error;
  }
};

const handleApiError = (error: AxiosError) => {
  console.error('API Request Error:', error.message);
};
