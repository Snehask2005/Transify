use anchor_lang::prelude::*;
use anchor_lang::system_program;
use anchor_lang::solana_program::program::invoke;

declare_id!("9F1UFZuVunCtAJzvSyefpxzJLvzbfqu1npZxqdsvZGXz");

#[program]
pub mod transify_token {
    use super::*;

    pub fn initialize_user(ctx: Context<InitializeUser>) -> Result<()> {
        let user = &mut ctx.accounts.user;
        user.rides = 0;
        user.rewards = 0;
        Ok(())
    }

    pub fn log_ride(ctx: Context<LogRide>) -> Result<()> {
        let user = &mut ctx.accounts.user;
        user.rides += 1;
        user.rewards += 10; // reward 10 tokens per ride
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeUser<'info> {
    #[account(init, payer = signer, space = 8 + 8 + 8)]
    pub user: Account<'info, UserAccount>,
    #[account(mut)]
    pub signer: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct LogRide<'info> {
    #[account(mut)]
    pub user: Account<'info, UserAccount>,
}

#[account]
pub struct UserAccount {
    pub rides: u64,
    pub rewards: u64,
}