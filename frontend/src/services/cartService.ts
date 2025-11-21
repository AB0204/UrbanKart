import api from './api';

export interface CartItem {
    id: number;
    product_id: number;
    product_name: string;
    product_price: number;
    product_image: string;
    quantity: number;
    subtotal: number;
}

export const cartService = {
    getCart: async () => {
        const response = await api.get<CartItem[]>('/cart');
        return response.data;
    },

    addToCart: async (productId: number, quantity: number = 1) => {
        const response = await api.post('/cart', { product_id: productId, quantity });
        return response.data;
    },

    updateQuantity: async (itemId: number, quantity: number) => {
        const response = await api.put(`/cart/${itemId}`, { quantity });
        return response.data;
    },

    removeItem: async (itemId: number) => {
        await api.delete(`/cart/${itemId}`);
    },

    clearCart: async () => {
        await api.delete('/cart');
    },
};
