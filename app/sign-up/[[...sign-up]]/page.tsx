import { SignUp } from "@clerk/nextjs";
import { ClerkProvider, SignInButton, SignedIn, SignedOut, UserButton } from '@clerk/nextjs'

export default function Page() {
  return (
        <section>
           <div className="center-content">
            <SignUp/>
        </div> 
        </section>
  )
}