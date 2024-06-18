// pages/api/signup.js
import bcrypt from 'bcrypt';

let users = [];

export default async (req, res) => {
  if (req.method === 'POST') {
    const { email, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);
    users.push({ email, password: hashedPassword });
    res.status(200).json({ message: 'User registered' });
  } else {
    res.status(405).end();
  }
};
