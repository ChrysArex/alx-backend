import { createClient } from 'redis';

const client = createClient();
const subscriber = client.duplicate();

subscriber.on('connect', () => console.log('Redis client connected to the server'));
subscriber.on('error', (err) => console.log(`Redis client not connected to the server: ${err.message}`));

subscriber.SUBSCRIBE('holberton school channel');
subscriber.on('message', (channel, message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    process.exit();
  }
});
