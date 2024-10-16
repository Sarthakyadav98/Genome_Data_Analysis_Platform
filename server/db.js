import { createConnection } from 'mysql'; // Ensure you have mysql package installed

const db = createConnection({
  host: 'localhost',
  user: 'root',
  password: 'mereces', // Ensure this is the correct password for your MySQL user
  database: 'genome',
});

// Connect to the database
db.connect(err => {
  if (err) {
    console.error('Database connection failed:', err.stack);
    return;
  }
  console.log('Database connected as id ' + db.threadId);
});

export default db; // Ensure this is exporting the connection