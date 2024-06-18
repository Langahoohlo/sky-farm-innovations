// pages/protected.js
import { getSession } from 'next-auth/react';

export default function Protected() {
  return <div>This is a protected route</div>;
}

export async function getServerSideProps(context) {
  const session = await getSession(context);
  if (!session) {
    return {
      redirect: {
        destination: '/auth/signin',
        permanent: false,
      }
    };
  }
  return {
    props: { session }
  };
}
