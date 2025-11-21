import api from './api';

export interface Product {
    id: number;
    name: string;
    description: string;
    price: number;
    stock_quantity: number;
    image_url: string;
    category_id: number;
    is_active: boolean;
}

export const productService = {
    getAll: async () => {
        const response = await api.get<Product[]>('/products');
        return response.data;
    },

    getById: async (id: number) => {
        const response = await api.get<Product>(`/products/${id}`);
        return response.data;
    },
};
