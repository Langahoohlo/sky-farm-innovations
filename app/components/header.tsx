import Link from "next/link";
import { SignedIn, SignedOut, SignOutButton, UserButton } from "@clerk/nextjs";

function Header() {

  return (
    <div className="bg-gray-600 text-neutral-50">
      <div className="container mx-auto flex items-center justify-between py-4">
        <Link href="/">Home</Link>
        <div>
          <SignedIn>
            <div className="flex gap-4 items-center">
              <UserButton showName />
              <SignOutButton/>
            </div>
          </SignedIn>
          <SignedOut>
            <div className="flex gap-4 items-center">
              <Link href="/sign-up">Sign Up</Link>
              <Link href="/sign-in">Sign In</Link>
            </div>
          </SignedOut>
        </div>
      </div>
    </div>
  );
}

export default Header;
