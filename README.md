# Why should kubectl apply not be used in CI?
- CI should only build and test code, not deploy
- Applying directly can casue unstable deployments and environment inconsistencec
- CI is used to create artifacts while CD used for deploy

# Why is latest a bad Docker tag?
- You don’t know which exact version is running.
- Make rollbacks will be difficult 

# Difference between CI and CD:
- CI = build & test the code , runs on every push/PR , produces artifacts
- CD = deploy code to envs , runs after build or release , updates clusters / servers

# How does this pipeline support GitOps?
- CI builds a Docker image tagged with the commit SHA
- Argo CD (or Helm) automatically syncs the cluster with Git
- No manual deployment steps → safe, repeatable, and fully traceable.