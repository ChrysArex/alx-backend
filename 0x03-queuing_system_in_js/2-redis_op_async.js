import { createClient, print } from 'redis';

const util = require('util');

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ',
  err.message));

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const get = util.promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const name = await get(schoolName);
  console.log(name);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
