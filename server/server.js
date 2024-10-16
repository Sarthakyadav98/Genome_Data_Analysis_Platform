import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import db from './db.js'; // Ensure to use the .js extension for local files

// Initialize Express
const app = express();
app.use(cors());
app.use(bodyParser.json());

// Login Endpoint
app.post('/login', (req, res) => {
  const { clientId, password } = req.body;

  // Query to validate the user login based on client_id and password
  const query = `
    SELECT User.user_id, User.name, Client.status
    FROM User
    JOIN Client ON User.user_id = Client.client_id
    WHERE Client.client_id = ? AND User.password = ?;
  `;

  db.query(query, [clientId, password], (err, result) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ message: 'Server error' });
    }

    if (result.length > 0) {
      res.json({ success: true, user: result[0] });
    } else {
      res.json({ success: false, message: 'Invalid client ID or password' });
    }
  });
});

// Start the Server
app.listen(3000, () => {
  console.log('Server is running on port 5000');
});