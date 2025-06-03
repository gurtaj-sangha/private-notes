import { io, Socket } from 'socket.io-client';
import { useMemo } from "react";

export const useSocket = (): Socket => {
    return useMemo(() => io('http://localhost:3000'), []);
};