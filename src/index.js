const express = require('express');
const app = express(); //Servidor
const path = require('path'); //Convert path Linux/Windows

//Puerto
app.set('port', 4000);

//Setting
app.set('views',path.join(__dirname +"/views"))
app.engine('html',require('ejs').renderFile);
app.set('view engine','ejs');


//Routes
app.use(require('./routes/index'));

//Static files
app.use(express.static(path.join(__dirname+'/public')));

//Listening Server
app.listen(app.get('port'), () => {
    console.log("Server port: ",app.get('port'));
});

//-------------------EDIT---------------------------
/*
const { QueueClient, QueueServiceClient } = require("@azure/storage-queue");

// Retrieve the connection from an environment
// variable called AZURE_STORAGE_CONNECTION_STRING
const connectionString = "DefaultEndpointsProtocol=https;AccountName=teststorageaccount4queue;AccountKey=cfghQPAEPb+Zao/pW5Miz9Qni4Xg/IY37QlsqXVnRPg5cZHCC2C1YplXz5AsN+3yemkEDzcDuAyOj+akIJ2LEg==;EndpointSuffix=core.windows.net";

// Create a unique name for the queue
const queueName = "myqueue-" + '1';

console.log("Creating queue: ", queueName);

// Instantiate a QueueServiceClient which will be used
// to create a QueueClient and to list all the queues
const queueServiceClient = QueueServiceClient.fromConnectionString(connectionString);

// Get a QueueClient which will be used
// to create and manipulate a queue
const queueClient = queueServiceClient.getQueueClient(queueName);



messageText = "Hola soy David 2";
console.log("Adding message to the queue: ", messageText);

// Add a message to the queue
const response = async () => {
    try
    {
      await queueClient.sendMessage(messageText);
    }
    catch (error) {
      console.error(error);
      // expected output: ReferenceError: nonExistentFunction is not defined
      // Note - error messages will vary depending on browser
    }
} 

console.log(response());
*/