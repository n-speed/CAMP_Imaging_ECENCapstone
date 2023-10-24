const { MongoClient } = require('mongodb');

// MongoDB connection information
const mongoURI = "mongodb+srv://sethroyder:l427r7bjOEpyBuKf@capstonecluster.d4azdqr.mongodb.net/";
const dbName = "test";
const collectionName = "collection_test";

// Create a MongoClient
const client = new MongoClient(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });

async function connectAndQueryMongoDB() {
    try {
        // Connect to MongoDB
        await client.connect();
        console.log('Connected to MongoDB');

        // Get a reference to the database
        const db = client.db(dbName);

        // Get a reference to the collection
        const collection = db.collection(collectionName);

        // Retrieve all documents from the collection and convert to an array
        const allDocuments = await collection.find({}).toArray();

        // Print the first document
        console.log(allDocuments[0]);

    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
    } finally {
        // Don't forget to close the connection when done
        await client.close();
    }
}

connectAndQueryMongoDB();
