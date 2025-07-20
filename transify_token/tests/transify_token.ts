import * as anchor from "@coral-xyz/anchor";
import { Program } from "@coral-xyz/anchor";
import { TransifyToken } from "../target/types/transify_token";

describe("transify_token", () => {
  // Configure the client to use the local cluster.
  const provider = anchor.AnchorProvider.env();
  anchor.setProvider(provider);

  const program = anchor.workspace.transifyToken as Program<TransifyToken>;

  it("Initializes a user and logs a ride", async () => {
    const user = anchor.web3.Keypair.generate();

    // Initialize
    await program.methods
      .initializeUser()
      .accounts({
        user: user.publicKey,
        signer: provider.wallet.publicKey,
        //systemProgram: anchor.web3.SystemProgram.programId,
      })
      .signers([user])
      .rpc();

    // Log Ride
    await program.methods
      .logRide()
      .accounts({
        user: user.publicKey,
      })
      .rpc();

    const account = await program.account.userAccount.fetch(user.publicKey);
    console.log("🚍 Rides:", account.rides.toString()); // should be 1
    console.log("🎁 Rewards:", account.rewards.toString()); // should be 10
  });
});
