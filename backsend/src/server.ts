import express from 'express';
import { createServer } from 'http';
import { Http2ServerRequest, Http2ServerResponse } from 'http2';
import { Server } from 'socket.io';

const app = express();
const server = createServer(app);
const io = new Server(server, {
  cors: {
    origin: '*', 
  }
});
app.get('/health', (req, res) => {res.json({ status: 'ok' });});
io.on('connection', (socket) => {
  console.log('A user connected', socket.id);
  
  socket.on('disconnect', () => 
    console.log('A user disconnected', socket.id));

});
server.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});