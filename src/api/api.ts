import axios from 'axios';

export interface DataItem {
    SvrSeid: number;
    SvrSrt: number;
    seid: number;
    SRT: number;
    type: string;
    name: string;
    deviceAddress: string;
    deviceHostName: string;
    severity: string;
    destinationAddress: string;
    destinationUserName: string;
    sourceAddress: string;
    sourceUserName: string;
    deviceVendor: string;
    deviceProduct: string;
    agentAddress: string;
}

export interface RadarDataItem {
    argument: string;
    number: number;
    max: number;
    min: number;
    cnt: number;
}

export interface BarChartDataItem {
    destinationUserName: string;
    sum: number;
}

export interface PieChartDataItem {
    destinationAddress: string;
    sum: number;
}

export const apiUrl = import.meta.env.VITE_API_URL as string;

if (!apiUrl) {
    throw new Error('VITE_API_URL is not defined in the environment variables.');
}

export async function fetchData(): Promise<DataItem[]> {
    try {
        const response = await axios.get<DataItem[]>(`${apiUrl}/data`);
        return response.data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw new Error('Failed to fetch data');
    }
}

export async function fetchRadarData(): Promise<RadarDataItem[]> {
    try {
        const response = await axios.get<RadarDataItem[]>(`${apiUrl}/radar`);
        return response.data;
    } catch (error) {
        console.error('Error fetching radar data:', error);
        throw new Error('Failed to fetch radar data');
    }
}

export async function fetchPieChartData(): Promise<PieChartDataItem[]> {
    try {
        const response = await axios.get<PieChartDataItem[]>(`${apiUrl}/pie_chart`);
        return response.data;
    } catch (error) {
        console.error('Error fetching pie chart data:', error);
        throw new Error('Failed to fetch pie chart data');
    }
}

export async function fetchBarChartData(): Promise<BarChartDataItem[]> {
    try {
        const response = await axios.get<BarChartDataItem[]>(`${apiUrl}/bar_chart`);
        return response.data;
    } catch (error) {
        console.error('Error fetching bar chart data:', error);
        throw new Error('Failed to fetch bar chart data');
    }
}