# Generating an SSH Key for Secure Authentication

SSH (Secure Shell) keys provide a secure and convenient way to authenticate with
remote servers and services like GitHub, GitLab, and other repositories.
This guide explains how to generate and configure an SSH key for secure authentication.

---

## Step 1: Generate an SSH Key

To generate an SSH key using the Ed25519 algorithm (recommended for security and performance),
run the following command:

```sh
ssh-keygen -t ed25519 -C "your-email@example.com"
```

- `-t ed25519`: Specifies the Ed25519 algorithm, which is more secure and faster than RSA.
- `-C "your-email@example.com"`: Adds a comment (your email) to help identify the key.

When prompted:

- **Enter a file location:** Press **Enter** to use the default path (`~/.ssh/id_ed25519`).
- **Enter a passphrase (optional):** You can add a passphrase for additional security or leave it empty for convenience.

---

## Step 2: Start the SSH Agent

The SSH agent keeps your key unlocked while you work, so you don’t need to enter the passphrase every time.

Run the following command:

```sh
eval "$(ssh-agent -s)"
```

For **Fish shell**, use:

```sh
eval (ssh-agent -s)
```

---

## Step 3: Configure SSH to Use the Key

Create or update your SSH configuration file:

```sh
touch ~/.ssh/config
```

Then, add the following content to `~/.ssh/config`:

```config
Host *
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_ed25519
```

This configuration ensures:

- Your SSH key is automatically added to the agent.
- The correct key (`~/.ssh/id_ed25519`) is used by default.

---

## Step 4: Add Your SSH Key to the Agent

To ensure your SSH key is loaded, run:

```sh
ssh-add ~/.ssh/id_ed25519
```

---

## Step 5: Copy Your SSH Public Key

To copy your SSH public key, use:

```sh
bat ~/.ssh/id_ed25519.pub
```

If `bat` is not installed, use `cat` instead:

```sh
cat ~/.ssh/id_ed25519.pub
```

Copy the output and add it to your GitHub SSH keys at:
[GitHub SSH Key Settings](https://github.com/settings/keys)

- Click **New SSH Key**.
- Paste the copied key.
- Give it a title (e.g., “My Laptop” or “Work Computer”).
- Click **Add SSH Key**.

---

## Step 6: Test the Connection

To verify that GitHub recognizes your SSH key, run:

```sh
ssh -T git@github.com
```

Type `yes`

You should see a message like:

```text
Hi {user name}! You've successfully ...
```

If you see a permission error, ensure your SSH key is correctly added and try again.
