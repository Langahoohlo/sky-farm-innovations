import { SignIn } from "@clerk/nextjs";
import { ClerkProvider, SignInButton, SignedIn, SignedOut, UserButton } from '@clerk/nextjs'

export default function Page() {
  return (
    <section className="items-center h-full" >
      <div className="justify-center items-center flex" style={{ height: '941px' }}>
        <SignIn />
      </div>
    </section>
  )
}