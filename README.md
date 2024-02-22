Lesson Completion Guide

This guide provides step-by-step instructions for completing the lesson. Follow these instructions to set up your GitHub repository and deploy a static website using Amazon S3, GitHub Actions, and IAM roles.

Step 1: Create a GitHub Repository

Go to GitHub and sign in to your account.
Click on the "+" sign in the top right corner and select "New repository."
Enter a name for your repository and add a description if needed.
Choose whether the repository will be public or private and click "Create repository."

Step 2: Create Required Files/Resources for the Website

Create an index.html file and any other necessary files (e.g., CSS, JavaScript) for your website.
Add content to your files to create the desired layout and functionality for your website.

Step 3: Set Up Amazon S3 Bucket for Hosting

Go to the Amazon S3 Management Console.
Click on "Create bucket" and enter a name for your bucket.
Make sure that the bucket's content is freely visible and enable "static website hosting."
Update the bucket policy to provide permission for everyone to view the stored files.

Step 4: Create a Separate IAM Role for GitHub

Go to the IAM Management Console.
Click on "Roles" in the sidebar and then "Create role."
Choose the service that will use this role (GitHub) and click "Next: Permissions."
Search for and attach the "AmazonS3FullAccess" policy.
Review the role and click "Next: Tags" and then "Next: Review."
Enter a name for the role and click "Create role."

Step 5: Create a "GitHub Actions" Folder and YAML File

In your GitHub repository, create a folder named .github/workflows.
Inside this folder, create a YAML file (e.g., deploy.yml) for your GitHub Actions workflow.

.yaml content

name: Deploy to S3

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1
      - name: Sync files to S3
        run: aws s3 sync . s3://your-bucket-name --delete
        
Note: Do not store secrets in your YAML file. Use GitHub Secrets or other secure methods.

Step 6: Enable GitHub Actions Workflow

Commit your changes to the repository.
Go to the "Actions" tab in your GitHub repository.
Click on "Set up this workflow" next to the workflow file you created.
Click on "Start commit" and then "Commit new file" to enable the workflow.

Step 7: View Your Website

Wait for the GitHub Actions workflow to run and deploy your files to the S3 bucket.
Once the workflow has completed successfully, navigate to the "Properties" tab of your S3 bucket in the AWS Management Console.
Find the "Static website hosting" section and click on the provided link to view your website.
