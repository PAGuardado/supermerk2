const express = require('express');
const app = express(); //Servidor
const path = require('path'); //Convert path Linux/Windows

//Puerto
app.set('port', 4000);

//Setting
app.set('views', path.join(__dirname + "/views"))
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'ejs');


//Routes
app.use(require('./routes/index'));

//Static files
app.use(express.static(path.join(__dirname + '/public')));

//Listening Server
app.listen(app.get('port'), () => {
  console.log("Server port: ", app.get('port'));
});

//-------------------EDIT---------------------------

const { QueueClient, QueueServiceClient } = require("@azure/storage-queue");
const { strict } = require('assert');

// Retrieve the connection from an environment
// variable called AZURE_STORAGE_CONNECTION_STRING
const connectionString = process.env.AZURE_STORAGE_CONNECTION_STRING;

// Create a unique name for the queue
const queueName = 'new-feedback-q';
const queuePositive = 'positive-feedback-q';
console.log("Creating queue: ", queueName);

// Instantiate a QueueServiceClient which will be used
// to create a QueueClient and to list all the queues
const queueServiceClient = QueueServiceClient.fromConnectionString(connectionString);

// Get a QueueClient which will be used
// to create and manipulate a queue
const queueClient = queueServiceClient.getQueueClient(queueName);
const queuePositiveClient = queueServiceClient.getQueueClient(queuePositive);

//Message to Send
messageText = "Este es un gran mensaje ";
let queueMessage = Buffer.from(messageText).toString('base64');

// Add a message to the queue
const response = async () => {
  try {
    await queueClient.sendMessage(queueMessage);
    const peekedMessages = await queuePositiveClient.peekMessages({ numberOfMessages: 5 });

    for (i = 0; i < peekedMessages.peekedMessageItems.length; i++) {
      // Display the peeked message
      const decodeQueue = Buffer.from(peekedMessages.peekedMessageItems[i].messageText, 'base64').toString('ascii');
      console.log("Peeked message: ", decodeQueue);
    }
  }
  catch (error) {
    console.error(error);
    // expected output: ReferenceError: nonExistentFunction is not defined
    // Note - error messages will vary depending on browser
  }
}
const showMessageQueu = async () => {
  try {
    const peekedMessages = await queuePositiveClient.peekMessages({ numberOfMessages: 5 });

    for (i = 0; i < peekedMessages.peekedMessageItems.length; i++) {
      // Display the peeked message
      const decodeQueue = Buffer.from(peekedMessages.peekedMessageItems[i].messageText, 'base64').toString('ascii');
      const decodeQueueJSON = JSON.parse(decodeQueue);
      console.log("Peeked message: ", (decodeQueueJSON.originalMessage));
    }
  }
  catch (error) {
    console.error(error);
    // expected output: ReferenceError: nonExistentFunction is not defined
    // Note - error messages will vary depending on browser
  }
}
// Peek at messages in the queue

//console.log(response());
//console.log(path.join(__dirname +'/public/js/main.js'));
const recibirHTML = require(path.join(__dirname +'/public/js/main.js'));

console.log(showMessageQueu());
