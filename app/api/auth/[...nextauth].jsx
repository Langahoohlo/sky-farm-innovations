// pages/api/auth/[...nextauth].js
import NextAuth from 'next-auth';
import Providers from 'next-auth/providers';
import bcrypt from 'bcrypt';

const users = [];

export default NextAuth({
  providers: [
    Providers.Credentials({
      name: 'Credentials',
      credentials: {
        email: { label: "Email", type: "text" },
        password: { label: "Password", type: "password" }
      },
      async authorize(credentials) {
        const user = users.find(user => user.email === credentials.email);
        if (user && bcrypt.compareSync(credentials.password, user.password)) {
          return { email: user.email };
        }
        return null;
      }
    })
  ],
  session: {
    jwt: true
  },
  callbacks: {
    async jwt(token, user) {
      if (user) {
        token.email = user.email;
      }
      return token;
    },
    async session(session, token) {
      session.user.email = token.email;
      return session;
    }
  },
  pages: {
    signIn: '/auth/signin'
  }
});
