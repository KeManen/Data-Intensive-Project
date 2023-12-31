import axios, { AxiosResponse, AxiosError, AxiosRequestConfig, AxiosHeaderValue } from 'axios';

const apiUrl = 'http://localhost:8000';


export const get = async (url: string, token?: string): Promise<AxiosResponse<any>> => {
  console.log(token)
  try {
    const response: AxiosResponse<any> = await axios.get(`${apiUrl}${url}`, getHeaders(url, token));
    return response.data;
  } catch (error) {
    handleApiError(error as AxiosError);
    throw error;
  }
};

export const post = async (url: string, data: any, token?: string): Promise<AxiosResponse<any>> => {
  console.log(token)
  try {
    const response: AxiosResponse<any> = await axios.post(`${apiUrl}${url}`, data, getHeaders(url, token));
    console.log('Response', response)
    return response.data;
  } catch (error) {
    handleApiError(error as AxiosError);
    throw error;
  }
};

const handleApiError = (error: AxiosError) => {
  console.error('API Request Error:', error.message);
};

const getHeaders = (url: string, token?: string) => {
  console.log(token)
  if (token && url != '/login' && url != '/signup') {
    let headers: AxiosRequestConfig = {
      headers: {
        token: token as AxiosHeaderValue,
      }
    }
    return headers
  }
  return undefined;
};
